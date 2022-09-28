import math
a = int(input('a= '))
b = int(input('b= '))
c = int(input('c= '))
def triunghi(m,n,f):
    if m<n+f and n<m+f and f<m+n:
        semisuma = (m+n+f)/2
        Aria = math.sqrt(semisuma*(semisuma-m)*(semisuma-n)*(semisuma-f))
        ha=(2*Aria)/(m)
        return print('Inaltimea este', ha )
    else:
        print('Acestea marimi nu pot fi laturile triughiului')    
print(triunghi(a, b, c))