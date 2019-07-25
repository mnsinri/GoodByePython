#hello >>>>>inori<<<<<
#You should put only 2nd commandline-arg "inori".

from sys import argv

print('hello, {}'.format(argv[1] if len(argv) == 2 else "inori"))
