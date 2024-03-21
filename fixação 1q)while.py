areatotal=0
resp='sim'
while resp!="não":
    comodo=input("degite o comodo:")
    largura=float(input("degite a largura do comodo:"))
    comprimento=float(input("degite o comprimento do comodo:"))
    areacomodo=largura*comprimento
    print("a area do comodo",comodo,"é",areacomodo)
    areatotal+=areacomodo
    resp=input("deseja continuar?:")
    if resp=='não':
        break
print("a area total da casa é",areatotal)