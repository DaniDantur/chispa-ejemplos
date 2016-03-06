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

    if(objetos is not None):
        print "Encontre objetos " + color

    imagen.mostrar("Original")
    zona_recortada.mostrar("Zona recortada")
    mascara.mostrar("Mascara objetos")

    chispa.esperar(0.025)
