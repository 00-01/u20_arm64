##from local
### remote to local
    scp your_username@ip:/target/directory/{a,b,c\} ~/local/location
### local to remote
    scp foo.txt bar.txt your_username@remotehost.edu:~
    scp {foo,bar}.txt your_username@remotehost.edu:~
    scp *.txt your_username@remotehost.edu:~
### remote to remote
    scp your_username@remote1.edu:/some/remote/directory/foobar.txt your_username@remote2.edu:/some/remote/directory/
