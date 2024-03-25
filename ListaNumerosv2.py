lista = []
totalnumeros = None
verificador = int(0)

while totalnumeros is None:
    try:
        while verificador < 3:
            totalnumeros = int(input ("¿Cuantos numeros quieres capturar? "))
            if totalnumeros < 3:
                print ("No pueden ser menos de 3 numeros\n\n")
            else:
                verificador = totalnumeros
    except ValueError:
        print ("\n** Solo ingresar numeros **")

while (len(lista) != totalnumeros):
    try:
        lista.append(int(input("Número a capturar: ")))
    except ValueError:
        print("Solo numeros es permitido")

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
