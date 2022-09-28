import math
a = int(input('a= '))
b = int(input('b= '))
c = int(input('c= '))
def triunghi(m,n,f):
    if m<n+f and n<m+f and f<m+n:
        ma=0,5*math.sqrt(2*n**2+2*c**2-a**2)
        return print('Mediana =', ma)
    else:
        print('Acestea marimi nu pot fi laturile triughiului')    
print(triunghi(a, b, c))