import random

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
            return False
