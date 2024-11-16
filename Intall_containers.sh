docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama


#start 
docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

docker exec -it ollama ollama run llama3


#install open webUI

docker pull ghcr.io/open-webui/open-webui:main


docker run -d -p 3000:8080 -v open-webui:/app/backend/data --name open-webui ghcr.io/open-webui/open-webui:main



docker run -d \
  --name=obsidian \
  --security-opt seccomp=unconfined `#optional` \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Etc/UTC \
  -p 3000:3000 \
  -p 3001:3001 \
  -v /path/to/config:/config \
  --device /dev/dri:/dev/dri `#optional` \
  --shm-size="1gb" \
  --restart unless-stopped \
  lscr.io/linuxserver/obsidian:latest
