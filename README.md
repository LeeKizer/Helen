# Helen
A home server and Calendar app

🔧 How to Use It
Save the file as docker-compose.yml

Run the stack:

--bash
Copy
Edit
podman-compose -p Helen-Infrastructure up -d
--bash
Access Nginx Proxy Manager at:

http://<your-ip>:81

Default login: admin@example.com / changeme (prompted to reset on first login)

🏗️ Infrastructure
These are the foundational containers that support and enable other services.

Traefik or Caddy – reverse proxy with automatic HTTPS

Portainer – web UI for managing containers

Watchtower – auto-updates containers

Nginx Proxy Manager – alternative GUI-based reverse proxy

Netdata – system monitoring

Uptime Kuma – uptime monitoring

Prometheus + Grafana – metrics and dashboards

Plausible – self-hosted analytics

CrowdSec – security and intrusion detection

Vaultwarden – self-hosted password manager

🧠 AI / LLM
AI model hosting, interfaces, and tools for automation and experimentation.

Ollama – local LLM model runtime

Open WebUI – frontend for interacting with Ollama

Text Generation WebUI – advanced model management

LM Studio – local model interface (if containerized)

FastAPI or Flask API – your own custom LLM tool endpoints

Langchain Server – orchestration layer for LLM agents

Vector DBs (e.g. Qdrant, Weaviate) – for RAG-based retrieval

Jupyter Notebook / VS Code Server – for model testing/development

🔁 Automation / Productivity
Workflow tools, scripting, integrations, and task automation.

n8n – workflow automation (Zapier alternative)

Homebox – digital inventory management

Home Assistant – home automation

Node-RED – low-code automation tool

Tandoor Recipes – recipe and meal planning manager

Mealie – meal planning and shopping list app

Logseq or Outline – personal knowledge base (self-hosted Notion/Obsidian)

Paperless-ngx – document management (scanned docs, PDFs)

🛜 Networking / Access / Security
Tools for remote access, secure tunnels, and network visibility.

WireGuard or OpenVPN – VPN access

Tailscale – easy remote access to your network

Pi-hole – network-wide ad blocker

AdGuard Home – DNS-level blocker with UI

DoH Server (e.g., dnscrypt-proxy) – encrypted DNS

Glances – system and container monitoring

🎬 Media
Media servers and their supporting tools for organization and streaming.

Plex or Jellyfin – media server

Radarr – movies downloader (via Usenet/torrent)

Sonarr – TV series downloader

Bazarr – subtitles automation

Prowlarr – indexer manager

qBittorrent or Transmission – torrent client

Tdarr – media transcoding automation

🧑‍🍳 Food & Health
Nutrition, tracking, and planning tools.

Tandoor Recipes – recipe and nutrition tracker

Mealie – meal planning and shopping

Own calorie tracker API (or link to external like LoseIt! via API)

Grocy – grocery inventory and budgeting

🧪 Development / Coding
Tools for code hosting, dev environments, and collaborative tools.

Code-Server – VS Code in the browser

GitLab / Gitea – Git hosting

PostgreSQL / MariaDB / Redis – common database backends

Minio – S3-compatible object storage

SFTPgo – file transfer and storage

🏡 Home / Utility
Tools that serve home-focused or general life management purposes.

OpenHAB – alternative home automation platform

Grocy – home management (inventory, chores, budgeting)

Immich – self-hosted Google Photos alternative

Photoprism – AI photo organization

Nextcloud – personal cloud storage and apps

Syncthing – file sync across devices

Dashy / Heimdall – dashboard for service access
