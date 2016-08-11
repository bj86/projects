from config import *



# This is for making the user table. Only run this once!
def SQL_Table():
    c.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER, name TEXT, position INTEGER, signIn REAL, signOut REAL)')
    return True

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
            return Verify()
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
    if input_id == int and input_name == str:
        c.execute(insert_users_create, (input_id, input_name))
        conn.commit()
        print('>> User %s has been created, with ID: %s' % (input_name, input_id))
        input('\nPress enter to continue...')
        clear()
    else:
        print('\nValueError \nExample:\n>> Name: John Smith\n>> ID: 5555 ')
        input('\nPress enter to continue...')
    return Verify()

# Makes the first timestamp in the database.
def Clock_In(input_id):
    print('Please submit your work position')
    input_position = input('>> Position: ')
    c.execute(select_users_name, (input_id,))
    data = str(c.fetchall()).strip("[]()'',,")
    c.execute(select_users_out,(time_in, input_position, input_id))
    conn.commit()
    print('%s ID: %s signed in at %s' % (data, input_id, time_in))
    time.sleep(3.5)
    clear()
    return Verify()

# Makes the second and final timestamp.
def Clock_Out(input_id):
    c.execute(select_users_in, (input_id,))
    data_in = str(c.fetchall()).strip("[]()'',,")
    c.execute(update_signout_id, (time_out, input_id))
    c.execute(select_users_name, (input_id,))
    data_name = str(c.fetchall()).strip("[]()'',,")
    conn.commit()
    print('%s ID: %s signed in at %s and signed out at %s' % (data_name, input_id, data_in, time_out))
    time.sleep(3.5)
    clear()
    return Verify()

Verify()