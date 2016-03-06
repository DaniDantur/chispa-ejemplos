#!/usr/bin/env python

import chispaengine

chispa = chispaengine.prender()

camara = chispa.camaras.Netbook()
camara.prender()

color = "rojo"

while(True):

    imagen = camara.traer_imagen()

    zona_recortada = imagen.recortar([80, 200], [300, 450])

    mascara, objetos = zona_recortada.buscar_objetos_por_color(color)

    imagen.mostrar("Original")
    zona_recortada.mostrar("Zona recortada")


    if objetos is not None:
        objeto_mas_grande = objetos.mas_grande()
        print "El area del objeto mas grande es " + str(objeto_mas_grande.area)


    chispa.esperar(0.025)
