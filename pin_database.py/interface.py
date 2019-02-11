import accdb
import pindb

class Login:
    def loginmenu(self):
        print('*Register new account  : 1')
        print('*Log in to your acount : 2')
        return input('=> ')

    def entername(self):
        username = input(' *User name : ')
        self.name = accdb.makeAccountname(username)

    def enteraddr(self):
        while True:
            self.address = input(' *Email address : ')
            if accdb.decMail(self.address):
                if self.address == input(' *Repeat email address : '):
                    break
                else:
                    print(' --The emails do not match')                
            else:
                print(' --Please fill in your email address ')

    def enterpin(self):
        self.pincode = input(' *Password : ')
        while not self.pincode == input(' *Repeat password : '):
            print(' --The passwords do not match')
            self.pincode = input(' *Password : ')

    def registarNewUser(self):
        self.entername()
        self.enteraddr()
        self.enterpin()
        if accdb.register(self.name, self.address, self.pincode):
            print(' --Registration Complete')
        else:
            print(' --Registration fail')

    def comparePersonalData(self):
        value = input(' *Email address or username: ')
        while True:
            self.data = accdb.checkinfo(value)
            if not self.data == None:
                break
            print(' --This is not registared')
            value = input(' *Email address or username: ')
    
    def comparePin(self):
        pincode = input(' *Password : ')
        while not accdb.checkPin(pincode, self.data):
            print(' --This password is incorrect')
            pincode = input(' *Password : ')
        self.name = self.data[0][0]

class Mypage:
    def __init__(self, username):
        self.name = username

    def usermenu(self):
        print(' >Registar new app  : 1')
        print(' >Display your apps : 2')
        print(' >Log out           : 3')
        return input('=> ')
    
    def getAppsname(self):
        print('  >Add new app')
        while True:
            self.app = input('  >App name : ')
            while True:
                conf = input("  >Is {} correct ? ('yes' or 'no') : ".format(self.app)).lower()
                if conf in ['y', 'ye', 'yes', 'n', 'no']:
                    break
            if conf in ['y', 'ye', 'yes']:
                break
    
    def setPin(self):
        while True:
            print('   >Generate complex password : 1')
            print('   >Make password by yourself : 2')
            sieve = input('=> ')

            if sieve == str(1):
                self.pin = pindb.genPass()
                break
            elif sieve == str(2):
                self.pin = input('    >password :')
                while not self.pin == input('    >Repeat password :'):
                    print('  --The passwords do not match')
                    self.pin = input('  >Password : ')
                break

    def addApps(self):
        if pindb.addapp(self.app, self.name, self.pin):
            print('   --Registration Complete')
        else:
            print('   --Registration fail')
