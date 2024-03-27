a=[]
b=[]
c=[]
for i in range(5):
    a.append (int(input("degite o {i+1} numeros de A:")))
    b.append (int(input("degite o {i+1} numeros de B:")))
    c.append(a[i]-b[i])
print(c)