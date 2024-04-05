lista = [1,2,3,4,5,6,7,8,9,10]
resp='sim'
while True:
    n=int(input("degite um numero para buscar na lista:"))
    if n in lista:
        print("O numero",n,"esta na lista")
    else:
        print("O numero",n," não esta na lista")
    resp=input("deseja busca outro numero?:")
    if resp=='não':
        break
print('fim de progama')