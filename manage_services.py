#!/usr/bin/env python3
"""Unified helper to manage Helen docker-compose stacks."""

from __future__ import annotations

import argparse
import getpass
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import List, Tuple

SECTIONS = [
    ("Infrastructure services", "docker-compose.Helen-Infrastructure.yml"),
    ("AI services", "docker-compose.Helen-AI.yml"),
]

CATEGORIES = [
    "infrastructure",
    "ai_llm",
    "automation_productivity",
    "networking",
    "media",
    "food_health",
    "development",
    "home_utility",
]


def confirm(prompt: str) -> bool:
    """Prompt the user for yes/no response and return True for yes."""
    while True:
        choice = input(f"{prompt} (y/n): ").strip().lower()
        if choice in {"y", "n"}:
            return choice == "y"
        print("Please enter 'y' or 'n'.")


def run_compose_file(
    compose_file: Path,
    *,
    engine: str = "docker",
    command: str = "up -d",
    env: Path | None = None,
    project: str | None = None,
) -> None:
    """Execute a compose file using the chosen container engine."""
    cmd = [engine, "compose"]
    if env is not None:
        cmd += ["--env-file", str(env)]
    cmd += ["-f", str(compose_file)]
    if project:
        cmd += ["-p", project]
    cmd += command.split()
    subprocess.run(cmd, check=True)


def parse_compose(path: Path) -> Tuple[List[str], List[str]]:
    """Extract port mappings and volume mounts from a compose YAML file.

    This parser is intentionally simple and only handles the subset of YAML
    used by the project compose files. It scans for ``ports`` and ``volumes``
    sections and captures any ``- host:container`` style entries beneath them.
    """

    ports: List[str] = []
    volumes: List[str] = []
    current: str | None = None
    indent_level = 0

    with open(path) as fh:
        for raw in fh:
            if not raw.strip() or raw.strip().startswith("#"):
                continue

            indent = len(raw) - len(raw.lstrip())
            line = raw.strip()

            if line.startswith("ports:"):
                current = "ports"
                indent_level = indent
                continue
            if line.startswith("volumes:"):
                current = "volumes"
                indent_level = indent
                continue

            if current and indent <= indent_level:
                current = None

            if current and line.startswith("-"):
                entry = line[1:].strip().split("#")[0].strip().strip('"')
                if current == "ports":
                    ports.append(entry)
                else:
                    volumes.append(entry)

    return ports, volumes


# ----- install -----

def cmd_install(_: argparse.Namespace) -> None:
    script_dir = Path(__file__).resolve().parent
    for name, fname in SECTIONS:
        compose_path = script_dir / fname
        if not compose_path.exists():
            print(f"Compose file {compose_path} not found, skipping {name}.")
            continue
        if confirm(f"Would you like to install {name}?"):
            run_compose_file(compose_path)
        else:
            print(f"Skipping {name}.")
    print("All sections processed.")


# ----- setup -----

def cmd_setup(args: argparse.Namespace) -> None:
    root = Path(__file__).resolve().parent
    categories = args.categories or CATEGORIES
    for category in categories:
        compose_path = root / category / "docker-compose.yml"
        if not compose_path.exists():
            print(f"Missing compose file for {category}, skipping")
            continue
        print(f"Deploying {category} stack...")
        run_compose_file(compose_path)


# ----- run -----

def cmd_run(args: argparse.Namespace) -> None:
    pw1 = getpass.getpass("Enter password: ")
    pw2 = getpass.getpass("Confirm password: ")
    if pw1 != pw2:
        print("Passwords do not match.")
        sys.exit(1)

    compose_path = Path(args.compose_file)
    ports, volumes = parse_compose(compose_path)

    info_path = Path(__file__).resolve().parent / "deployment_info.txt"
    with info_path.open("a") as info:
        info.write(f"Compose: {compose_path}\n")
        info.write(f"Password: {pw1}\n")
        if ports:
            info.write("Ports:\n")
            for p in ports:
                info.write(f"  - {p}\n")
        if volumes:
            info.write("Volumes:\n")
            for v in volumes:
                info.write(f"  - {v}\n")
        info.write("\n")

    with tempfile.NamedTemporaryFile("w", delete=False) as tmp:
        tmp.write(f"{args.var}={pw1}\n")
        env_file = Path(tmp.name)

    try:
        run_compose_file(
            Path(args.compose_file),
            engine=args.engine,
            command=args.command,
            env=env_file,
            project=args.project,
        )
    finally:
        env_file.unlink(missing_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Manage Helen docker-compose stacks"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sp_install = sub.add_parser("install", help="Interactive install of base stacks")
    sp_install.set_defaults(func=cmd_install)

    sp_setup = sub.add_parser("setup", help="Deploy category stacks")
    sp_setup.add_argument("categories", nargs="*", help="Categories to deploy (default: all)")
    sp_setup.set_defaults(func=cmd_setup)

    sp_run = sub.add_parser("run", help="Run compose with a password variable")
    sp_run.add_argument("compose_file", help="Path to the compose YAML file")
    sp_run.add_argument("--project-name", "-p", dest="project", help="Compose project name")
    sp_run.add_argument(
        "--command",
        default="up -d",
        help="Compose command to run (default 'up -d')",
    )
    sp_run.add_argument(
        "--var",
        dest="var",
        default="PASSWORD",
        help="Environment variable name to set (default PASSWORD)",
    )
    sp_run.add_argument(
        "--engine",
        choices=["docker", "podman"],
        default="podman",
        help="Container engine to use (default podman)",
    )
    sp_run.set_defaults(func=cmd_run)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
