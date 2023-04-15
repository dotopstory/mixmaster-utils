1. we need to run step cypher. Can be found <a href="https://github.com/mathmpr/mixmaster-utils/blob/master/docs/USING_CYPHER.md" target="_blank">here</a>
2. inside folders lgs, gms and zs1 you have files .cfg. Open these files and replace all IPS with virtual machine IP. Virtual machine IP can be found running `ifconfig` in terminal
3. if cypher, LoginServer, GameManagerServer or ZoneServer won't works, maybe your system have a miss configured shared libary. Original game server run in older CentOS version. You need to copy some files to `/usr/lib/` and `/lib/`.
    1. download in virtual machine files for `/lib/` <a href="https://drive.google.com/file/d/1PDKGY4eVyb7kOomRW7GbjCzsm9yMvXRe/view?usp=share_link" target="_blank">here</a>
    2. download in virtual machine files for `/usr/lib/` <a href="https://drive.google.com/file/d/1vlu5y4Hu_MpxT3t_AY8fw7SUw8mB2f_U/view?usp=sharing" target="_blank">here</a>
    3. now open a sudo nautilus execute in terminal: `sudo nautilus`
    4. extract these two files to correct locations
    5. finnaly you need to create a symb link to lib with this command `sudo ln -s /lib/i386-linux-gnu/ld-2.27.so /lib/ld-linux.so.2`
4. Run sudo chmod +x for `~/home/server/lgs/LoginServer`, `~/home/server/gms/GameManagerServer` and finaly `~/home/server/zs1/ZoneServer`.
5. Now you can open three terminals and run in this order. I thought that all of these three server show message `START` when it ran with success:
    1. `./server/lgs/LoginServer`
    2. `./server/gms/GameManagerServer`. If fails, just run again.
    3. `./server/zs1/ZoneServer`. If fails, just run again.