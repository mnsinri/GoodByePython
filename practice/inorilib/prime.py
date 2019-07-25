from inorilib import Minase


prime = Minase()
while True :
    try :
        n = input('It generates a list of prime number From 2 to n :')
        n = int(n)
        break
    except :
        print('Only integer is usable.')


n = prime.____(n)
print(n)
