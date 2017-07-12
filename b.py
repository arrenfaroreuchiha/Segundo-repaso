# -*- coding: utf-8 -*-
import os.path as path

class aa():
	def a(self):
		lista = []
		if path.exists("texto.txt"):
			cantidad = int(raw_input("Cuantos estudiantes hay:"))
		#else:
        #    open("texto.txt", "a")
        #    cantidad = int(raw_input("Cuantos estudiantes hay:"))
		lista = [cantidad]
		return lista

	def b(self, lista):
		cantidad = lista[0]
		contador = 0
		contador1 = 0
		contador2 = 0
		contador3 = 0
		contador4 = 0
		archivo = open("texto.txt", "a")
        finalArchivo = archivo.tell()
        lista1 = []
		for i in range(cantidad):
			nombre = str(raw_input("Cual es el nombre del estudiante:"))
			apellido = str(raw_input("Cual es el apelldo del estudiante:"))
			edad = str(raw_input("Cual es la edad del estudiante:"))
			sexo = str(raw_input("Cual es el sexo del estudiante:"))
			print "Por favor las notas van de 0.0 a 5.0"
			numero = float(raw_input("Nota de cada estudiante:"))
			while numero > 5.0:
				numero = float(raw_input("Marque como se le indica arriba:"))
			lista1 = [nombre, apellido, edad, sexo, numero]
			archivo.writelines(lista1)
            archivo.seek(finalArchivo)

        a = data.a()
        data.b(a)

	def c(self, lista1):
		if menu == 1:
			data1 = data.a(a)
			procesa = data.b(data1)
		
		if menu == 0:
			print "entro"

		if menu == 2:
			print "entro2"

		if menu == 3:
			print "entro3"

	def d(self):
		print "MENU"
		print "Mostrar Estudiantes = 0"
		print "Agregar estudiantes = 1"
		print "Borrar Estudiantes = 2"
		print "Editar = 3"
		menu = int(raw_input("Que quiere hacer:"))
		print "\n"
		while menu > 3:
			menu = int(raw_input("Que desea hacer:"))
		return menu


data = aa()
def mein():
	data2 = data.d()
	data3 = data.c(data2)




