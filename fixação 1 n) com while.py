soma=0
cont=1

while True:
    num=int(input("degite um numero:"))
    if num<0:
        break
    soma+=num
    media=soma/cont
    cont+=1
print("o somatorio dos valores é:",soma)
print("a madia dos valoresé:",media)
print("o total de valores lidos é:",cont-1)