# -*- coding: utf-8 -*-
print "REPASO"

class sol():
	def estrella(self):
		cantidad = int(raw_input("Cantidad de numeros:"))
		return cantidad

	def luna(self, cantidad):
		lista = []
		vector = []
		contador = 0
		listas = []
		for i in range(cantidad):
			lista.append([])
			for j in range(cantidad):
				numero = int(raw_input("Cual es el numero:"))
				contador = contador + numero
				lista[i].append(numero)
				vector.insert(i, numero)
				vector.sort()
		print "_____________________________"

		for i in range(cantidad):
			print lista[i]

		print "______________________________"
		print lista
		print "______________________________"
		print vector
		listas = [vector, contador]
		return listas
		

	def tierra(self, listas):
		contador = listas[1]
		vector = listas[0]
		print "_______________________________"
		print "Esta es la suma de los numeros del vector:", contador
		print "Este es el numero menor en el vector:", (min(vector))
		print "Este es el numero mayor que hay en el vector:", (max(vector))
		print "Esta es la cantidad de numeros que hay en el vector:", (len(vector))
		print "_______________________________________________"

galaxia = sol() 
def main():
	supernova = galaxia.estrella()
	meteoro = galaxia.luna(supernova)
	jupiter = galaxia.tierra(meteoro)