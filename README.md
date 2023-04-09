## Up server

### Requirements

- Linux x64

#### Inside the Linux system

- Install MySQL

1. sudo apt update
2. sudo apt install mysql-server
3. sudo systemctl start mysql.service
4. sudo mysql_secure_installation
    1. Choose: Y
    2. Type: 2
    3. Enter password and type it again (reenter password)
    4. Choose: Y. And if program enter in loop and ask for password again after choose Y, put the same password again and when ask for "Do you wish to continue with the password provided?(Press y|Y for Yes, any other key for No)" again, press CTRL + C
5. mysql -u root -p
    1. Type the password typed in step #4
6. run in MySQL console: ALTER USER 'root'@'localhost' IDENTIFIED WITH auth_socket;
7. run in MySQL console: CREATE USER 'root'@'%' IDENTIFIED WITH auth_socket BY '< password typed in step 4 >'

- Copy files from folder `/server-files` of root of this project to folder `~/server` (home directory of current logged user)
- Now enter in `~/server/sql/` folder and run all commands bellow:

1. mysql -u root -p < create_databases.sql
2. mysql -u root -p -f gamedata < gamedata.sql
3. mysql -u root -p -f LogDB < LogDB.sql
4. mysql -u root -p -f Member < Member.sql
5. mysql -u root -p -f S_Data < S_Data.sql
6. mysql -u root -p -f Web_Account < Web_Account.sql

- 