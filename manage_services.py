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

CATEGORIES = [
    "infrastructure",
    "ai_llm",
#    "automation_productivity",
#    "networking",
#    "media",
#    "food_health",
#    "development",
#    "home_utility",
]


def confirm(category: str) -> bool:
    """Prompt the user for yes/no response and return True for yes."""
    print(f"Would you like to ruo the yaml file in {category}?")
    choice = input(f"Please enter 'y' or 'n': ").strip().lower()
    if choice in {"y", "n"}:
        return True

def run_compose_file(category: str) -> None:
    """Execute a compose file using the chosen container engine."""

    engine = "podman-compose"
    command: str = "up -d"
    root = Path(__file__).resolve().parent
    compose_path = root / category / "docker-compose.yml"

    cmd = [engine]
    cmd += ["-f", str(compose_path)]
    cmd += ["-p", category]
    cmd += command.split()
    subprocess.run(cmd, check=True)


def main() -> None:

    for cat in CATEGORIES:
        if confirm(cat):
            run_compose_file(cat)


if __name__ == "__main__":
    main()

