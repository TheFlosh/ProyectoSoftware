#!/usr/bin/env python
# -*- coding: utf-8 -*

import sys
import pyttsx3
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from ModulosExternos import Boton_1,Boton_2,Boton_3,Boton_4,Boton_Final,Listas_Pictogramas, Frases_Completas

NºClicks = 0 	#Variable global que indica cuantas imagenes se van almacenando

pic_Btn1 = "" 	#Imagen seleccionada/Imagen mostrada para seleccionar
pic_Btn2 = ""	#Imagen seleccionada/Imagen mostrada para seleccionar
pic_Btn3 = ""	#Imagen seleccionada/Imagen mostrada para seleccionar
pic_Btn4 = ""	#Imagen seleccionada/Imagen mostrada para seleccionar


pic_Btn_Superior = ""						#Pictograma seleccionado que se visualiza en la parte superior del software
lista_botones_presionados = []				#Lista ordenada de botones presiones para formar cada frase con pictogramas
lista_pict = []								#Lista acumulada de pictogramas que se van seleccionando
var_frase = False 							#Variable que me indica si se llego al final de los pictogramas

obj_boton = ""								#Variable para ayuda a identificar que boton fue presionado

#Clase heredada de QMainWindow (constructor de ventanas)
class Proyecto(QMainWindow):
	#Método constructor de la clase
	def __init__(self):
		global pic_Btn1,pic_Btn2,pic_Btn3,pic_Btn4
		#Iniciar el objeto QMainWindow
		super().__init__()
		#Cargar la configuración del archivo .ui en el objeto
		uic.loadUi(r"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/ProyectoNew.ui", self)
		
		self.setWindowTitle("Nombre de la aplicación")
		self.setWindowIcon(QIcon())

		oimage = QImage(r"C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/fondo_Azul2")
		simage = oimage.scaled(QSize(self.width(), self.height()))
		palette = QPalette()
		palette.setBrush(QPalette.Window, QBrush(simage))
		self.setPalette(palette)

		#La ventana se iniciará maximizada y tendra un tamaño mínimo
		self.showMaximized()
		self.statusBar().showMessage("Bienvenidos")

		self.CargarImagenes()

		#Agregamos una accion al boton 1 y distintas caracteristicas
		#print ("Accion agregada al boton 1")
		self.btn_1.setCheckable(True)
		self.btn_1.setObjectName("Boton1")
		self.btn_1.setIcon(QIcon(pic_Btn1))
		self.btn_1.setIconSize(QSize(240,240))
		#self.btn_1.setStyleSheet('image: url({})'.format("C:/Users/PabloFlores/Desktop/ProyectoSoftware/Imagenes/pict_Yo"))	USO ESTE SI NO QUIERO COLOCAR LA IMAGEN COMO ICONO
		#self.btn_1.setText("Texto de Prueba")	#Texto del botón
		self.btn_1.setStyleSheet("border :10px solid ;"
                             "border-top-color : blue; "
                             "border-left-color : blue;"
                             "border-right-color : blue;"
                             "border-bottom-color : blue")
		#Conexión al método para identificar si se presiono el botón
		self.btn_1.clicked.connect(lambda: CrearBotonSuperior.BotonPresionado(self, self.btn_1))

		#Agregamos una accion al boton 2 y distintas caracteristicas
		#print ("Accion agregada al boton 2")
		self.btn_2.setCheckable(True)
		self.btn_2.setObjectName("Boton2")
		self.btn_2.setIcon(QIcon(pic_Btn2))
		self.btn_2.setIconSize(QSize(240,240))
		self.btn_2.setStyleSheet("border :10px solid ;"
                             "border-top-color : red; "
                             "border-left-color : red;"
                             "border-right-color : red;"
                             "border-bottom-color : red")
		#Conexión al método para identificar si se presiono el botón
		self.btn_2.clicked.connect(lambda: CrearBotonSuperior.BotonPresionado(self, self.btn_2))

		#agregamos una accion al boton 3 y distintas caracteristicas
		#print ("Accion agregada al boton 3")
		self.btn_3.setCheckable(True)
		self.btn_3.setObjectName("Boton3")
		self.btn_3.setIcon(QIcon(pic_Btn3))
		self.btn_3.setIconSize(QSize(240,240))
		self.btn_3.setStyleSheet("border :10px solid ;"
                             "border-top-color : orange; "
                             "border-left-color :orange;"
                             "border-right-color :orange;"
                             "border-bottom-color : orange")
		#Conexión al método para identificar si se presiono el botón
		self.btn_3.clicked.connect(lambda: CrearBotonSuperior.BotonPresionado(self, self.btn_3))

		#agregamos una accion al boton 4 y distintas caracteristicas
		#print ("Accion agregada al boton 4")
		self.btn_4.setCheckable(True)
		self.btn_4.setObjectName("Boton4")
		self.btn_4.setIcon(QIcon(pic_Btn4))
		self.btn_4.setIconSize(QSize(240,240))
		self.btn_4.setStyleSheet("border :10px solid ;"
                             "border-top-color : green; "
                             "border-left-color :green;"
                             "border-right-color :green;"
                             "border-bottom-color : green")
		#Conexión al método para identificar si se presiono el botón
		self.btn_4.clicked.connect(lambda: CrearBotonSuperior.BotonPresionado(self, self.btn_4))

	def CargarImagenes(self):
		global NºClicks, pic_Btn1,pic_Btn2,pic_Btn3 ,pic_Btn4
		global lista_botones_presionados, lista_pict
		#Cargamos las imagenes iniciales para los botones
		print ("------ Metodo CargarImagenes ------")
		print ("NºClicks: " + str(NºClicks))
		if NºClicks == 0:
			print ("Pictogramas iniciales")
			n = "Inicio"
			obtenerLista = Listas_Pictogramas.Listas()
			lista_pict = obtenerLista.Lista_Pictogramas(n)

			pic_Btn1 = lista_pict[0]
			self.lbl_1.setText(lista_pict[3][0])
			pic_Btn2 = lista_pict[1]
			self.lbl_2.setText(lista_pict[3][1])
			pic_Btn3 = ""
			self.lbl_3.setText(lista_pict[3][2])
			pic_Btn4 = "C:/Users/PabloFlores/Google Drive/Prueba Excel - Python/ProyectoSoftware/Imagenes/Pictogramas - App/pict_Si"	
		else:
			#Cargamos las imagenes iniciales para los botones
			pic_Btn1 = pic_Btn1
			pic_Btn2 = pic_Btn2
			pic_Btn3 = pic_Btn3
			pic_Btn4 = pic_Btn4

	def ActualizarImagenes(self):
		print ("------ Metodo ActualizarImagenes ------")
		global pic_Btn1,pic_Btn2,pic_Btn3,pic_Btn4
		self.btn_1.setIcon(QIcon(pic_Btn1))
		self.btn_1.setIconSize(QSize(240,240))
		self.btn_2.setIcon(QIcon(pic_Btn2))
		self.btn_2.setIconSize(QSize(240,240))
		self.btn_3.setIcon(QIcon(pic_Btn3))
		self.btn_3.setIconSize(QSize(240,240))
		self.btn_4.setIcon(QIcon(pic_Btn4))
		self.btn_4.setIconSize(QSize(240,240))

	def keyPressEvent(self,event):
		#Detecta los botones presionados del 1 al 4
		if (event.key() == Qt.Key_1):
			print("pressed 1")
			CrearBotonSuperior.BotonPresionado(self, self.btn_1)

		elif (event.key() == Qt.Key_2):
			print("pressed 2")
			CrearBotonSuperior.BotonPresionado(self, self.btn_2)

		elif (event.key() == Qt.Key_3):
			print("pressed 3")
			CrearBotonSuperior.BotonPresionado(self, self.btn_3)

		elif (event.key() == Qt.Key_4):
			print("pressed 4")
			CrearBotonSuperior.BotonPresionado(self, self.btn_4)


class CrearBotonSuperior():
	#Agregamos una imagen minimizada de la imagen seleccionada
	def BotonPresionado(self, b):
		#print("El boton presionado es: ", b.text())
		global obj_boton, NºClicks
		print ("------------------------------------")
		print ("------------------------------------")
		print ("------ Método BotonPresionado ------")

		#Agregamos una imagen al contador de imagenes
		NºClicks = NºClicks + 1

		if b.isChecked():
				#Configuramos que el boton sea "checkeable" nuevamente
				b.setCheckable(False)
				b.setCheckable(True)
		#Obtenemos el nombre asignado al boton
		obj_boton = b.objectName()

		if (NºClicks <= 4 and obj_boton != "Boton4"):
			if obj_boton == "Boton1" and self.lbl_1.text() != "":
					CrearBotonSuperior.Llamar_Funciones(self)
			elif obj_boton == "Boton2" and self.lbl_2.text() != "":
					CrearBotonSuperior.Llamar_Funciones(self)
			elif obj_boton == "Boton3" and self.lbl_3.text() != "":
					CrearBotonSuperior.Llamar_Funciones(self)				
			else:
				print ("El boton seleccionado se encuentra en blanco")
				NºClicks = NºClicks - 1

		elif (obj_boton == "Boton4"):

			#Llamamos al módulo para el boton 4
			print ("Se ha presionado el boton 4")
			NºClicks = NºClicks - 1
			print ("NºdeClicks despues de presionar boton 4 = " + str(NºClicks))
			
			engine = pyttsx3.init()
			engine.setProperty('rate', 150)
			engine.say("SI")			
			engine.runAndWait()
			
		elif (NºClicks > 4):
			print ("SE HA ALCANZADO EL MAXIMO DE CLICKS PERMITIDOS")
			CrearBotonSuperior.Check_estado_actual(self, obj_boton)

	def Llamar_Funciones(self):
		global NºClicks, obj_boton
		#Si el numero de clicks se encuentra al limite del total estipulado (4 veces) se trabaja normalmente
		CrearBotonSuperior.IdentificarBoton(self, NºClicks, obj_boton)
		CrearBotonSuperior.Agregar_imagen_superior(self)
		Proyecto.CargarImagenes(self)
		Proyecto.ActualizarImagenes(self)
		CrearBotonSuperior.Reproducir_frase(self, lista_botones_presionados)

	def IdentificarBoton(self, Clicks, obj_boton):
		#Identificamos la imagen seleccionada 
		print("------ Método IdentificarBoton ------")
		global pic_Btn1,pic_Btn2,pic_Btn3,pic_Btn4
		global pic_Btn_Superior, lista_botones_presionados, lista_pict, NºClicks
		
		#Confirmamos cual boton es el seleccionado 
		if obj_boton == "Boton1":
			print ("Se ha presionado el boton 1")
			print ("NºClicks = " + str(NºClicks))
			#Llamamos al módulo para el boton 1
			lista_botones_presionados.append(lista_pict[3][0])

			self.configurarBoton1 = Boton_1.ModuloBoton1()
			self.configurarBoton1.CambiarImagenes(NºClicks, lista_botones_presionados)

			#Asigno al boton superior la imagen seleccionada
			pic_Btn_Superior = QIcon(pic_Btn1)

			#Actualizo la lista de botones presionados para formar el texto correspondiente
			lista_pict = Boton_1.ModuloBoton1.lista_pict
			#Verificamos si la lista importada esta vacía
			lista_vacia = CrearBotonSuperior.Check_lista_vacia(self, lista_pict)

			#Verificamos si la lista esta vacía o si se llego al limite de pictogramas para formar una frase
			if (lista_vacia == False):
				#Asigno las imagenes nuevas a las variables para actualizar
				pic_Btn1 = Boton_1.ModuloBoton1.pic_Btn1
				self.lbl_1.setText(lista_pict[3][0])
				pic_Btn2 = Boton_1.ModuloBoton1.pic_Btn2
				self.lbl_2.setText(lista_pict[3][1])
				pic_Btn3 = Boton_1.ModuloBoton1.pic_Btn3
				self.lbl_3.setText(lista_pict[3][2])
				pic_Btn4 = Boton_1.ModuloBoton1.pic_Btn4
				
				#CrearBotonSuperior.Agregar_imagen_superior(self)
				#print ("Lista de botones Presionados en 'Proyecto' = ")
				#print (lista_botones_presionados)
			else:
				#CrearBotonSuperior.Agregar_imagen_superior(self)
				NºClicks = 4			#Para indicar que se llego al final de la linea de pictogramas defino el valor
										#maximo de clicks posibles

				#print ("Lista de botones Presionados en 'Proyecto' = ")
				#print (lista_botones_presionados)
				#print ("Linea de pictogramas finalizado")

		elif obj_boton == "Boton2":
			print ("Se ha presionado el boton 2")
			print ("NºClicks = " + str(NºClicks))
			#Llamamos al módulo para el boton 2
			lista_botones_presionados.append(lista_pict[3][1])

			self.configurarBoton2 = Boton_2.ModuloBoton2()
			self.configurarBoton2.CambiarImagenes(NºClicks, lista_botones_presionados)

			#Asigno al boton superior la imagen seleccionada
			pic_Btn_Superior = QIcon(pic_Btn2)

			#Actualizo la lista de botones presionados para formar el texto correspondiente
			lista_pict = Boton_2.ModuloBoton2.lista_pict

			#Verificamos si la lista esta vacío o si se llego al limite de pictogramas para formar una frase
			lista_vacia = CrearBotonSuperior.Check_lista_vacia(self, lista_pict)

			if (lista_vacia == False):
				#Asigno las imagenes nuevas a las variables para actualizar
				pic_Btn1 = Boton_2.ModuloBoton2.pic_Btn1
				self.lbl_1.setText(lista_pict[3][0])
				pic_Btn2 = Boton_2.ModuloBoton2.pic_Btn2
				self.lbl_2.setText(lista_pict[3][1])
				pic_Btn3 = Boton_2.ModuloBoton2.pic_Btn3
				self.lbl_3.setText(lista_pict[3][2])
				pic_Btn4 = Boton_2.ModuloBoton2.pic_Btn4

			else:
				NºClicks = 4			#Para indicar que se llego al final de la linea de pictogramas defino el valor
										#maximo de clicks posibles

		elif obj_boton == "Boton3":
			print ("Se ha presionado el boton 3")
			print ("NºClicks = " + str(NºClicks))
			#Llamamos al módulo para el boton 3
			lista_botones_presionados.append(lista_pict[3][2])

			print ("lista_pic: " + lista_pict[3][2])

			self.configurarBoton3 = Boton_3.ModuloBoton3()
			self.configurarBoton3.CambiarImagenes(NºClicks, lista_botones_presionados)

			#Asigno al boton superior la imagen seleccionada
			pic_Btn_Superior = QIcon(pic_Btn3)

			#Actualizo la lista de botones presionados para formar el texto correspondiente
			lista_pict = Boton_3.ModuloBoton3.lista_pict
			print ("lista_pict = " + str(lista_pict))
			#Verificamos si la lista esta vacío o si se llego al limite de pictogramas para formar una frase
			lista_vacia = CrearBotonSuperior.Check_lista_vacia(self, lista_pict)
			print ("lista_vacia = " + str(lista_vacia))

			#Verificamos si la lista esta vacío o si se llego al limite de pictogramas para formar una frase
			if (lista_vacia == False):
				#Asigno las imagenes nuevas a las variables para actualizar
				pic_Btn1 = Boton_3.ModuloBoton3.pic_Btn1
				self.lbl_1.setText(lista_pict[3][0])
				pic_Btn2 = Boton_3.ModuloBoton3.pic_Btn2
				self.lbl_2.setText(lista_pict[3][1])
				pic_Btn3 = Boton_3.ModuloBoton3.pic_Btn3
				self.lbl_3.setText(lista_pict[3][2])
				pic_Btn4 = Boton_3.ModuloBoton3.pic_Btn4

			else:
				NºClicks = 4			#Para indicar que se llego al final de la linea de pictogramas defino el valor
										#maximo de clicks posibles

	def Agregar_imagen_superior(self):
		print("------ Método Agregar_imagen_superior ------")
		global NºClicks, obj_boton, pic_Btn1,pic_Btn2,pic_Btn3,pic_Btn4
		global lista_botones_presionados
		#Borramos el Spacer y agregamos una imagen mas
		if NºClicks == 1:
			#Agregamos la primera imagen minimizada
			self.select_1 = QPushButton("")
			
			#Agregamos la imagen seleccionada al boton superior
			self.select_1.setIcon(pic_Btn_Superior)

			#Especificamos el tamaño de la imagen
			self.select_1.setIconSize(QSize(90,90))
	
			#Ajustamos el tamaño del boton superior
			self.select_1.setMinimumSize(90,90)
			self.select_1.setMaximumSize(90,90)

			self.sup_Layout.addWidget(self.select_1)

			#Agregamos un "Spacer" o espaciador lateral
			self.Separador = QSpacerItem(20, 40, QSizePolicy.Expanding)
			self.sup_Layout.addItem(self.Separador)

			#Agregar la palabra seleccionada al texto que se forma
			#Contabilizamos la cantidad de elementos en la lista de botones presionados
			total_lista = len(lista_botones_presionados)
			print ("total_lista = " , str(total_lista))
			print ("lista_botones_presionados = " + str(lista_botones_presionados))
			print ("lista_botones_presionados[0] = " + lista_botones_presionados[0])
			
			#Agregamos cada elemento al texto
			frase_completa = " ".join(lista_botones_presionados)
			self.lbl_frase.setText(frase_completa)

		elif NºClicks < 5:
			try:
				self.sup_Layout.removeItem(self.Separador)
				del self.Separador
				
				#Agregamos un boton mas
				self.select_234 = QPushButton("")
				print("La imagen pertenece a este boton:", obj_boton)
				
				#Agregamos la imagen seleccionada al boton superior y especificamos el tamaño de la imagen
				self.select_234.setIcon(pic_Btn_Superior)	
				self.select_234.setIconSize(QSize(90,90))

				#Ajustamos el tamaño del boton superior
				self.select_1.setMinimumSize(90,90)
				self.select_1.setMaximumSize(90,90)
				
				self.sup_Layout.addWidget(self.select_234)

				#Agregamos un "Spacer"
				self.Separador = QSpacerItem(20, 40, QSizePolicy.Expanding)
				self.sup_Layout.addItem(self.Separador)

				#Agregar la palabra seleccionada al texto que se forma
				#Contabilizamos la cantidad de elementos en la lista de botones presionados
				total_lista = len(lista_botones_presionados)
				print ("total_lista = " , str(total_lista))
				print ("lista_botones_presionados = " + str(lista_botones_presionados))
				print ("lista_botones_presionados[0] = " + lista_botones_presionados[0])

				frase_completa = " ".join(lista_botones_presionados)
				self.lbl_frase.setText(frase_completa)
			except:
				print ("No hay separadores para eliminar")

	def Check_lista_vacia(self,lista):
		print ("------ Método Check_lista_vacia ------")
		#Verificamos que la lista no este vacia y devolvemos un valor "TRUE" en caso de finalizar los pictogramas, o "FALSE"
		global var_frase, pic_Btn1, pic_Btn2, pic_Btn3, pic_Btn4, NºClicks
		if len(lista) == 0:
			print ("Longitud igual a cero ")
			return True
		
		elif (lista == "No se encontro la lista" or NºClicks == 4):
			#ESTE CASO INDICA QUE SE FINALIZO LA LINEA DE PICTOGRAMAS PARA FORMAR LA FRASE DESEADA
			print ("El elemento de la lista es la frase 'No se encontro la lista' ")
			var_frase = True 				#El valor "True" indica que se finalizo el camino del pictograma
			
			self.configurarBotonFinal = Boton_Final.ModuloBotonFinal()
			self.configurarBotonFinal.Pictogramas_Finales()

			lista_pict = Boton_Final.ModuloBotonFinal.lista_pict

			pic_Btn1 = Boton_Final.ModuloBotonFinal.pic_Btn1
			self.lbl_1.setText(lista_pict[3][0])
			pic_Btn2 = Boton_Final.ModuloBotonFinal.pic_Btn2
			self.lbl_2.setText(lista_pict[3][1])
			pic_Btn3 = Boton_Final.ModuloBotonFinal.pic_Btn3
			self.lbl_3.setText(lista_pict[3][2])
			pic_Btn4 = Boton_Final.ModuloBotonFinal.pic_Btn4

			return True
		else:
			print ("Return: False")
			return False

	def Check_estado_actual(self, obj_boton):
		print("------ Método Check_estado_actual ------")
		#Especificamos el uso de la variable global imagenes
		global var_frase,NºClicks

		if var_frase == True:
			print ("obj_boton: " + str(obj_boton))
			print ("var_frase: " + str(var_frase))

			if obj_boton == "Boton1":
				print ("Se reproduce la frase")
				CrearBotonSuperior.Reproducir_frase(self, lista_botones_presionados)
			elif obj_boton == "Boton3":
				print ("Se reinician los pictogramas")
				CrearBotonSuperior.Reiniciar_Pictogramas(self)
			elif NºClicks == 4:
				print ("Se reproduce la frase")
				CrearBotonSuperior.Reproducir_frase(self, lista_botones_presionados)
		else:
			print ("Se pueden agregar mas imagenes")
			print ("obj_boton: " + str(obj_boton))

	def Reproducir_frase(self, frase):
		global NºClicks
		try:
			if NºClicks >= 4 :
				modulo_frase = Frases_Completas.Pict_Frases()
				modulo_frase.Frases_Pictogramas(frase)

				frase_final = Frases_Completas.Pict_Frases.frase_a_decir
				self.lbl_frase.setText(frase_final)

				engine = pyttsx3.init()
				engine.setProperty('rate', 120)
				engine.say(frase_final)

				engine.runAndWait()
			else:
				print ("Error de loop (Demasiados clicks seguidos")
		except:
			pass

	def Reiniciar_Pictogramas(self):
		print("------ Método Reiniciar_Pictogramas ------")
		global NºClicks, var_frase, pic_Btn_Superior, lista_botones_presionados, lista_pict
		NºClicks = 0
		pic_Btn_Superior = ""						#Pictograma seleccionado que se visualiza en la parte superior del software
		lista_botones_presionados = []				#Lista ordenada de botones presiones para formar cada frase con pictogramas
		lista_pict = []								#Lista acumulada de pictogramas que se van seleccionando
		var_frase = False 							#Variable que me indica si se llego al final de los pictogramas
		
		CrearBotonSuperior.EliminarImgSuperior(self.sup_Layout)	
		self.lbl_frase.setText("")	
		Proyecto.CargarImagenes(self)
		Proyecto.ActualizarImagenes(self)

	def EliminarImgSuperior(layout):
		print ("------ Método EliminarImgSuperior ------")
		#Confirmamos si el layout posee widgets
		if layout is not None:
			#Si no esta vacío contamos la cantidad de elementos que posee
			while layout.count():
				print ("layout.count():" + str(layout.count()))
				item = layout.takeAt(0)
				print ("item: " + str(item))
				widget = item.widget()
				print ("widget: " + str(widget))
				if widget is not None:
					widget.setParent(None)
				else:
					CrearBotonSuperior.EliminarImgSuperior(item.layout())
		print ("Imagenes superiores eliminadas")


if __name__ == "__main__":
	#Instancia para iniciar una aplicación
	app = QApplication(sys.argv)
	#Crear un objeto de la clase principal
	GUI = Proyecto()
	#Mostramos la ventana
	GUI.show()
	#Ejecutamos la aplicación
	sys.exit(app.exec()) #Nos aseguramos que la ventana se cierre con el boton "X"
