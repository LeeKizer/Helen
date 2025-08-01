#!/usr/bin/env bash
# Install and update NVIDIA drivers on Debian 12

set -euo pipefail

# Ensure contrib and non-free components are enabled
if ! grep -Eq "non-free" /etc/apt/sources.list /etc/apt/sources.list.d/* 2>/dev/null; then
    echo "Enabling contrib and non-free repositories" >&2
    sudo sed -i 's/main$/main contrib non-free non-free-firmware/' /etc/apt/sources.list
fi

# Update package list
sudo apt-get update

# Install build dependencies
sudo apt-get install -y linux-headers-$(uname -r) build-essential dkms

# Install the NVIDIA driver from Debian repositories
sudo apt-get install -y nvidia-driver

# Reboot prompt
echo "NVIDIA drivers installed/updated. A reboot may be required."
