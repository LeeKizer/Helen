# Helen
# Installation 
## Install and Update debian
### Create USB boot drive
Click [here](https://www.debian.org/distrib/netinst) to go to the debian iso pape.
Use AMD64
Helpful page: [Debian install](https://wiki.debian.org/DebianInstall)

### Setup install settings file
[Preseed file help](https://debian-handbook.info/browse/stable/sect.automated-installation.html#sect.fai)

### Update
```
sudo apt update && sudo apt upgrade
```


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
  - run:sudo apt update -y
  - run: sudo apt upgrade -y
  - run: sudo apt-get install git -y
  - run: git clone https://github.com/LeeKizer/Helen.git
  - run: cd Helen
  - run: chmod +x helen_setup.sh
  - run: ./helen_setup.sh
```python
import os
if foo then fuo:
  test = 1
```




