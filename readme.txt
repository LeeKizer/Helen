Helen
=====

This repository collects docker-compose stacks for a personal home server.

Prerequisites
-------------
- Docker or Podman with the compose plugin
- Python 3.8+ to run `manage_services.py`

Usage
-----
1. Clone this repository.
2. Ensure the prerequisites above are installed.
3. Deploy all service stacks with:
   `python manage_services.py setup`
4. To run an individual compose file:
   `python manage_services.py run <compose-file> -p <project>`

Containers
----------
Infrastructure
* [Nginx Proxy Manager](https://nginxproxymanager.com/)
* [Portainer](https://www.portainer.io/)
* [Watchtower](https://containrrr.dev/watchtower/)
* [Netdata](https://www.netdata.cloud/)
* [Uptime Kuma](https://github.com/louislam/uptime-kuma)
* [Plausible](https://plausible.io/)
* [Prometheus](https://prometheus.io/)
* [Grafana](https://grafana.com/)
* [CrowdSec](https://www.crowdsec.net/)
* [Vaultwarden](https://github.com/dani-garcia/vaultwarden)

AI / LLM
* [Ollama](https://ollama.ai/)
* [Open WebUI](https://github.com/open-webui/open-webui)
* [Text Generation WebUI](https://github.com/oobabooga/text-generation-webui)
* [LM Studio](https://lmstudio.ai/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Langchain Server](https://github.com/hwchase17/langchain)
* [Qdrant](https://qdrant.tech/)
* [Weaviate](https://weaviate.io/)
* [Jupyter Notebook](https://jupyter.org/)
* [VS Code Server](https://github.com/coder/code-server)

Automation / Productivity
* [n8n](https://n8n.io/)
* [Homebox](https://github.com/hay-kot/homebox)
* [Home Assistant](https://www.home-assistant.io/)
* [Node-RED](https://nodered.org/)
* [Tandoor Recipes](https://tandoor.dev/)
* [Mealie](https://github.com/mealie-recipes/mealie)
* [Logseq](https://logseq.com/)
* [Outline](https://www.getoutline.com/)
* [Paperless-ngx](https://paperless-ngx.com/)

Networking / Access / Security
* [WireGuard](https://www.wireguard.com/)
* [OpenVPN](https://openvpn.net/)
* [Tailscale](https://tailscale.com/)
* [Pi-hole](https://pi-hole.net/)
* [AdGuard Home](https://adguard.com/adguard-home/overview.html)
* [dnscrypt-proxy](https://github.com/DNSCrypt/dnscrypt-proxy)
* [Glances](https://nicolargo.github.io/glances/)

Media
* [Plex](https://www.plex.tv/) / [Jellyfin](https://jellyfin.org/)
* [Radarr](https://radarr.video/)
* [Sonarr](https://sonarr.tv/)
* [Bazarr](https://www.bazarr.media/)
* [Prowlarr](https://wiki.servarr.com/prowlarr)
* [qBittorrent](https://www.qbittorrent.org/) / [Transmission](https://transmissionbt.com/)
* [Tdarr](https://github.com/HaveAGitGat/Tdarr)

Food & Health
* [Tandoor Recipes](https://tandoor.dev/)
* [Mealie](https://github.com/mealie-recipes/mealie)
* [Calorie API](https://fastapi.tiangolo.com/)
* [Grocy](https://grocy.info/)

Development / Coding
* [Code-Server](https://github.com/coder/code-server)
* [Gitea](https://gitea.io/) / [GitLab](https://about.gitlab.com/)
* [PostgreSQL](https://www.postgresql.org/) / [MariaDB](https://mariadb.org/) / [Redis](https://redis.io/)
* [Minio](https://min.io/)
* [SFTPgo](https://github.com/drakkan/sftpgo)

Home / Utility
* [OpenHAB](https://www.openhab.org/)
* [Grocy](https://grocy.info/)
* [Immich](https://github.com/immich-app/immich)
* [Photoprism](https://photoprism.app/)
* [Nextcloud](https://nextcloud.com/)
* [Syncthing](https://syncthing.net/)
* [Dashy](https://github.com/Lissy93/dashy) / [Heimdall](https://heimdall.site/)
