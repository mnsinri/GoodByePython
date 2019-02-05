import sqlite3
import random
acc_path = 'cus_data/accData.db'

def pintable():
    conn = sqlite3.connect(acc_path)
    c = conn.cursor()

    sql = 'CREATE TABLE pin_data(apps TEXT, name TEXT, pin TEXT)'
    c.execute(sql)

    conn.commit()
    conn.close()

def addapp(apps, name, pin):
    conn = sqlite3.connect(acc_path)
    c = conn.cursor()

    empt_data = "INSERT INTO pin_data VALUES (?,?,?)"
    try:
        c.execute(empt_data, (apps, name, pin))

        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(e)
        return False

def char_list() :
    char = ''
    char_list = [[97, 123], [65, 91], [48, 58]]
    for i in range(len(char_list)) :
        for j in range(char_list[i][0], char_list[i][1]) :
            char += chr(j)
    return char

def genPass() :
    chlist = char_list()
    password = ''.join([random.choice(chlist) for i in range(24)])
    return password

def displayApps(name):
    conn = sqlite3.connect(acc_path)
    c = conn.cursor()

    username = "SELECT * FROM pin_data WHERE name = ?"
    c.execute(username, (name,))
    result = c.fetchall()

    if not result == []:
        print('*')
        for pin in result:
            print('|App : {0}\n|pin : {1}\n*'.format(pin[0], pin[2]))
        return True
    else:
        return False
