#!/usr/bin/env python3
"""Deploy docker compose stacks for each service category."""

import subprocess
from pathlib import Path

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


def run_compose(compose_file: Path) -> None:
    """Run docker compose up for the given compose file."""
    subprocess.run(["docker", "compose", "-f", str(compose_file), "up", "-d"], check=True)


def main() -> None:
    root = Path(__file__).resolve().parent
    for category in CATEGORIES:
        dir_path = root / category
        compose_path = dir_path / "docker-compose.yml"
        if not compose_path.exists():
            print(f"Missing compose file for {category}, skipping")
            continue
        print(f"Deploying {category} stack...")
        run_compose(compose_path)


if __name__ == "__main__":
    main()
