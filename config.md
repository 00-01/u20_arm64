## - display resolution
### open:
    sudo nano /boot/firmware/usercfg.txt
### add:
    disable_overscan=1
    
    cvt 1920 1080
    xrandr --newmode "1920x1080_60.00"  173.00  1920 2048 2248 2576  1080 1083 1088 1120 -hsync +vsync
    xrandr --addmode default 1920x1080_60.00
    
## to add perminently, create the file
    ~/.xprofile
### add
    #!/bin/sh
    xrandr --newmode "1920x1080_60.00"  173.00  1920 2048 2248 2576  1080 1083 1088 1120 -hsync +vsync
    xrandr --addmode default 1920x1080_60.00

    

## - bluetooth
    sudo apt install pi-bluetooth
    
## - ssh
    sudo systemctl enable ssh
    sudo systemctl start ssh

## - software-center
    sudo apt install ubuntu-software
    sudo apt install gnome-software
    
## - csi camera
### open:
    sudo nano /boot/firmware/config.txt
### add:
    gpu_mem=512
    disable_camera_led=1
    start_file=start4x.elf
    fixup_file=fixup4x.dat

## reboot
    sudo reboot
