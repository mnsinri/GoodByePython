import sqlite3
import random
acc_path = 'cus_data/accData.db'

def acctable():
    conn = sqlite3.connect(acc_path)
    c = conn.cursor()

    sql = "CREATE TABLE IF NOT EXISTS acc_data(name TEXT, address TEXT, pin TEXT)"
    c.execute(sql)

    conn.commit()
    conn.close()

def makeAccountname(name):
    conn = sqlite3.connect(acc_path)
    c = conn.cursor()

    while True:
        serial_num = random.randrange(1, 10000)
        acc_name = name + '#' + str(serial_num).zfill(4)

        try:
            sql = "SELECT * FROM acc_data WHERE name = '?'"
            c.execute(sql, (acc_name,))
            val = c.fetchall()

            if val == []:
                break
        except:
            break
    
    conn.commit()
    conn.close()

    return acc_name

def register(username, emailaddress, pincode):
    conn = sqlite3.connect(acc_path)
    c = conn.cursor()

    empt_data = "INSERT INTO acc_data VALUES(?,?,?)"
    try:
        c.execute(empt_data, (username, emailaddress, pincode))

        conn.commit()
        conn.close()
        return True
    except:
        return False

def decMail(address):
    if address.count('@') == 1:
        if address.split('@')[1].count('.') >= 1:
            return True
    return False

def checkinfo(val):
    conn = sqlite3.connect(acc_path)
    c = conn.cursor()

    if decMail(val) == True:
        addr = "SELECT * FROM acc_data WHERE address = ?"
        c.execute(addr, (val,))
        result = c.fetchall()
    else:
        name = "SELECT * FROM acc_data WHERE name = ?"
        c.execute(name, (val,))
        result = c.fetchall()
    
    conn.commit()
    conn.close()

    if result == []:
        return None
    else:
        return result

def checkPin(pincode, data):
    if pincode == data[0][2]:
        return True
    else:
        return False

def manageAccount():
    conn = sqlite3.connect(acc_path)
    c = conn.cursor()

    print('\n---Acoount Data---')
    sql = "SELECT * FROM acc_data"
    for row in c.execute(sql):
        print(row)
    print('------------------\n')
