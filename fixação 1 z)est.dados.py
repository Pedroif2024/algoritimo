a=[]
impar=0
total=0
for i in range(10):
    a.append(int(input("degite um numero:")))
    if a[i]%2!=0:
        impar+=1
    total+=1
print("quantidade de numeros pares:",impar)
print("o percentual de elementos impares:",(impar/total)*100,"%")