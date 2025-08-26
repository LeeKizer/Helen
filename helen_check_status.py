#!/usr/bin/env python3
import subprocess
from datetime import datetime
import time
from urllib import request, error

# List of containers and URLs to check
SERVICES = [
    ("mealie", "http://mealie.local"),
    ("grocy", "http://grocy.local"),
    ("paperless-ngx", "http://paperless.local"),
    ("actual", "http://budget.local"),
    ("homebox", "http://homebox.local"),
    ("plex", "http://localhost:32400/web"),  # Plex uses host networking
    ("openwebui", "http://ai.local"),
    ("manyfold", "http://manyfold.local"),
    ("immich-server", "http://immich.local"),
    ("nextcloud", "http://nextcloud.local"),
    ("glance", "http://home.local"),
    ("pinchflat", "http://pinchflat.local"),
]

DOCKER_CMD = ["docker", "ps", "--format", "{{.Names}}"]

def get_running_containers():
    """Return a set of currently running container names."""
    try:
        output = subprocess.check_output(DOCKER_CMD, text=True)
        return set(filter(None, output.splitlines()))
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print("Error checking Docker containers:", e)
        return set()

def check_web(url):
    """Check if a web page is reachable."""
    try:
        start = time.monotonic()
        with request.urlopen(url, timeout=5) as r:
            return r.getcode(), time.monotonic() - start
    except error.URLError:
        return None, None

def main():
    print(f"Container Health Check - {datetime.now().isoformat()}")
    running = get_running_containers()

    for name, url in SERVICES:
        container_status = "UP" if name in running else "DOWN"
        status_code, response_time = check_web(url) if container_status == "UP" else (None, None)

        if status_code is None:
            web_status = "NO RESPONSE"
        else:
            web_status = f"{status_code} ({response_time:.2f}s)"

        print(f"{name:20} | Container: {container_status:4} | Web: {web_status}")

if __name__ == "__main__":
    main()
