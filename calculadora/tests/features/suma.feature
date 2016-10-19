Feature: Suma de dos numeros
	Yo como usuario de la app calculadora
	quiero realizar una suma de dos numeros
	para poder tener un resultado confiable.

	Scenario: Sumar 2 más 2
		dado que tengo los operandos "2" y "2"
		cuando realizo la suma
		entonces el resultado que obtengo es "4"

	Scenario: Restar 7 menos 3
		dado que tengo los operandos "7" y "2"
		cuando realizo la resta
		entonces el resultado que obtengo es "5"

	Scenario: Multiplicar 4 por 3
		dado que tengo los operandos "4" y "3"
		cuando realizo la multiplicacion
		entonces el resultado que obtengo es "12"

	Scenario: Dividir 10 entre 5
		dado que tengo los operandos "10" y "5"
		cuando realizo la division
		entonces el resultado que obtengo es "2"