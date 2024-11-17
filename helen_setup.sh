

# Script to install Visual Studio Code on Raspbian
echo "Starting Visual Studio Code installation..."

# Update package list and install prerequisites
sudo apt install -y wget gpg

# Add Microsoft GPG key
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo install -o root -g root -m 644 microsoft.gpg /usr/share/keyrings/microsoft.gpg
rm microsoft.gpg

# Add the VS Code repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/microsoft.gpg] https://packages.microsoft.com/repos/code stable main" | \
sudo tee /etc/apt/sources.list.d/vscode.list

# Update package list and install VS Code
sudo apt update
sudo apt install -y code

# Confirm installation
echo "Visual Studio Code installed successfully. Launch it using the command: code"

# Uninstall conflicting or old packages
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do
    sudo apt-get remove -y $pkg
done

# Update package lists and install prerequisites
sudo apt-get update
sudo apt-get install -y ca-certificates curl

# Set up Docker GPG key and repository
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/raspbian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/raspbian $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker and plugins
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Verify Docker installation
sudo docker run hello-world

# Pull Containers
sudo docker pull lscr.io/linuxserver/obsidian:latest
sudo docker pull pihole/pihole:latest
sudo docker pull leplusorg/kali
sudo docker pull ollama/ollama
