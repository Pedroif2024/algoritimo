maior = 0
menor = 0
while True:
    n = int(input("Digite um número: "))
    if n > maior:
        maior = n
    if n < menor or menor == 0:
        menor = n
    if n < 0:
        break
print("Maior valor:", maior)
print("Menor valor:", menor)
