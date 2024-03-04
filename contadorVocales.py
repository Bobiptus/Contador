diccionario = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

palabra = input("Dame la palabra: ")
for letra in palabra:
    if letra.lower() in diccionario:
        diccionario[letra.lower()] += 1

print("vocales: ",diccionario)
