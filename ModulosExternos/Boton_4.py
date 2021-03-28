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

class ModuloBoton4():
	def CambiarImagenes(self, imagenes, obj_boton):
		print ("****** Ingreso al modulo del boton 4 ******")

		global lista_btn_presionados, Clicks, lista_pict

		Clicks = nºClicks
		print ("clicks = " + str(Clicks))
		
		ModuloBoton4.lista_btn_presionados = lista_botones_presionados

		print ("ModuloBoton4.lista_btn_presionados: ")
		print (ModuloBoton4.lista_btn_presionados)
		#Obtengo la lista correspondiente al boton seleccionado
		n = ModuloBoton4.lista_btn_presionados[Clicks - 1]
		print ("n: ")
		print (n)

		obtenerLista = Listas_Pictogramas.Listas()
		ModuloBoton4.lista_pict = obtenerLista.Lista_Pictogramas(n)
		
		#Pictogramas pertenecientes al camino generado al seleccionar el primer boton de la lista mostrada
		ModuloBoton4.pic_Btn1 = ModuloBoton3.lista_pict[0]
		ModuloBoton4.pic_Btn2 = ModuloBoton3.lista_pict[1]
		ModuloBoton4.pic_Btn3 = ModuloBoton3.lista_pict[2]
		#El cuarto pictograma será siempre la palabra “SI”.
		ModuloBoton4.pic_Btn4 = "C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Si"
