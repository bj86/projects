import pickle

def menu():
    data = pickle.load(open('test.pickle', 'rb'))
    print("""
    1. read
    2. add
    3. remove""")
    answer = int(input(''))
    if answer == 1:
        return read(data)
    elif answer == 2:
        return add(data)
    elif answer == 3:
        return remove(data)
    else:
        return print('Not a valid option!'), menu()

def load():
    return data, menu()

def read(data):
    name = str(input('name: '))
    print(('number:'), (data[name]))
    return menu()

def add(data):
    name = str(input('name: '))
    number = int(input('number: '))
    data[str(name)] = number
    pickle.dump(data, open('test.pickle', 'wb'))
    return menu()

def remove(data):
    name = str(input('name: '))
    del data[name]
    pickle.dump(data, open('test.pickle', 'wb'))
    return menu()

menu()
