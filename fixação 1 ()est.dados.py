a=[]
par=0
impar=0
for i in range(10):
    a.append(int(input("degite um numero:")))
    if a[i]%2==0:
        par+=1
    else:
        impar+=1
print(f"quantidade de numeros pares:{par}")
print(f"quantidade de numeros impares:{impar}")