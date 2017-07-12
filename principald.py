from d import main

repetir = 1
while repetir != 0:
	main()
	repetir = int(raw_input("Repetir:"))
	while repetir > 1:
		repetir = int(raw_input("Repetir:"))
	