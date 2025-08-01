import argparse
import getpass
import os
import subprocess
import sys
import tempfile


def main():
    parser = argparse.ArgumentParser(description="Run docker compose with a provided password.")
    parser.add_argument("compose_file", help="Path to the compose YAML file")
    parser.add_argument("--project-name", "-p", dest="project", default=None,
                        help="Compose project name")
    parser.add_argument("--command", default="up -d",
                        help="Compose command to run (default 'up -d')")
    parser.add_argument("--var", dest="var", default="PASSWORD",
                        help="Environment variable name to set (default PASSWORD)")
    parser.add_argument("--engine", choices=["docker", "podman"], default="podman",
                        help="Container engine to use")
    args = parser.parse_args()

    pw1 = getpass.getpass("Enter password: ")
    pw2 = getpass.getpass("Confirm password: ")
    if pw1 != pw2:
        print("Passwords do not match.")
        sys.exit(1)

    with tempfile.NamedTemporaryFile("w", delete=False) as tmp:
        tmp.write(f"{args.var}={pw1}\n")
        env_file = tmp.name

    engine_cmd = [args.engine, "compose", "--env-file", env_file, "-f", args.compose_file]
    if args.project:
        engine_cmd += ["-p", args.project]
    engine_cmd += args.command.split()

    try:
        subprocess.run(engine_cmd, check=True)
    finally:
        os.remove(env_file)


if __name__ == "__main__":
    main()
