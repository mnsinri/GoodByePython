from inorilib import Minase
import sys

path = sys.argv[1]
list = []

with open(path, mode='r') as f :
    line = f.readline()
    while line :
        try :
            line = int(line.strip())
            list.append(line)
        except :
            pass
        line = f.readline()

list.sort()
print(' '.join(map(str, list)))
