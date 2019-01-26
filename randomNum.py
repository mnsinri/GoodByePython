from inorilib import Minase
import random

f = Minase()
name = input('textname :')
while 0 < name.count('.') : 
    print('no dot in textname')
    name = input('textname：')
name = 'sample_text/' + name + '.txt'
#pre-compute path

n = None
while not isinstance(n, int) :
    try :
        n = input('How many factors do you want ? :')
        n = int(n)
    except :
        print('As you know, put a positive integer.')

if f.integerfile(name, n) == False :
    print('unable to write to the file')
