a=[]
b=[]
cont=0
while cont<5:
    n=int(input("degite um valor: "))
    if n>0:
        a.append (n)
        b.append(a[cont]*-1)
        cont+=1
    else:
        print('degite um valor positivo')
        
print(a)
print(b)