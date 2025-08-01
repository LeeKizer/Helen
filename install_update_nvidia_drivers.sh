#!/usr/bin/env bash
# Install and update NVIDIA drivers on Debian/Ubuntu

set -euo pipefail

# Update package list
sudo apt-get update

# Install required packages for adding repositories
sudo apt-get install -y software-properties-common gnupg-curl

# Add the graphics drivers PPA if not already added
if ! grep -q "graphics-drivers" /etc/apt/sources.list /etc/apt/sources.list.d/* 2>/dev/null; then
    sudo add-apt-repository -y ppa:graphics-drivers/ppa
fi

# Refresh package lists after adding the PPA
sudo apt-get update

# Install recommended NVIDIA driver
sudo ubuntu-drivers autoinstall

# Reboot prompt
echo "NVIDIA drivers installed/updated. A reboot may be required."
