import pindb
import accdb 

def menu():
    try:
        accdb.acctable()
    except:
        pass

    while True:
        print('*Register new account  : 1')
        print('*Log in to your acount : 2')
        sieve = input('=> ')

        if sieve == str(0):
            accdb.manageAccount()

        if sieve == str(1):
            print('*Create your account')

            username = input(' *User name : ')
            username = accdb.makeAccountname(username)

            while True:
                address = input(' *Email address : ')
                if accdb.decMail(address):
                    if address == input(' *Repeat email address : '):
                        break
                    else:
                        print(' --The emails do not match')                
                else:
                    print(' --Please fill in your email address ')

            pincode = input(' *Password : ')
            while not pincode == input(' *Repeat password : '):
                print(' --The passwords do not match')
                pincode = input(' *Password : ')

            if accdb.register(username, address, pincode):
                print(' --Registration Complete')
                return username
            else:
                print(' --Registration fail')
                
        elif sieve == str(2):
            print('*Log in')

            value = input(' *Email address or username: ')
            while True:
                data = accdb.checkinfo(value)
                if not data == None:
                    break
                print(' --This is not registared')
                value = input(' *Email address or username: ')
            
            pincode = input(' *Password : ')
            while not accdb.checkPin(pincode, data):
                print(' --This password is incorrect')
                pincode = input(' *Password : ')
            return data[0][0]

        else:
            print('--Choose your choice')

def userpage(username):
    try:
        pindb.pintable()
    except:
        pass
    print('>Hello, {} !'.format(username))

    while True:
        print(' >Registar new app  : 1')
        print(' >Display your apps : 2')
        print(' >Log out           : 3')
        sieve = input('=> ')

        if sieve == str(1):
            print('  >Add new app')
            while True:
                appname = input('  >App name : ')
                while True:
                    conf = input("  >Is {} correct ? ('yes' or 'no') : ".format(appname)).lower()
                    if conf in ['y', 'ye', 'yes', 'n', 'no']:
                        break
                if conf in ['y', 'ye', 'yes']:
                    break
            
            while True:
                print('   >Generate complex password : 1')
                print('   >Make password by yourself : 2')
                sieve = input('=> ')

                if sieve == str(1):
                    password = pindb.genPass()
                    break
                elif sieve == str(2):
                    password = input('    >password :')
                    while not password == input('    >Repeat password :'):
                        print('  --The passwords do not match')
                        password = input('  >Password : ')
                    break

            if pindb.addapp(appname, username, password):
                print('   --Registration Complete')
            else:
                print('   --Registration fail')

        elif sieve == str(2):
            if not pindb.displayApps(username):
                print('  --error')

        elif sieve == str(3):
            return True

        else:
            print('\n')

if __name__ == '__main__':
    userpage(menu())
