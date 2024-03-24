lista = [10,7,17,4,12]
i = int(0)
j = len(lista) - 2

while  (i < j):
  
  primernumero = float (lista[i])
  segundonumero = float (lista[i+1])
  tercernumero = float (lista[i+2])
  suma = primernumero + segundonumero
  
  if suma == tercernumero:
    print (f"La suma de {primernumero} y {segundonumero} si es igual a {tercernumero}")
  else:
    print (f"La suma de {primernumero} y {segundonumero} no es igual a {tercernumero}")
  
  i+=1
