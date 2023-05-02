# hola pipol

from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
import sys
from ui_tp3 import *
import matplotlib.pyplot as plt
import numpy as np
import math



class AppWin(QMainWindow, Ui_MainWindow):

    def __init__(self):

        QMainWindow.__init__(self)
        self.setupUi(self)  # Se genera la interfaz llamando al metodo setupUi


    #leer parametros

    #inicializar variables

    #hacer for con las simulaciones

        #ver cuando vuelta sea igual a desde, empezar a agregar en la tabla desde +500

    #mostrar ultima fila en la tabla

    #pasar resultados a cada textBox de cada mantenimiento

    #elaborar conclusion




if __name__ == '__main__':
    app = QApplication(sys.argv)  # create an instance of the application
    appWin = AppWin()  # create an instance of a window
    appWin.show()  # to make the window visible
    app.exec()  # to start up the event loop
    app = QApplication(sys.argv)  # create an instance of the application
    appWin = AppWin()  # create an instance of a window
    appWin.show()  # to make the window visible
    app.exec()  # to start up the event loop