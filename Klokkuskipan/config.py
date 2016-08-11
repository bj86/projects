import time
import datetime
import sqlite3
import os

# Timestamps
ts = time.time()

clear = lambda: os.system('cls')

# Temporary Database config and functions below
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Pulls id from users (Verify)
select_users_verify = "SELECT %s FROM %s WHERE %s = ?" % ('id', 'users', 'id')

# Inserts id and name into users (Create_Employee)
insert_users_create = "INSERT INTO users(id, name) VALUES (?, ?)"

# Selects signOut from users where id = input
select_users_in = "SELECT %s FROM %s WHERE %s = ?" % ('signIn', 'users', 'id')

# Selects signIn from users where id = input
update_signin_id = "UPDATE %s SET %s = ?, %s = ? WHERE %s = ?" % ('users', 'signIn', 'position', 'id')

# Selects name from users where id = input
select_users_name = "SELECT %s FROM %s WHERE %s = ?" % ('name', 'users', 'id')

# Updates signOut where id = input
update_signout_id= "UPDATE %s SET %s = ? WHERE %s = ?" % ('users', 'signOut', 'id')
