a=[]
b=[]
for i in range(5):
    a.append(int(input("degite um numero:")))
    somatorio=0
    for j in range(a[i]+1):
        somatorio+=j
    b.append(somatorio)
print(a)
print(b)