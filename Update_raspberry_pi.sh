#!/bin/bash

# Script to update and upgrade a Raspberry Pi

echo "Starting Raspberry Pi update process..."

# Update package list
echo "Updating package list..."
sudo apt update -y

# Upgrade installed packages
echo "Upgrading installed packages..."
sudo apt upgrade -y

# Full upgrade (if necessary)
echo "Performing a full upgrade..."
sudo apt full-upgrade -y

# Remove unnecessary packages
echo "Cleaning up unnecessary packages..."
sudo apt autoremove -y
sudo apt autoclean -y

# Install Git
echo "Installing Git..."
sudo apt-get install git -y

# Install pyenv
curl https://pyenv.run | bash

#install vs code

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

# Optionally update firmware
read -p "Do you want to update the Raspberry Pi firmware? (y/n): " update_firmware
if [ "$update_firmware" == "y" ]; then
    echo "Updating firmware..."
    sudo rpi-update
else
    echo "Skipping firmware update."
fi

echo "Update process completed. A reboot is recommended."
read -p "Do you want to reboot now? (y/n): " reboot_choice
if [ "$reboot_choice" == "y" ]; then
    echo "Rebooting..."
    sudo reboot
else
    echo "You can reboot later with 'sudo reboot'."
fi
