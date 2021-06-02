### open:
    sudo nano /etc/ssh/sshd_config
### chage: (#PasswordAuthentication yes) -> (PasswordAuthentication no)
    service sshd restart
