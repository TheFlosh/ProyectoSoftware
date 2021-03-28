#!/usr/bin/env python
# -*- coding: utf-8 -*

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

#MODULO PARA FORMAR LAS FRASES FINALES DEL CONJUNTO DE PICTOGRAMAS SELECCIONADO
print ("****** Ingreso al modulo Pict_Frases ******")
frase_a_decir =""

class Pict_Frases():
    def Frases_Pictogramas(self, frase):
        global frase_a_decir
        print ("------Ingreso a Frases_Pictogramas-------")
        print ("Frase original: " + str(frase))

        dict_frases = {
            tuple(["Yo", "Estoy", "Bien"]) : "Estoy bien",
            tuple(["Yo", "Estoy", "Mal"]) : "Estoy mal",
            tuple(["Yo", "Estoy", "Enojado"]) : "Estoy enojado",
            tuple(["Yo", "Quiero", "Ir", "Afuera"]) : "Quiero ir afuera",
            tuple(["Yo", "Quiero", "Ir", "Baño"]) : "Quiero ir al baño",
            tuple(["Yo", "Quiero", "Ir", "Casa"]) : "Quiero ir a casa",
            tuple(["Yo", "Quiero", "Descansar"]) : "Quiero descansar",
            tuple(["Yo", "Quiero", "Ver","Mamá"]) : "Quiero ver a mamá",
            tuple(["Yo", "Quiero", "Ver","Papá"]) : "Quiero ver a papá",
            tuple(["Yo", "Quiero", "Ver", "TV"]) : "Quiero ver televisión",
            tuple(["Yo", "Tengo", "Sed"]) : "Tengo sed",
            tuple(["Yo", "Tengo", "Hambre"]) : "Tengo Hambre",
            tuple(["Yo", "Tengo", "Temperatura", "Frío"]) : "Tengo frío",
            tuple(["Yo", "Tengo", "Temperatura", "Calor"]) : "Tengo Calor",
            tuple(["Familia", "Papá", "LI1", "LI11"]) : "Faltan Pictogramas",
            tuple(["Familia", "Papá", "LI1", "LI12"]) : "Faltan Pictogramas",
            tuple(["Familia", "Papá", "LI2", "LI21"]) : "Faltan Pictogramas",
            tuple(["Familia", "Papá", "LI2", "LI22"]) : "Faltan Pictogramas",
            tuple(["Familia", "Papá", "LI3", "LI31"]) : "Faltan Pictogramas",
            tuple(["Familia", "Papá", "LI3", "LI32"]) : "Faltan Pictogramas",
            tuple(["Familia", "Mamá", "LI4", "LI41"]) : "Faltan Pictogramas",
            tuple(["Familia", "Mamá", "LI4", "LI42"]) : "Faltan Pictogramas",
            tuple(["Familia", "Mamá", "LI5", "LI51"]) : "Faltan Pictogramas",
            tuple(["Familia", "Mamá", "LI5", "LI52"]) : "Faltan Pictogramas",
            tuple(["Familia", "Mamá", "LI6", "LI61"]) : "Faltan Pictogramas",
            tuple(["Familia", "Mamá", "LI6", "LI62"]) : "Faltan Pictogramas",
            tuple(["Familia", "Otra", "LI7", "LI71"]) : "Faltan Pictogramas",
            tuple(["Familia", "Otra", "LI7", "LI72"]) : "Faltan Pictogramas",
            tuple(["Familia", "Otra", "LI8", "LI81"]) : "Faltan Pictogramas",
            tuple(["Familia", "Otra", "LI8", "LI82"]) : "Faltan Pictogramas",
            tuple(["Familia", "Otra", "LI9", "LI91"]) : "Faltan Pictogramas",
            tuple(["Familia", "Otra", "LI9", "LI92"]) : "Faltan Pictogramas",

        }

        Pict_Frases.frase_a_decir = dict_frases.get(tuple(frase))

