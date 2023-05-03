# hola pipol

from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
import sys
from ui_tp3 import *
from generadores.normal import *




class AppWin(QMainWindow, Ui_MainWindow):

    def __init__(self):

        QMainWindow.__init__(self)
        self.setupUi(self)  # Se genera la interfaz llamando al metodo setupUi


    def getDiaAveria(self, n):
        '''n: numero random generado\n
        devuelve int de en cuantos dias se rompe el motor'''
        if( n < 0.25 ):
            return 5
        elif( n < 0.70 ):
            return 6
        elif( n < 0.90 ):
            return 7
        else:
            return 8

    def calcularMaximo(self, acum, maxActual):
        return max(acum, maxActual)
        


    def simulacion(self):
        
        #leer parametros para la simulacion
        if(self.cantSimLineEdit.text() != "" and 
           self.desdeLineEdit.text() != "" and
           self.mediaLineEdit.text() != "" and
           self.desvEstLineEdit.text() != "" and
           self.costoRevisionLineEdit.text() != "" and
           self.costoArregloLineEdit.text() != ""):
            
            cantSimulaciones = int(self.cantSimLineEdit.text())
            primeraLineaAVer = int(self.desdeLineEdit.text())
            media = int(self.mediaLineEdit.text())
            desvEstandar = float(self.desvEstLineEdit.text())
            costoRevision = int(self.costoRevisionLineEdit.text())
            costoArreglo = int(self.costoArregloLineEdit.text())

            
            #inicializar variables
            reloj = 0
            costoTotalPreventivo = 0
            costoPromedioPreventivo = 0
            acumTiempoPreventivo = 0
            acumAveriasPreventivo = 0
            acumMaxDiasSinAveriasPreventivo = 0
            maxDiasSinAveriasPreventivo = 0
            costoTotalCorrectivo = 0
            costoPromedioCorrectivo = 0
            acumTiempoCorrectivo = 0
            acumAveriasCorrectivo = 0
            maxDiasSinAveriasCorrectivo = 0

            hayRNDGenerado = False
            hayArreglo = False
            hayControl = False

            for i in range(cantSimulaciones):
                #hacer todos los calculos
                
                reloj = i+1
                #crear cantidad de horas a trabajar
                horasFuncTupla = normalConvolucion(media, desvEstandar)
                rndHoras = horasFuncTupla[0]
                horasFunc = horasFuncTupla[1]

                if not hayRNDGenerado:
                    rndDiaAveria = random.random()
                    diaAveria = self.getDiaAveria(rndDiaAveria)
                    proxAveria = reloj + diaAveria - 1
                    proxControl = reloj + 6 - 1
                    hayRNDGenerado = True

                    if(proxAveria <= proxControl): #ver si hay control o averia
                        hayArreglo = True
                    else:
                        hayControl = True
                

                if(hayArreglo and reloj == proxAveria): #es el dia que se rompe y se arregla
                    costoTotalPreventivo += 2500
                    costoPromedioPreventivo = costoTotalPreventivo / reloj
                    acumTiempoPreventivo += 0 # como se pasa todo el dia arreglando, no se cuentan las horas
                    acumAveriasPreventivo += 1
                    maxDiasSinAveriasPreventivo = self.calcularMaximo(acumMaxDiasSinAveriasPreventivo, maxDiasSinAveriasPreventivo)
                    acumMaxDiasSinAveriasPreventivo = 0
                    hayRNDGenerado = False
                    hayArreglo = False

                elif(hayControl and reloj == proxControl): #es el dia que hay que hacer el control 
                    costoTotalPreventivo += 900
                    costoPromedioPreventivo = costoTotalPreventivo / reloj
                    acumTiempoPreventivo += horasFunc 
                    acumMaxDiasSinAveriasPreventivo += 1
                    maxDiasSinAveriasPreventivo = self.calcularMaximo(acumMaxDiasSinAveriasPreventivo, maxDiasSinAveriasPreventivo)
                    hayRNDGenerado = False
                    hayControl = False
                else:
                    costoPromedioPreventivo = costoTotalPreventivo / reloj
                    acumTiempoPreventivo += horasFunc 
                    acumMaxDiasSinAveriasPreventivo += 1
                    maxDiasSinAveriasPreventivo = self.calcularMaximo(acumMaxDiasSinAveriasPreventivo, maxDiasSinAveriasPreventivo)


                #verificar al final cuando vuelta sea igual a desde, empezar a agregar en la tabla desde +500
                if(reloj >= primeraLineaAVer and reloj <= (primeraLineaAVer + 500)):
                    #agregar valores en las filas de la tabla
                    pass
        #hacer for con las simulaciones

            

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