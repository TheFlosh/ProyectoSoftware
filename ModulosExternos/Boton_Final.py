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

class ModuloBotonFinal():
	def Pictogramas_Finales(self):
		print ("****** Ingreso al modulo Pictogramas_Finales ******")
		n = "Final"
		obtenerLista = Listas_Pictogramas.Listas()
		ModuloBotonFinal.lista_pict = obtenerLista.Lista_Pictogramas(n)
		
		#Pictogramas pertenecientes al camino generado al seleccionar el primer boton de la lista mostrada
		ModuloBotonFinal.pic_Btn1 = ModuloBotonFinal.lista_pict[0]
		#print ("ModuloBotonFinal: " + str(ModuloBotonFinal.pic_Btn1))
		ModuloBotonFinal.pic_Btn2 = ModuloBotonFinal.lista_pict[1]
		ModuloBotonFinal.pic_Btn3 = ModuloBotonFinal.lista_pict[2]
		#El cuarto pictograma será siempre la palabra “SI”.
		ModuloBotonFinal.pic_Btn4 = "C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Si"
