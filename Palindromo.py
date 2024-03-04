texto_original = input("Dame la palabra o frase: ")
texto_invertido = texto_original[::-1]

if texto_original == texto_invertido:
    print ("Si es un palindromo")
else:
    print ("No es un palindromo")
