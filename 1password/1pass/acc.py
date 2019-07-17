class Account:
    Dpath = 'customerData/accountData.txt'
    Apath = 'customerData/accountPass/'
    serial = 'customerData/serialNum.txt'

    def __init__(self, username, email_address, pincode):
        self.name = username
        self.address = email_address
        self.pin = pincode
        self.count = 0
        self.num = None

    def register(self):
        try:
            with open(self.serial, mode='r') as f:
                num = f.read()
            try:
                self.num = int(num) + 1
            except:
                self.num = 0
            with open(self.serial, mode='w') as f:
                f.write(str(self.num))

            with open(self.Dpath, mode='a') as f:
                f.write('{0};{1};{2};{3}\n'.format(self.num, self.name, self.address, self.pin))

            user_pass = self.Apath + 'number' + str(self.num) + '.txt'
            with open(user_pass, 'w') as f:
                pass
            return True
        except:
            return False

    def checkAddr(self, email_address):
        with open(self.Dpath, mode='r') as f:
            for line in f:
                data = line.strip().split(';')
                if data[2] == email_address:
                    self.num = data[0]
                    self.name = data[1]
                    self.address = data[2]
                    self.pin = data[3]
                    return True
            return False

    def checkPin(self, pincode):
        self.count += 1
        if self.pin == pincode:
            self.count = 0
            return True
        else:
            return False
