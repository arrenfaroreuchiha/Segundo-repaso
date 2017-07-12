from c import main

repetir = 1
while repetir != 0:
	main()
	print "Si desea repetir marque 1 si no marque 0."
	repetir = int(raw_input("Desea repetir este proceso:"))
	while repetir > 1:
		repetir = int(raw_input("Marque como se le indica arriba ANIMAL:"))