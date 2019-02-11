import accdb
import pindb
import interface 

def menu():
    accdb.acctable()
    login = interface.Login()

    while True:
        sieve = login.loginmenu()

        if sieve.lower() == 'inoriminase': #admin command
            accdb.manageAccount()

        elif sieve == str(1): #registar new user
            print('*Create your account')

            login.registarNewUser()
            return login.name

        elif sieve == str(2): #login own account
            print('*Log in')
            
            login.comparePersonalData()
            login.comparePin()
            return login.name

        else:
            print('--Choose your choice\n')

def userpage(username):
    pindb.pintable()
    conn = interface.Mypage(username)
    print('\n>Hello, {} !'.format(conn.name))

    while True:
        sieve = conn.usermenu()

        if sieve == str(1): #add new appname and app'pin
            conn.getAppsname()
            conn.setPin()
            conn.addApps()

        elif sieve == str(2): #desplay own appname and app'pin
            if not pindb.displayApps(username):
                print('  --error')

        elif sieve == str(3): #log out
            return True

        else:
            pass

if __name__ == '__main__':
    userpage(menu())
