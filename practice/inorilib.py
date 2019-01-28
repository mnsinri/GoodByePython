import random
import math
#import string

class Minase:
    def __init__(self) :
        print('おやすみなせ')
        #'おやすみなせ' is one of the magic word everyone come to be happy.

    def fibonacch(self) :
        f1 = f2 = 1
        while True :
            yield f1
            f1, f2 = f2, f1 + f2
    
    def pow_tail(self, n) :
        return pow(n, pow(n, n), 10)

    def integerfile(self, filename, n) :
        try :
            with open(filename, mode='w') as f :
                for i in range(n) :
                    f.write(str(random.randrange(1000)) + '\n')
            return True
        except :
            print('This file couldn\'t be opened.')
            return False

    def eratosthenes(self, n) :
        if not isinstance(n, int) :
            print('Only integer is usable.')
            return False
        if n < 2 :
            print('Please use natural number is more than two.')
            return False
        prime = []
        num = [i for i in range(2, n)]
        limit = math.sqrt(n)
        while True :
            p = num[0]
            if p >= limit :
                return prime + num
            prime.append(p)
            num = [i for i in num if not i % p == 0]

    def char_list(self) :
        char = ''
        char_list = [[97, 123], [65, 91], [48, 58]]
        for i in range(len(char_list)) :
            for j in range(char_list[i][0], char_list[i][1]) :
                char += chr(j)
        return char

    def makePassword(self, limit) :
        if not isinstance(limit, int) :
            try :
                limit = int(limit)
            except :
                print('Only integer is usable.')
                return False
        chlist = self.char_list()
        password = ''.join([random.choice(chlist) for i in range(limit)])
        return password
