# -*- coding: utf-8 -*-

class a():
	def b(self):
		base = int(raw_input("base:"))
		altura = int(raw_input("altura:"))
		lista = []
		lista = [base, altura]
		return lista

	def c(self, lista):
		base = lista[0]
		altura = lista[1]
		area = base * altura / 2
		return area

	def d(self, area):
		print "Esta es el area del maldito triangulo:", area

aa = a()
def main():
	bb = aa.b()
	cc = aa.c(bb)
	dd = aa.d(cc)
