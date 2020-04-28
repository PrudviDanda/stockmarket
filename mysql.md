In order to use a password to connect to MySQL as root, you will need to switch its authentication method from auth_socket to mysql_native_password. To do this, open up the MySQL prompt from your terminal:

```sudo mysql```

Next, check which authentication method each of your MySQL user accounts use with the following command:

```sql
SELECT user,authentication_string,plugin,host FROM mysql.user;
```

```bash
Output

+------------------+-------------------------------------------+-----------------------+-----------+
| user             | authentication_string                     | plugin                | host      |
+------------------+-------------------------------------------+-----------------------+-----------+
| root             |                                           | auth_socket           | localhost |
| mysql.session    | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE | mysql_native_password | localhost |
| mysql.sys        | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE | mysql_native_password | localhost |
| debian-sys-maint | *CC744277A401A7D25BE1CA89AFF17BF607F876FF | mysql_native_password | localhost |
+------------------+-------------------------------------------+-----------------------+-----------+
4 rows in set (0.00 sec)
```
In this example, you can see that the root user does in fact authenticate using the auth_socket plugin. To configure the root account to authenticate with a password, run the following ALTER USER command. Be sure to change password to a strong password of your choosing, and note that this command will change the root password you set in Step 2:

```sql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
```

Then, run FLUSH PRIVILEGES which tells the server to reload the grant tables and put your new changes into effect:

```
FLUSH PRIVILEGES;
```

```
sudo mysql -- It does not ask me for any password

-- Then in MariaDB/MySQL console:
update mysql.user set plugin = 'mysql_native_password' where User='root';
FLUSH PRIVILEGES;
exit;
```