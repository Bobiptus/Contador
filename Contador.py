def contar_vocalA(cadena):
	contador = 0
	for letra in cadena:
		if letra.lower() in "a":
			contador += 1
	return contador

def contar_vocalE(cadena):
	contador = 0
	for letra in cadena:
		if letra.lower() in "e":
			contador += 1
	return contador

def contar_vocalI(cadena):
	contador = 0
	for letra in cadena:
		if letra.lower() in "i":
			contador += 1
	return contador

def contar_vocalO(cadena):
	contador = 0
	for letra in cadena:
		if letra.lower() in "o":
			contador += 1
	return contador

def contar_vocalU(cadena):
	contador = 0
	for letra in cadena:
		if letra.lower() in "u":
			contador += 1
	return contador

palabra = input("Dame la palabra: ")
conteoA = contar_vocalA(palabra)
conteoE = contar_vocalE(palabra)
conteoI = contar_vocalI(palabra)
conteoO = contar_vocalO(palabra)
conteoU = contar_vocalU(palabra)

print ("Letras A: ",conteoA)
print ("Letras E: ",conteoE)
print ("Letras I: ",conteoI)
print ("Letras O: ",conteoO)
print ("Letras U: ",conteoU)
