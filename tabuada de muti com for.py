while True:
    n=int(input("degite um numero para ver a tabuada:"))
    print("tabuada de multiplivação do numero",n)
    for i in range(1,11):
        print(i,"x",n,"=",i*n)
    continua=input("deseja continuar? (sim/não)")
    if continua=="não":
     break