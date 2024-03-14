#progama que mostra os somatórios do numeros pares de 1 até 500 com for
for i in range (1,501):
    if i%2==0:
        somatoria=0
        for j in range(1,i+1):
            somatoria+=j
        print("O somatoria do numero",i,"é:",somatoria)
print("fim de progama")