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

## reboot
    sudo reboot
