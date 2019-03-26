#!C:\Python27
"""
Nombre: JeanKarin
Fecha: 17/03/2019
"""

# Comprobamos datos del fichero
def ComprobarFitxero(euro):
	for i in range(len(euro)):
			if (euro[i][7] not in semana or euro[i][9] not in meses):
				print ("Error en los datos, revisar dia o mes.")
				print ("Fallo en linea: " + str(i))
				print ("Dia de la semana: " + euro[i][7] + "\nMes: " + euro[i][9])
				break

# Lectura fichero csv
def LecturaFichero(Lectura):
	numeros = []
	fichero = open(Lectura,'r')
	lineas = csv.reader(fichero)
	for line in lineas:
		numeros.append(line)

	return numeros

# Funcion principal
def main():
	# Definimos las variables
	
	# Tratamos los argumentos
	parser = argparse.ArgumentParser()
	parser.add_argument("-f", "--file", help="Nombre de archivo a procesar")
	args = parser.parse_args()

	# Tratamos el archivo y escribimos en la base de datos
	if args.file:
		print ("Procesamos el archivo con nombre : ", args.file)
		if (args.file == 'numeros.txt'):
			euro = LecturaFichero(args.file)
			ComprobarFitxero(euro)
			consulta = SqlStatement(euro)
			InsertData(consulta)
		elif (args.file == 'millones.txt'):
			euro = LecturaFichero(args.file)
			consmill = SqlStatement2(euro)
			InsertData(consmill)

if __name__ == '__main__':
	# Librerias
	import argparse
	import csv
	from sql_insert import SqlStatement
	from sql_insert import SqlStatement2
	from mysql_con import *

	# Variables globales
	semana = ["'Martes'","'Viernes'"]
	meses = ["'Enero'","'Febrero'","'Marzo'","'Abril'","'Mayo'","'Junio'","'Julio'","'Agosto'","'Septiembre'","'Octubre'","'Noviembre'","'Diciembre'"]
	
	# Ejecutamos funcion principal
	main()