a=[]
soma=0
for i in range(0,5):
    a.append(int(input("degite um numero:")))
    if a[i]%2!=0:
        soma+=a[i]
print("A SOMA DOS NUMEROS ÍMPARES É:",soma)
