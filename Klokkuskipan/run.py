from config import *


# This is for making the user table. Only run this once!
def SQL_Table():
    c.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER, name TEXT, position INTEGER, signIn REAL, signOut REAL)')
    c.execute('CREATE TABLE IF NOT EXISTS shifts(id INTEGER, name TEXT, signIn REAL, signOut REAL, date REAL)')
    return True

# Returns a timestamp when called.
def Get_Time():
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    return timestamp

# Verifies that the user id is in the database.
def Verify():
    print('\nKlokkuskipan 1.0\n')
    input_id = input('>> ID: ')
    c.execute(select_users_verify, (input_id,))
    data = str(c.fetchall())
    try:
        int(input_id)
    except ValueError:
        print('ValueError: id has to be integers')
    if input_id in data:
        answer = int(input(
        """>> Choose an option:

        1. Sign In
        2. Sign Out
        9. Administration
        0. Exit \n>> """))

        if answer == 1:
            return Clock_In(int(input_id))
        elif answer == 2:
            return Clock_Out(int(input_id))
        elif answer == 9:
            return Create_User()
        elif answer == 0:
            return exit()
        else:
            print('Not a valid option')
            return Verify()
    else:
        print('User not in database')
        return Verify()

# Self explanatory
def Create_User():
    print('\nRegister new employee\n')
    input_id = input('>> ID: ')
    input_name = input('>> Name: ')
    try:
        (int(input_id) and str(input_name))
        c.execute(insert_users_create, (input_id, input_name))
        conn.commit()
        print('>> User %s has been created, with ID: %s' % (input_name, input_id))
        input('\nPress enter to continue...')
        clear()
    except ValueError:
            print('ValueError')
    return Verify()

# Makes the first timestamp in the database.
def Clock_In(input_id):
    print('Please submit your work position')
    input_position = input('>> Position: ')
    try:
        int(input_position)
        c.execute(select_users_name, (input_id,))
        data_name = str(c.fetchall()).strip("[]()'',,")
        c.execute(update_signin_id, (Get_Time(), input_position, input_id))
        conn.commit()
        print('%s ID: %s signed in at %s' % (data_name, input_id, Get_Time()))
        time.sleep(3.5)
        clear()
    except ValueError:
        print('Position has to be a number. Try again!')
    return Verify()

# Makes the second and final timestamp.
def Clock_Out(input_id):
    c.execute(select_users_in, (input_id,))
    data_in = str(c.fetchall()).strip("[]()'',,")
    conn.commit()
    c.execute(update_signout_id, (Get_Time(), input_id))
    c.execute(select_users_name, (input_id,))
    data_name = str(c.fetchall()).strip("[]()'',,")
    conn.commit()
    print('%s ID: %s signed in at %s and signed out at %s' % (data_name, input_id, data_in, Get_Time()))
    time.sleep(3.5)
    clear()
    return Verify()

Verify()
