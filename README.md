## Up server

### Requirements

- VMWare, Virtual Box or similar
- Linux x32 Debian Based (for use like virtual machine)
- MySQL client in host (workbench, navicat, dbeaver)
- Bitvise (if use windows) or similar SSH client tool

#### Inside the Linux system (or amost)

- Install MySQL

1. sudo apt update
2. sudo apt install mysql-server
3. sudo systemctl start mysql
	1. If during first install, ask for a root password, just type a password and finish instalation.
4. sudo mysql_secure_installation
    1. Choose `N` for `VALIDATE PASSWORD PLUGIN`;
    2. If ask for root password, choose the same password typed in step 3;
    3. Choose: Y for `Remove anonymous users?`
    4. Choose: Y for `Disallow root login remotely?`
    5. Choose: Y for `Remove test database and access to it?`
    6. Choose: Y for `Reload privilege tables now?`
5. sudo mysql -u root -p
    1. Type the password typed in step 3.1 or 4.2
	2. run: CREATE USER '`username_at_your_choise`'@'%' IDENTIFIED BY '`password_at_your_choise`';
	3. run: GRANT ALL PRIVILEGES ON *.* TO '`username_used_in_last_command`'@'%';
	4. run: exit; for exist MySQL console.
6. sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
7. with down and up arrows find line `bind-address` and replace `127.0.0.1` by `0.0.0.0`
8. press `CTRL + O` to save and write file, and press enter for save in same path with same name.
9. press `CTRL + X` for quit nano.
10. sudo systemctl restart mysql
11. run: `ifconfig` and try find an IP begin with `192.168` this is the ip of virtual machine, copy this ip and go to host machine (windows)
12. open your prefered MySQL client (workbench, navicat, dbeaver) and try to connect using:
	1. host as copied ip
	2. username as `username_at_your_choise` typed in step 5.2
	3. password as `password_at_your_choise` typed in step 5.2
13. try to connect
14. now back to virtual machine
15. copy files from folder `/server-files` of root of this project to folder `~/server` (home directory of current logged user)
16. now enter in `~/server/database/` folder and run all commands bellow:
	1. mysql -u `username_at_your_choise` -p < create_databases.sql
	2. mysql -u `username_at_your_choise` -p -f gamedata < gamedata.sql
	3. mysql -u `username_at_your_choise` -p -f LogDB < LogDB.sql
	4. mysql -u `username_at_your_choise` -p -f Member < Member.sql
	5. mysql -u `username_at_your_choise` -p -f S_Data < S_Data.sql
	6. mysql -u `username_at_your_choise` -p -f Web_Account < Web_Account.sql

- Configure LGS, GMS and ZS1

1. we need to run step cypher. Can be found <a href="https://github.com/mathmpr/mixmaster-utils/blob/master/docs/USING_CYPHER.md" target="_blank">here</a>
2. inside folders lgs, gms and zs1 you have files .cfg. Open these files and replace all IPS with virtual machine IP. Virtual machine IP can be found running `ifconfig` in terminal
3. if cypher, LoginServer, GameManagerServer or ZoneServer won't works, maybe your system have a miss configured shared libary. Original game server run in older CentOS version. You need to copy some files to `/usr/lib/` and `/lib/`.
	1. download in virtual machine files for `/lib/` <a href="https://drive.google.com/file/d/1PDKGY4eVyb7kOomRW7GbjCzsm9yMvXRe/view?usp=share_link" target="_blank">here</a>
	2. download in virtual machine files for `/usr/lib/` <a href="https://drive.google.com/file/d/1vlu5y4Hu_MpxT3t_AY8fw7SUw8mB2f_U/view?usp=sharing" target="_blank">here</a>
	3. now open a sudo nautilus execute in terminal: `sudo nautilus`
	4. extract these two files to correct locations
	5. finnaly you need to create a symb link to lib with this command `sudo ln -s /lib/i386-linux-gnu/ld-2.27.so /lib/ld-linux.so.2`