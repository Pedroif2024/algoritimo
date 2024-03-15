primeiro=1
segundo=1
print("primeiro")
print("segundo")
cont=2
for cont in range(1,14):
    proximo=primeiro+segundo
    print(proximo)
    primeiro=segundo
    segundo=proximo
    cont+=1
print("fim da serie de fibonacci")