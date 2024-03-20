#progama que ler dez valores e aprensenta a soma desses valores e a medias deles com for
soma = 0
for i in range(1,11):
    valor=int(input("degite o valor:"))
    soma+=valor
media=soma/10
print('a soma dos valores é:',soma)
print('a media dos valores é:',media)