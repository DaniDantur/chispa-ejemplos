#!/usr/bin/env python

import chispaengine

chispa = chispaengine.prender()

camara = chispa.camaras.Netbook()
camara.prender()
camara.mostrar_controles()

while(True):

    imagen = camara.traer_imagen()
    imagen.mostrar("Original")

    chispa.esperar(0.025)
