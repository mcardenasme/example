#Hash plegado
def plegado(numero):
    digitos = [int(a) for a in str(numero)]
    parejas = []
    suma = 0

    if(len(digitos) % 2 != 0):
      suma = digitos[-1]
      print(suma)
      digitos.remove(digitos[-1])
      print(digitos)

    for i in range(len(digitos)):
      if (i == 0) or (i % 2 == 0):
        pareja = str(digitos[i]) + str(digitos[i+1])
        parejas.append(pareja)
      print(parejas)

    for i in range(len(parejas)):
      suma += int(parejas[i])
        
    return suma

print(plegado(1234567))