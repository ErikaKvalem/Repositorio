#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


Ejemplo de un modulo Python. Contiene una variable llamada pi,
una funcion para calcular el area del un círculo de radio r 
y una clase llamada punto

Created on Thu Feb 11 20:27:30 2021

@author: erika
"""

import math

pi = math.pi

def area_circulo(radio):
    """
    Me da automaticamente la plantilla para generar documentacion
    
    Funcion que devuelve el area de un circulo de radio r

    Parameters
    ----------
    radio : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """

    return pi*radio**2

class Punto:
    """
    Clase que instancia puntos en 2 dimensiones
    """
    def __init__(self, x=0 , y=0):
        self.x= x
        self.y = y
        
    def formato (self):
        
        """

        Returns: Un string con el formato(x,y)
        -------
        None.

        """
        
        txt = "(" + str(self.x) + ", " + str(self.y) + ")"
        
        return txt
        
    def cuadrante(self):
        """
        

        Returns Devuelve el cuadrante donde se encuentra el punto
        -------
        None.

        """
        
        if self.x >0 and self.y >0:
            return 1
        elif self.x <0 and self.y >0:
            return 2
        elif self.x <0 and self.y <0:
            return 3
        elif self.x >0 and self.y <0:
            return 4
        elif self.x !=0 and self.y==0:
            return "x"
        elif self.x == 0 and self.y!=0:
            return "y"
        else:
            return 0
        
    def distancia(self,p):
        """
        Este metodo calcula la distancia a otro punto p

        Parameters
        ----------
        p : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        d = math.sqrt((p.x - self.x))**2 + ((p.y - self.y)**2)
        return d
        
            
