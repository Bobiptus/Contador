lista = [0,7,2,4,6,67,4,8,12]
i = int(0)

while  (i < 7):
  
  primernumero = float (lista[i])
  segundonumero = float (lista[i+1])
  tercernumero = float (lista[i+2])
  suma = primernumero + segundonumero
  
  if suma == tercernumero:
    print (f"La suma de {primernumero} y {segundonumero} si es igual a {tercernumero}")
  else:
    print (f"La suma de {primernumero} y {segundonumero} no es igual a {tercernumero}")
  
  i+=1
