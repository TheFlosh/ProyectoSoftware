#!/usr/bin/env python
# -*- coding: utf-8 -*

# ----------------  PARA AGREGAR PICTOGRAMAS EN LAS LISTAS ---------------- #
# 1) Crear un método con el nombre "ListaPic_" + Nombre del pictograma que abrira la lista
# 2) Crear 2 listas: una lista con pictograma y una lista con los textos de cada pictograma

print ("****** Ingreso al modulo Listas_Pictogramas ******")

nombre_lista = ""
lista = []

class Listas():
	def Lista_Pictogramas(self,n):
		print ("------Ingreso a Lista_Pictogramas-------")
		#Nombre del método correspondiente
		nombre_lista = "ListaPic_" + n
		#Utilizamos la funcion "gerattr" y la funcion "lambda"
		#NOTA DE INTERNET: Basado en el argumento, la función getattr() recuperará métodos de objetos con el nombre en particular
		lista = getattr(self, nombre_lista, lambda: "No se encontro la lista")
		#Retornamos el valor de la lista encontrado

		return lista()

	def ListaPic_Inicio(self):
		print ("Ingreso a Lista_Inicio")
		Lista_Inicio_pict = ["C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Yo", 
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Familia",
								""]
		Lista_Inicio_texto = ["Yo", "Familia", ""]

		ListaInicio = Lista_Inicio_pict
		ListaInicio.append(Lista_Inicio_texto)

		return ListaInicio

	def ListaPic_Yo(self):
		print ("Ingreso a Lista_Yo")
		Lista_Yo_pict = ["C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Estoy", 
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Quiero",
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Tengo"]
		Lista_Yo_texto = ["Estoy", "Quiero", "Tengo"]

		ListaYo = Lista_Yo_pict
		ListaYo.append(Lista_Yo_texto)

		return ListaYo

	def ListaPic_Estoy(self):
		print ("Ingreso a Lista_Estoy")
		Lista_Estoy_pict = ["C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Bien", 
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Mal",
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Enojado"]
		Lista_Estoy_texto = ["Bien", "Mal", "Enojado"]

		ListaEstoy = Lista_Estoy_pict
		ListaEstoy.append(Lista_Estoy_texto)

		return ListaEstoy

	def ListaPic_Quiero(self):
		print ("Ingreso a Lista_Quiero")
		Lista_Quiero_pict = ["C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Ir", 
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Descansar",
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Ver"]
		Lista_Quiero_texto = ["Ir", "Descansar", "Ver"]

		ListaQuiero = Lista_Quiero_pict
		ListaQuiero.append(Lista_Quiero_texto)

		return ListaQuiero

	def ListaPic_Tengo(self):
		print ("Ingreso a Lista_Tengo")
		Lista_Tengo_pict = ["C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Sed", 
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Hambre",
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Temperatura"]
		
		Lista_Tengo_texto = ["Sed", "Hambre", "Temperatura"]

		ListaTengo = Lista_Tengo_pict
		ListaTengo.append(Lista_Tengo_texto)

		return ListaTengo

	def ListaPic_Ir(self):
		print ("Ingreso a Lista_Ir")
		Lista_Ir_pict = ["C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Afuera", 
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Baño",
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Casa"]
		
		Lista_Ir_texto = ["Afuera", "Baño", "Casa"]

		ListaIr = Lista_Ir_pict
		ListaIr.append(Lista_Ir_texto)

		return ListaIr

	def ListaPic_Ver(self):
		print ("Ingreso a Lista_Ver")
		Lista_Ver_pict = ["C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_TV", 
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Mama",
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Papa"]
		
		Lista_Ver_texto = ["TV", "Mamá", "Papá"]

		ListaVer = Lista_Ver_pict
		ListaVer.append(Lista_Ver_texto)

		return ListaVer

	def ListaPic_Temperatura(self):
		print ("Ingreso a Lista_Temperatura")
		Lista_Temperatura_pict = ["C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Frio", 
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Calor",
								""]
		
		Lista_Temperatura_texto = ["Frío", "Calor", ""]

		ListaTemperatura = Lista_Temperatura_pict
		ListaTemperatura.append(Lista_Temperatura_texto)

		return ListaTemperatura


	def ListaPic_Familia(self):
		print ("Ingreso a Lista_Familia")
		Lista_Familia_pict = ["C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Papa", 
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Mama",
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Otra"]
		
		Lista_Familia_texto = ["Papá", "Mamá", "Otra"]

		ListaFamilia = Lista_Familia_pict
		ListaFamilia.append(Lista_Familia_texto)

		return ListaFamilia


	def ListaPic_Papá(self):
		print ("Ingreso a Lista_Papa")
		Lista_Papa_pict = ["C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_LI1", 
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_LI2",
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_LI3"]
		
		Lista_Papa_texto = ["LI1", "LI2", "LI3"]

		ListaPapa = Lista_Papa_pict
		ListaPapa.append(Lista_Papa_texto)

		return ListaPapa


	def ListaPic_Mamá(self):
		print ("Ingreso a Lista_Mama")
		Lista_Mama_pict = ["C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_LI2", 
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_LI3",
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_LI1"]
		
		Lista_Mama_texto = ["LI4", "LI5", "LI6"]

		ListaMama = Lista_Mama_pict
		ListaMama.append(Lista_Mama_texto)

		return ListaMama

	def ListaPic_Otra(self):
		print ("Ingreso a Lista_Otra")
		Lista_Otra_pict = ["C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_LI3", 
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_LI2",
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_LI1"]
		
		Lista_Otra_texto = ["LI7", "LI8", "LI9"]

		ListaOtra = Lista_Otra_pict
		ListaOtra.append(Lista_Otra_texto)

		return ListaOtra

	def ListaPic_LI1(self):
		print ("Ingreso a Lista_LI1")
		Lista_LI1_pict = ["C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Perro1", 
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Perro2",
								""]
		
		Lista_LI1_texto = ["LI11", "LI12", ""]

		ListaLI1 = Lista_LI1_pict
		ListaLI1.append(Lista_LI1_texto)

		return ListaLI1

	def ListaPic_LI2(self):
		print ("Ingreso a Lista_LI2")
		Lista_LI2_pict = ["C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Perro2", 
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Perro3",
								""]
		Lista_LI2_texto = ["LI21", "LI22", ""]

		ListaLI2 = Lista_LI2_pict
		ListaLI2.append(Lista_LI2_texto)

		return ListaLI2

	def ListaPic_LI3(self):
		print ("Ingreso a Lista_LI3")
		Lista_LI3_pict = ["C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Perro3", 
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Perro1",
								""]
		Lista_LI3_texto = ["LI31", "LI32", ""]

		ListaLI3 = Lista_LI3_pict
		ListaLI3.append(Lista_LI3_texto)

		return ListaLI3

	def ListaPic_LI4(self):
		print ("Ingreso a Lista_LI4")
		Lista_LI4_pict = ["C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Perro1", 
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Perro2",
								""]
		Lista_LI4_texto = ["LI41", "LI42", ""]

		ListaLI4 = Lista_LI4_pict
		ListaLI4.append(Lista_LI4_texto)

		return ListaLI4

	def ListaPic_LI5(self):
		print ("Ingreso a Lista_LI5")
		Lista_LI5_pict = ["C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Perro2", 
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Perro3",
								""]
		Lista_LI5_texto = ["LI51", "LI52", ""]

		ListaLI5 = Lista_LI5_pict
		ListaLI5.append(Lista_LI5_texto)

		return ListaLI5

	def ListaPic_LI6(self):
		print ("Ingreso a Lista_LI6")
		Lista_LI6_pict = ["C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Perro3", 
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Perro2",
								""]
		Lista_LI6_texto = ["LI61", "LI62", ""]

		ListaLI6 = Lista_LI6_pict
		ListaLI6.append(Lista_LI6_texto)

		return ListaLI6

	def ListaPic_LI7(self):
		print ("Ingreso a Lista_LI7")
		Lista_LI7_pict = ["C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Perro2", 
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Perro1",
								""]
		Lista_LI7_texto = ["LI71", "LI72", ""]

		ListaLI7 = Lista_LI7_pict
		ListaLI7.append(Lista_LI7_texto)

		return ListaLI7

	def ListaPic_LI8(self):
		print ("Ingreso a Lista_LI8")
		Lista_LI8_pict = ["C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Perro1", 
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Perro2",
								""]
		Lista_LI8_texto = ["LI81", "LI82", ""]

		ListaLI8 = Lista_LI8_pict
		ListaLI8.append(Lista_LI8_texto)

		return ListaLI8

	def ListaPic_LI9(self):
		print ("Ingreso a Lista_LI9")
		Lista_LI9_pict = ["C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Perro2", 
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Perro3",
								""]
		Lista_LI9_texto = ["LI91", "LI92", ""]

		ListaLI9 = Lista_LI9_pict
		ListaLI9.append(Lista_LI9_texto)

		return ListaLI9


	def ListaPic_Final(self):
		print ("Ingreso a Lista_Final")
		Lista_Final_pict = ["C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_EscucharFrase", 
								"",
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Deshacer"]
		Lista_Final_texto = ["Escuchar", "", "Reiniciar"]

		ListaFinal = Lista_Final_pict
		ListaFinal.append(Lista_Final_texto)

		return ListaFinal


