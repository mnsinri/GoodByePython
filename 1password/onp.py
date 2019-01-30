import random

class Onepass:
    def __init__(self, userId, username):
        self.path = 'customerData/accountPass/number' + str(userId) + '.txt'
        self.name = username
        self.app = None
        self.password = None

    def fetchData(self):
        try:
            apps = []
            passwords = []
            with open(self.path, mode='r') as f:
                for line in f:
                    data = line.strip().split(';')
                    apps.append(data[0])
                    passwords.append(data[1])
                return [apps, passwords]
        except:
            return [[], []]

    def addapp(self, data):
        data[0].append(self.app)
        data[1].append(self.password)
        with open(self.path, mode='a') as f:
            f.write('{};{}\n'.format(self.app, self.password))
            return data

    def char_list(self) :
        char = ''
        char_list = [[97, 123], [65, 91], [48, 58]]
        for i in range(len(char_list)) :
            for j in range(char_list[i][0], char_list[i][1]) :
                char += chr(j)
        return char

    def genPass(self) :
        chlist = self.char_list()
        password = ''.join([random.choice(chlist) for i in range(24)])
        return password

    def displayApps(self, data):
        try:
            print('*')
            for i in range(len(data[0])):
                print('|App : {0}\n|pin : {1}\n*'.format(data[0][i], data[1][i]))
            return True
        except:
            return False
