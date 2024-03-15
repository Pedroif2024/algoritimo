# progama que calcula a potencia de uma base qualquer elevada a um expoente qualquer
base=int(input("degite a base:"))
expoente=int(input("degite o expoente:"))
potencia=1
for i in range(expoente):
    potencia=potencia*base
    print("potencia de {} elevado a {} é igual a {}".format(base,expoente,potencia))