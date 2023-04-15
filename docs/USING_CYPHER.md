## Usando o cypher

For use cypher with desired user configurations for `username_at_your_choise` and database `password_at_your_choise`. Just enter in folder `./server/cypher/data` and edit files bellow:

- gms.cfg;
- lgs.cfg;
- zs.cfg;

All fields finished with `_ID` can be replaced with a new user database name and all fields finished with `_PW` can be replaced with a new password.

When you have done all changes that you want. Execute commands bellow:

run: `cd ./server/cypher/`

run: `./cypher`

If program don't execute, run: `sudo chmod +x ./cypher`. After run `./cypher` again. 

Is this momment select option 1 and press enter. After select option 1 again and press enter. The file will be generated inside folder `./server/data` identified by name: cfg_[created year][created month][created day][created hour][created minute][created seconds]

Exemple in folder: cfg_20181123103856. 

Inside folder created by cypher you can found the `key` and folder `enconde`. Enter inside folder `encode` and copy `gms_db.enc` for example. Go to the folder `gms` inside `./server` and paste (replace) the file here. Repeat the process for `lgs` and `zs1`.

The `key` file have to be copied and pasted to all folders lgs, gms and zs1.

Done that, all parts of server will be run with desired database configurations.

run: `chmod -R 777 ./data`

PS: The last line will free permission of read and write for all users.