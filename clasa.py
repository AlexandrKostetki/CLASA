

import math
a = int(input('a= '))
b = int(input('b= '))
c = int(input('c= '))
d = int(input('d= '))
#triunghiuri posibile: abc abd bcd acd
def perAria(x,y,z):
    P=x+y+z
    sp = P/2
    A = math.sqrt(sp*(sp-x)*(sp-y)*(sp-z))
    return print('Perimetru = ', P, 'Aria = ', A)
if ((a > 0) and (b > 0) and (c > 0) and (d > 0)):
    if ((a+b>c) and (b+c>a) and (a+c>b)):
        print('Date pentru triunghiul ABC')
        perAria(a,b,c)
    else:
        print('triunghiul ABC nu exista')
    if ((a+b>d) and (b+d>a) and (a+d>b)):
        print('Date pentru triunghiul ABD')
        perAria(a,b,d)
    else:
        print('triunghiul ABD nu exista')
    if ((c+b>d) and (b+d>c) and (c+d>b)):
        print('Date pentru triunghiul BCD')
        perAria(b,c,d)
    else:
        print('triunghiul bcd nu exista')
    if ((c+a>d) and (a+d>c) and (c+d>a)):
        print('Date pentru triunghiul ACD')
        perAria(a,c,d)
    else:
        print('triunghiul ACD nu exista')
else:
    print('nu sunt numere naturale')


