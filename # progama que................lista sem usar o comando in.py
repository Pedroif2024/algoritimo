lista = [1,2,3,4,5,6,7,8,9,10]
resp='sim'
while True:
    achou=False
    n=int(input("degite um numero para buscar na lista:"))
    cont=0
    while cont<len(lista):
        if lista[cont]==n:
            achou=True
            break
        cont+=1
    if achou:    
        print("O numero",n,"foi encontrado no lugar",cont+1)
    else:
        print("O numero",n," não foi encontrado no lugar")
    resp=input("deseja busca outro numero?:")
    if resp=='não':
        break
print('fim de progama')