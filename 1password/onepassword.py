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
                print(' **The emails do not match')
                p_address = input(' *Email address : ')
                q_address = input(' *Repeat email address : ')
            sleep(1)

            p_pincode = input(' *Password : ')
            q_pincode = input(' *Repeat password : ')
            while not p_pincode == q_pincode:
                sleep(1)
                print(' **The passwords do not match')
                p_address = input(' *Password : ')
                q_address = input(' *Repeat password : ')
            sleep(1)

            New_user = Account(username, p_address, p_pincode)
            sleep(1)
            if New_user.register():
                return New_user.num
            else:
                pass


        elif sieve == str(2):
            print('*Log in')
            user = Account(None, None, None)

            address = input(' *Email address : ')
            while not user.checkAddr(address):
                sleep(1)
                print(' **This email address is not be registared')
                address = input(' *Email address : ')
            sleep(1)

            pincode = input(' *Password : ')
            while not user.checkPin(pincode):
                sleep(1)
                print(' **This password is incorrect')
                if user.count >= 3:
                    print(' **Back to the menu')
                    break
                pincode = input(' *Password : ')
            if user.count >= 3:
                pass
            else:
                return int(user.num)
            sleep(1)
            
        else:
            print('**Choose your choice')
            sleep(1)

def userpage():
    pass

menu()