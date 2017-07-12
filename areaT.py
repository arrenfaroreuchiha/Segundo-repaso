print "REPASO"

def a():
	base = int(raw_input("base:"))
	altura = int(raw_input("altura:"))
	lista = [base, altura]
	return b(lista)

def b(lista):
	base = lista[0]
	altura = lista[1]
	area = base * altura
	return c(area)

def c(area):
	print "esta es el area:", area

a()
