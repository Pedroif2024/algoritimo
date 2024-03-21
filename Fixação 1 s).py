def divisao(dividendo, divisor):
  quociente = 0
  resto = dividendo
  while resto >= divisor:
    resto -= divisor
    quociente += 1
  return quociente

dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))

quociente = divisao(dividendo, divisor)

print("O quociente é:", quociente)
