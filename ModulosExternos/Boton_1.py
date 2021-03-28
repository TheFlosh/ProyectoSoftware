#!/usr/bin/env python
# -*- coding: utf-8 -*

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ModulosExternos import Listas_Pictogramas

pic_Btn1 = ""
pic_Btn2 = ""
pic_Btn3 = ""
pic_Btn4 = ""

lista_btn_presionados = []
Clicks = ""
lista_pict = []

class ModuloBoton1():
	def CambiarImagenes(self, nºClicks, lista_botones_presionados):
		print ("****** Ingreso al modulo del boton 1 ******")

		global lista_btn_presionados, Clicks, lista_pict

		Clicks = nºClicks
		print ("clicks = " + str(Clicks))
		
		ModuloBoton1.lista_btn_presionados = lista_botones_presionados

		print ("ModuloBoton1.lista_btn_presionados: ")
		print (ModuloBoton1.lista_btn_presionados)
		#Obtengo la lista correspondiente al boton seleccionado
		n = ModuloBoton1.lista_btn_presionados[Clicks - 1]
		print ("n: ")
		print (n)

		obtenerLista = Listas_Pictogramas.Listas()
		ModuloBoton1.lista_pict = obtenerLista.Lista_Pictogramas(n)
		
		#Pictogramas pertenecientes al camino generado al seleccionar el primer boton de la lista mostrada
		ModuloBoton1.pic_Btn1 = ModuloBoton1.lista_pict[0]
		ModuloBoton1.pic_Btn2 = ModuloBoton1.lista_pict[1]
		ModuloBoton1.pic_Btn3 = ModuloBoton1.lista_pict[2]
		#El cuarto pictograma será siempre la palabra “SI”.
		ModuloBoton1.pic_Btn4 = "C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Si"

	
# 4 DIAS PLANTEANDO TODO LO QUE ESTA ABAJO PARA TERMINAR HACIENDO LO QUE ESTA ARRIBA!!!!!


"""
		self.a = ["yo", "estoy", "bien"]
		self.b = ["yo", "quiero", "ir", "afuera"]
		self.c = ["yo", "quiero", "ver", "TV"]
		self.d = ["yo", "tengo", "sed"]
		self.e = ["yo", "tengo", "temperatura", "frio"]
		self.f = ["familia", "papá", "LI1", "LI11"]
		self.g = ["familia", "papá", "LI2", "LI21"]
		self.h = ["familia", "papá", "LI3", "LI31"]
		self.i = ["familia", "mamá", "LI1", "LI11"]
		self.j = ["familia", "mamá", "LI2", "LI21"]
		self.k = ["familia", "mamá", "LI3", "LI31"]
		self.l = ["familia", "otra", "LI1", "LI11"]
		self.m = ["familia", "otra", "LI2", "LI21"]
		self.n = ["familia", "otra", "LI3", "LI31"]


		self.lista_1_pict = ["C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoImagenPyqtGaby/Imagenes/Pictogramas - App/pict_Estoy", 
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoImagenPyqtGaby/Imagenes/Pictogramas - App/pict_Quiero",
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoImagenPyqtGaby/Imagenes/Pictogramas - App/pict_Tengo"]


		self.lista_2_pict = ["C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoImagenPyqtGaby/Imagenes/Pictogramas - App/pict_Bien", 
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoImagenPyqtGaby/Imagenes/Pictogramas - App/pict_Mal",
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoImagenPyqtGaby/Imagenes/Pictogramas - App/pict_Enojado"]

		long_lista_botones_presionados = len(lista_botones_presionados)
		
		if long_lista_botones_presionados == 0:
			#Pictogramas pertenecientes al camino generado al seleccionar el primer boton de la lista mostrada ("YO")
			ModuloBoton1.pic_Btn1 = self.lista_1_pict[0]
			ModuloBoton1.pic_Btn2 = self.lista_1_pict[1]
			ModuloBoton1.pic_Btn3 = self.lista_1_pict[2]
			#El cuarto pictograma será siempre la palabra “SI”.
			ModuloBoton1.pic_Btn4 = "C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoImagenPyqtGaby/Imagenes/Pictogramas - App/pict_Si"


		elif (lista_botones_presionados[long_lista_botones_presionados - 1] == a[long_lista_botones_presionados - 1]):
			#Pictogramas pertenecientes al camino generado al seleccionar el primer boton de la lista mostrada ("YO")
			ModuloBoton1.pic_Btn1 = self.lista_1_pict[0]
			ModuloBoton1.pic_Btn2 = self.lista_1_pict[1]
			ModuloBoton1.pic_Btn3 = self.lista_1_pict[2]
"""


"""
		if nºClicks == 1: #(SE SELECCIONA UNA IMAGEN POR 1ERA VEZ Y SE REALIZA EL 1ER CAMBIO)
			#Pictogramas pertenecientes al camino generado al seleccionar el primer boton de la lista mostrada
			ModuloBoton1.pic_Btn1 = "C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoImagenPyqtGaby/Imagenes/Pictogramas - App/pict_Estoy"
			ModuloBoton1.pic_Btn2 = "C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoImagenPyqtGaby/Imagenes/Pictogramas - App/pict_Quiero"
			ModuloBoton1.pic_Btn3 = "C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoImagenPyqtGaby/Imagenes/Pictogramas - App/pict_Tengo"
			#El cuarto pictograma será siempre la palabra “SI”.
			ModuloBoton1.pic_Btn4 = "C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoImagenPyqtGaby/Imagenes/Pictogramas - App/pict_Si"

			ModuloBoton1.lista_btn_presionados.append ("Yo")
			print ("lista_btn_presionados: ")
			print (ModuloBoton1.lista_btn_presionados)

		else:
			#Llamamos a la funcion que posee las listas con los pictogramas correspondientes
			#al boton presionado
			self.ListasPict()
			print ("Lista de botones presionados antes de enviarlos al modulo principal: ")
			print (ModuloBoton1.lista_btn_presionados)


	def ListasPict(self):
		print ("****** Ingreso al método ListasPict ******")
		global lista_btn_presionados, Clicks
		global pic_Btn1, pic_Btn2, pic_Btn3, pic_Btn4

		print ("numero de clicks en ListasPict: " + str(Clicks))
		print ("Lista de botones presionados = ")
		print (ModuloBoton1.lista_btn_presionados)

#---------------------------------------- LISTAS CON LOS PICTOGRAMAS CORRESPONDIENTES ----------------------------------------#
#------------------------------------------------------ AL BOTON 1------------------------------------------------------------#
		
		#*************************************************** YO *************************************************#
		#********************************************************************************************************#
		#La "lista 1" posee los pictogramas correspondientes al camino que comenzó con el pictograma "Yo" + "Estoy"
		self.lista_1_pict = ["C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoImagenPyqtGaby/Imagenes/Pictogramas - App/pict_Bien", 
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoImagenPyqtGaby/Imagenes/Pictogramas - App/pict_Mal",
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoImagenPyqtGaby/Imagenes/Pictogramas - App/pict_Enojado"]
		
		self.lista_1_texto = ["Bien", "Mal", "Enojado"]

		#La "lista 2" posee los pictogramas correspondientes al camino que comenzó con el pictograma "Yo" + "Quiero" + "Ir"
		self.lista_2_pict =  ["C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoImagenPyqtGaby/Imagenes/Pictogramas - App/pict_Afuera", 
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoImagenPyqtGaby/Imagenes/Pictogramas - App/pict_Baño",
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoImagenPyqtGaby/Imagenes/Pictogramas - App/pict_Casa"]

		self.lista_2_texto = ["Afuera", "Baño", "Casa"]
		#************************************************ FAMILIA ***********************************************#
		#********************************************************************************************************#

		#La "lista 3" posee los pictogramas correspondientes al camino que comenzó con el pictograma "Familia" + "Papa"
		self.lista_3_pict =  ["C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoImagenPyqtGaby/Imagenes/Pictogramas - App/pict_LoremIpsum1", 
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoImagenPyqtGaby/Imagenes/Pictogramas - App/pict_LoremIpsum2",
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoImagenPyqtGaby/Imagenes/Pictogramas - App/pict_LoremIpsum3"]

		self.lista_3_texto = ["LoremIpsum1", "LoremIpsum2", "LoremIpsum3"]

		#La "lista 4" posee los pictogramas correspondientes al camino que comenzó con el pictograma "Familia" + "Papa" + "Lorem Ipsum"
		self.lista_4_pict =  ["C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoImagenPyqtGaby/Imagenes/Pictogramas - App/pict_Perro1", 
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoImagenPyqtGaby/Imagenes/Pictogramas - App/pict_Perro2",
								"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoImagenPyqtGaby/Imagenes/Pictogramas - App/pict_Perro3"]

		self.lista_4_texto = ["Perro1", "Perro2", "Perro3"]

#-----------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------#
		
		#Confirmamos cual es el primer pictograma seleccionado al inicio de la frase y cuantos botones se van seleccionado
		if Clicks == 2:
			print ("ingresamos al numero de clicks = " + str(Clicks))
			print ("Primer valor de la lista: " + self.lista_1_texto[0].lower())

			if (ModuloBoton1.lista_btn_presionados[Clicks - 2].lower() == "yo"):	
				#Pictogramas pertenecientes al camino generado al seleccionar el primer boton de la lista mostrada
				ModuloBoton1.pic_Btn1 = self.lista_1_pict[0]
				ModuloBoton1.pic_Btn2 = self.lista_1_pict[1]
				ModuloBoton1.pic_Btn3 = self.lista_1_pict[2]

				#El cuarto pictograma será siempre la palabra “SI”.
				ModuloBoton1.pic_Btn4 = "C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoImagenPyqtGaby/Imagenes/Pictogramas - App/pict_Si"
				
				#Incorporamos la palabra seleccionada a la lista
				ModuloBoton1.lista_btn_presionados.append(self.lista_1_texto[0])

			#DEBO TENER UNA VARIABLE QUE ME INDIQUE EL FINAL DE LA FRASE QUE FORME (NO MAS PICTOGRAMAS DISPONIBLES)

			elif (ModuloBoton1.lista_btn_presionados[Clicks - 2].lower() == "familia"):
				#Pictogramas pertenecientes al camino generado al seleccionar el primer boton de la lista mostrada
				ModuloBoton1.pic_Btn1 = self.lista_3_pict[0]
				ModuloBoton1.pic_Btn2 = self.lista_3_pict[1]
				ModuloBoton1.pic_Btn3 = self.lista_3_pict[2]

				#El cuarto pictograma será siempre la palabra “SI”.
				ModuloBoton1.pic_Btn4 = "C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoImagenPyqtGaby/Imagenes/Pictogramas - App/pict_Si"
				
				ModuloBoton1.lista_btn_presionados.append(self.lista_3_texto[0])

		if Clicks == 3:
			print ("Ingresamos al numero de clicks " + str(Clicks))
			if (ModuloBoton1.lista_btn_presionados[1].lower() == "quiero"):		#debo crear esta ilsta todavia en el modulo Proyecto
				print ("lista_btn_presionados: ")
				print (ModuloBoton1.lista_btn_presionados)


				#Pictogramas pertenecientes al camino generado al seleccionar el primer boton de la lista mostrada
				ModuloBoton1.pic_Btn1 = self.lista_2_pict[0]
				ModuloBoton1.pic_Btn2 = self.lista_2_pict[1]
				ModuloBoton1.pic_Btn3 = self.lista_2_pict[2]

				#El cuarto pictograma será siempre la palabra “SI”.
				ModuloBoton1.pic_Btn4 = "C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoImagenPyqtGaby/Imagenes/Pictogramas - App/pict_Si"
				
				ModuloBoton1.lista_btn_presionados.append("Ir")

				print ("Lista de botones presionados luego de identificar la lista correspondiente: ")
				print (ModuloBoton1.lista_btn_presionados)

			elif (ModuloBoton1.lista_btn_presionados[1].lower() == "familia"):
				print ("lista_btn_presionados: ")
				print (ModuloBoton1.lista_btn_presionados)

				#Pictogramas pertenecientes al camino generado al seleccionar el primer boton de la lista mostrada
				ModuloBoton1.pic_Btn1 = self.lista_4_pict[0]
				ModuloBoton1.pic_Btn2 = self.lista_4_pict[1]
				ModuloBoton1.pic_Btn3 = self.lista_4_pict[2]

				#El cuarto pictograma será siempre la palabra “SI”.
				ModuloBoton1.pic_Btn4 = "C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoImagenPyqtGaby/Imagenes/Pictogramas - App/pict_Si"
				
				ModuloBoton1.lista_btn_presionados.append("Lorem Ipsum")

				print ("Lista de botones presionados luego de identificar la lista correspondiente: ")
				print (ModuloBoton1.lista_btn_presionados)
"""
