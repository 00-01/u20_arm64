## - display resolution
### open
    sudo nano /boot/firmware/usercfg.txt
### add
    disable_overscan=1

## - bluetooth
    sudo apt install pi-bluetooth
    
## - ssh
    sudo systemctl enable ssh
    sudo systemctl start ssh

## - software-center
    sudo apt install ubuntu-software
    sudo apt install gnome-software
    
## - csi camera
    sudo nano /boot/firmware/config.txt
### add these lines:
    gpu_mem=512
    disable_camera_led=1
    start_file=start4x.elf
    fixup_file=fixup4x.dat

## reboot
    sudo reboot
