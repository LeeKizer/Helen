#!/usr/bin/env python3
"""Pull the top N Ollama models into a running Podman container."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from typing import List

import urllib.request

API_URL = "https://ollama.ai/api/popular?limit={}"  # assumed endpoint

def fetch_top_models(limit: int) -> List[str]:
    """Return the names of the top models from Ollama."""
    with urllib.request.urlopen(API_URL.format(limit), timeout=10) as resp:
        data = json.load(resp)
    return [m["name"] for m in data.get("models", [])]


def pull_models(container: str, models: List[str]) -> None:
    """Run ``ollama pull`` inside the specified container for each model."""
    for model in models:
        print(f"Pulling {model}...")
        subprocess.run(
            ["podman", "exec", container, "ollama", "pull", model],
            check=True,
        )


def main() -> None:
    parser = argparse.ArgumentParser(description="Pull top Ollama models")
    parser.add_argument("n", type=int, help="Number of models to pull")
    parser.add_argument(
        "--container", default="ollama", help="Name of the running Ollama container"
    )

    args = parser.parse_args()

    try:
        models = fetch_top_models(args.n)
    except Exception as exc:  # network or parsing errors
        print(f"Failed to fetch models: {exc}", file=sys.stderr)
        sys.exit(1)

    if not models:
        print("No models returned", file=sys.stderr)
        sys.exit(1)

    pull_models(args.container, models)


if __name__ == "__main__":
    main()
