## Up server

### Requirements

- VMWare, Virtual Box or similar
- Linux x32 Debian Based (for use like virtual machine)
- MySQL client in host (workbench, navicat, dbeaver)
- Bitvise (if you use Windows) or similar SSH client tool

#### Inside the Linux system (or amost)

- Install MySQL and configure databases. Check how to do <a href="https://github.com/mathmpr/mixmaster-utils/blob/master/docs/INSTALL_MYSQL.md" target="_blank">here</a>

- Configure LGS, GMS and ZS1. Check how to do <a href="https://github.com/mathmpr/mixmaster-utils/blob/master/docs/CONFIGURE_SERVER.md" target="_blank">here</a>

- Installing SSH Server. Check how to do <a href="https://github.com/mathmpr/mixmaster-utils/blob/master/docs/INSTALL_SSH_SERVER.md" target="_blank">here</a>

Inside of folder `./server/clean/others/` have the server base from old MixMaster Up and MixMaster Titan. If you can have a great compatibility between server and client. Try to do steps above with Titan base and after try to run Titan client game.

After these steps you can download the game client from <a href="https://drive.google.com/file/d/1WXBPOR4aGOowS9ovS3svqPCiJB-3Y99c/view?usp=share_link">MixMaster Up</a> or <a href="https://drive.google.com/file/d/1Nn5gq11tA4nyxKXPFtuz5JE0mLs3T8tl/view?usp=share_link">MixMaster Titan</a>. Another tools and clients can be found in <a href="https://drive.google.com/drive/folders/14fXEpWbZnHvGWq7sWhPfpNyJrmflxoL-">this Google Drive folder</a>.

To run client you need to decrypt `mixer.cnf` in root folder of client, and put the IP of Linux Virtual Machine. If you can't do that, you can create a `.bat` file to run game directly.

You need to create an account for make login in `mixer.exe` or directly via `.bat`. To do that, just run this MySQL query into mysql sonsole. In Linux Virtual Machine, run in terminal. mysql -u `username_at_your_choise` -p.

1. run `use Member;`
2. run `INSERT INTO Player(PlayerID, Passwd, Email) VALUES ("username_for_login_in_game", PASSWORD("password_for_login_in_game"), "matheusprador@gmail.com");`
3. if the las command fails saing that passwr is so much long, run: `alter table Player
   modify Passwd varchar(45) default '' not null;` and try the command in step 2 again.

The bat content is any like: `start MixMaster.exe 3.85500 ip_of_vistual_machine_begin_with_192.168 22005 0 username_for_login_in_game password_for_login_in_game 1 AURORA_BR exit`