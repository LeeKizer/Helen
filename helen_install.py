import os
import subprocess

SECTIONS = [
    ("Infrastructure services", "docker-compose.Helen-Infrastructure.yml"),
    ("AI services", "docker-compose.Helen-AI.yml"),
]


def confirm(prompt: str) -> bool:
    """Prompt the user for yes/no response and return True for yes."""
    while True:
        choice = input(f"{prompt} (y/n): ").strip().lower()
        if choice in {"y", "n"}:
            return choice == "y"
        print("Please enter 'y' or 'n'.")


def run_compose(compose_file: str) -> None:
    """Run docker compose up -d for the given compose file."""
    print(f"Running compose file: {compose_file}")
    subprocess.run([
        "docker",
        "compose",
        "-f",
        compose_file,
        "up",
        "-d",
    ], check=True)


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    for name, filename in SECTIONS:
        path = os.path.join(script_dir, filename)
        if confirm(f"Would you like to install {name}?"):
            run_compose(path)
        else:
            print(f"Skipping {name}.")
    print("All sections processed.")
