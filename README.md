# Helen
A home server and Calendar app

Step 1 - Install an image
  - Goto raspberrypi.com/software/
  - Download and install Pi imager
  - Follow steps to create a image SD
    - use Raspberry PI OS Lite 64bit
    - enable ssh
    - setup wifi
    - set host name
    - set user and password
  
Step 2 - Update and install git
  - run: sudo apt update -y
  - run: sudo apt upgrade -y
  - run: sudo apt-get install git -y
  - run: git clone https://github.com/LeeKizer/Helen.git
  - run: cd Helen
  - run: chmod +x helen_setup.sh
  - run: ./helen_setup.sh


run update file

How to Use:

1. Save the script to a file (e.g., update_raspberry_pi.sh).


2. Make it executable:

chmod +x update_raspberry_pi.sh

create dir called helen
mkdir helen

clone git repo
git clone {my repo adress}



3. Run the script:

./update_raspberry_pi.sh



This script ensures your Raspberry Pi stays updated while providing an option for firmware updates and rebooting.

