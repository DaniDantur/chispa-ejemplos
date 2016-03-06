#!/usr/bin/env python

import chispaengine

import cv2

chispa = chispaengine.prender()

camara = chispa.camaras.Netbook()
camara.prender()

area = (80, 200, 300, 450)

rojo = "rojo"
verde = "verde"

while(True):

    imagen = camara.traer_imagen()

    zona_recortada = imagen.recortar([area[0], area[1]], [area[2], area[3]])
    imagen.dibujar_caja(area, rojo)

    mascara, objetos = zona_recortada.buscar_objetos_por_color(rojo)
    zona_recortada.mostrar("Zona recortada")

    if objetos is not None:
        objeto_mas_grande = objetos.mas_grande()
        print "El area del objeto mas grande es " + str(objeto_mas_grande.area)
        caja = objeto_mas_grande.encuadrar()
        zona_recortada.dibujar_caja(caja, verde)

    imagen.mostrar("Original")

    chispa.esperar(0.025)
