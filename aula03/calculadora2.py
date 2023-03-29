from math import sqrt

a=float(input('Digite um número: '))
c=input('Escolha uma operação: ') 
c=c.lower

if c=="raiz":
    print(sqrt(a))
    quit()
    
elif c=="ao quadrado":
    print(a**2)
    quit()

elif c=="1/":
    print(1/a)
    quit()
    
b=float(input('Digite outro número: ')) 

if c=="*":
    print(a*b)

elif c=="/":
    print(a/b)

elif c=="+":
    print(a+b)

elif c=="-":
    print(a-b)

elif c=="**":
    print(a**b)
