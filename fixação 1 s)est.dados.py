a,b,c=[],[],[]
cont=0
print("inserindo elementos da lista a")
while cont<6:
    n=int(input("degite um numero par:"))
    if n%2==0:
        a.append(n)
        cont+=1
    else:
        print("numero impar")        
#lista b
cont=0
print("inserindo elementos da lista b")
while cont<6:
    n=int(input("degite um numero impar:"))
    if n%2!=0:
        b.append(n)
        cont+=1
    else:
        print("numero par")
c=a+b        
print(c)      