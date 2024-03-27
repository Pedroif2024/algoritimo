a=[]
b=[]
for i in range(5):
    a.append(int(input("degite um valor para a lista A:")))
    fatorial=1
    for j in range(1,a[i]+1):
        fatorial=fatorial*j
    b.append(fatorial)
print("lista a:",a)
print("lista b:",b)