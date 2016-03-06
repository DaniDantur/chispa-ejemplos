#!/usr/bin/env python

import chispaengine

import cv2

chispa = chispaengine.prender()

camara = chispa.camaras.Netbook()
camara.prender()

rojo = "rojo"
verde = "verde"

min_area = 5000

while(True):

    imagen = camara.traer_imagen()

    _, objetos = imagen.buscar_objetos_por_color(rojo)

    if objetos is not None:
        objeto_mas_grande = objetos.mas_grande()
        area_objeto_mas_grande = objeto_mas_grande.area

        if(area_objeto_mas_grande > min_area):
            print "El area del objeto mas grande es " + str(objeto_mas_grande.area)
            caja = objeto_mas_grande.encuadrar()
            imagen.dibujar_caja(caja, verde)

    imagen.mostrar("Original")

    chispa.esperar(0.025)
