# -*- coding: utf-8 -*-
print "Repaso del whaile"
class a():
	def b(self):
		cantidad = int(raw_input("cantidad:"))
		while cantidad == 0:
			cantidad = int(raw_input("Por favor uqe sea mayor a 1:"))
		return cantidad

	def c(self, cantidad):
		lista = []
		matrix = []
		contador = 0
		total = 0
		total = cantidad * cantidad
		if cantidad > 1:
			for i in range(cantidad):
				matrix.append([])
				for x in range(cantidad):
					numero = int(raw_input("numero:"))
					matrix[i].append(numero)
					lista.insert(i, numero)
					contador = contador + numero
					lista.sort()
			print "\n"
			print "Esta es la matrix", matrix
			print "______________________________"
			print "Este es el vector:", lista
			print "______________________________"
			print "Este es el numero menor:", (min(min(matrix)))
			print "Este es el numero mayor:", (max(max(matrix)))
			print "Esta es la cantidad de numeros que hay:", total
			print "____________________________________________"

			for i in range(cantidad):
				print matrix[i]
		
		else:
			for i in range(cantidad):
				vector = []
				numero = int(raw_input("numero:"))
				vector.insert(i, numero)
				vector.sort()
				contador = contador + numero
			print vector 
		return contador

	def d(self, contador):
		print "_________________________________________"
		print "Esta es la suma de los numeros:", contador
		print "__________________________________________"
		print "Si de seas repetir marque 1  si deseas salir marque 0."
		
		
aa = a()

def main():
	z = aa.b()
	y = aa.c(z)
	a = aa.d(y)

		
