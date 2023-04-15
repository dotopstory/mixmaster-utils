- Run in a new terminal

1. sudo apt-get install openssh-server
2. sudo systemctl enable ssh --now
3. if you are using Windows OS as host, you can download Bitvise SSH Client <a href="https://www.bitvise.com/ssh-client-download">here</a>
    1. open Bitvise after install.
    2. run `ifconfig` inside a terminal in Virtual Machine. Find an ip begin with `192.168`, copy it and past into field `Host` in Bitvise
    3. the standart port is `22`
    4. in `Authentication` area of Bitvise, in field `Username` put the same username of Linux Virtual Machine
    5. in field `Initial method` choose `password`
    6. check the box `Store encrypted password in profile`
    7. and finaly add the same password of the Linux Virtual Machine at the field `Password`

Now you can use command from Host to Virtual Machine.