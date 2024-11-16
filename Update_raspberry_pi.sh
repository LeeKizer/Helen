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
