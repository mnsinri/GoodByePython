from onp import Onepass
from acc import Account
from time import sleep

def menu():
    while True:
        print('*Register new account  : 1')
        print('*Log in to your acount : 2')
        sieve = input('=> ')
        sleep(1)

        if sieve == str(1):
            print('*Create your account')

            username = input(' *User name : ')
            sleep(1)

            p_address = input(' *Email address : ')
            q_address = input(' *Repeat email address : ')
            while not p_address == q_address:
                sleep(1)
                print(' --The emails do not match')
                p_address = input(' *Email address : ')
                q_address = input(' *Repeat email address : ')
            sleep(1)

            p_pincode = input(' *Password : ')
            q_pincode = input(' *Repeat password : ')
            while not p_pincode == q_pincode:
                sleep(1)
                print(' --The passwords do not match')
                p_pincode = input(' *Password : ')
                q_pincode = input(' *Repeat password : ')
            sleep(1)

            New_user = Account(username, p_address, p_pincode)
            sleep(1)
            if New_user.register():
                print(' --Registration Complete')
                sleep(1)
                return [New_user.num, New_user.name]
            else:
                print(' --Registration fail')
                
        elif sieve == str(2):
            print('*Log in')
            user = Account(None, None, None)

            address = input(' *Email address : ')
            while not user.checkAddr(address):
                sleep(1)
                print(' --This email address is not be registared')
                address = input(' *Email address : ')
            sleep(1)

            pincode = input(' *Password : ')
            while not user.checkPin(pincode):
                sleep(1)
                print(' --This password is incorrect')
                if user.count >= 3:
                    print(' --Back to the menu')
                    break
                pincode = input(' *Password : ')
            if user.count >= 3:
                pass
            else:
                sleep(1)
                return [user.num, user.name]
            sleep(1)
            
        else:
            print('--Choose your choice')
            sleep(1)

def userpage(userId):
    login = Onepass(userId[0], userId[1])
    top_data = login.fetchData()
    print('>Hello, {}!'.format(login.name))
    sleep(1)

    while True:
        print(' >Registar new app  : 1')
        print(' >Display your apps : 2')
        print(' >Log out           : 3')
        sieve = input('=> ')
        sleep(1)

        if sieve == str(1):
            print('  >Add new app')
            while True:
                login.app = input('  >App name : ')
                sleep(1)
                while True:
                    conf = input("  >Is {} correct ? ('yes' or 'no') : ".format(login.app))
                    if conf == 'yes' or conf == 'no':
                        break
                    else:
                        pass
                if conf == 'yes':
                    break
                else:
                    pass
            
            while True:
                print('   >Generate complex password : 1')
                print('   >Make password by yourself : 2')
                sieve = input('=> ')

                if sieve == str(1):
                    login.password = login.genPass()
                    break
                elif sieve == str(2):
                    login.password = input('    >password :')
                    password = input('    >Repeat password :')
                    while not login.password == password:
                        sleep(1)
                        print('  --The passwords do not match')
                        login.password = input('  >Password : ')
                        password = input('  >Repeat password : ')
                    break
                else:
                    sleep(1)
                    print('\n')

            try:
                top_data = login.addapp(top_data)
                print('   --Registration Complete')
            except:
                print('   --Registration fail')
            sleep(1)

        elif sieve == str(2):
            if login.displayApps(top_data):
                pass
            else:
                print('  --error')
        elif sieve == str(3):
            return 1
        else:
            sleep(1)
            print('\n')

if __name__ == '__main__':
    main = userpage(menu())
    