# tabela de multiplicação de um numero qualquer
while True:
 n = int(input("degite um numero para ver a tablela:"))
i=1
while 1 <= 10:
 print(n,"x",i,"=",n*i)
 i+=1
 continua=int("deseja continuar?(sim/não)")
 if continua=="não":
   break