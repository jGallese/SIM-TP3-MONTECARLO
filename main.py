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
        if (n < 0.25):
            return 5
        elif (n < 0.70):
            return 6
        elif (n < 0.90):
            return 7
        else:
            return 8

    def calcularMaximo(self, acum, maxActual):
        return max(acum, maxActual)

    def cargarDatosTabla(self, indice, reloj, RNDTiempo1, RNDTiempo2, tiempoFuncionando, RNDDiaAveria, diaAveriaPreventivo, diaControlPreventivo, costoControlPreventivo, costoAveriaPrenventiva, costoTotalPreventivo, costoPromedioPreventivo, acumTiempoPreventivo, acumDiasSinAveriasPreventivo, maxDiasSinAveriasPrventivo, acumAveriasPreventiva, diaAveriaCorrectivo, arreglo, costoAveriaCorrectivo, costoTotalCorrectivo, costoPromedioCorrectivo, acumTiempoCorrectivo, acumDiasSinAveriasCorrectivo, maxDiasSinAveriaCorrectivo, acumAveriasCorrectivo):
        self.tableWidget.insertRow(indice)
        self.tableWidget.setItem(
            indice, 0, QtWidgets.QTableWidgetItem(str(reloj)))
        self.tableWidget.setItem(
            indice, 1, QtWidgets.QTableWidgetItem(str(RNDTiempo1)))
        self.tableWidget.setItem(
            indice, 2, QtWidgets.QTableWidgetItem(str(RNDTiempo2)))
        self.tableWidget.setItem(
            indice, 3, QtWidgets.QTableWidgetItem(str(tiempoFuncionando)))
        self.tableWidget.setItem(
            indice, 4, QtWidgets.QTableWidgetItem(str(RNDDiaAveria)))
        self.tableWidget.setItem(
            indice, 5, QtWidgets.QTableWidgetItem(str(diaAveriaPreventivo)))
        self.tableWidget.setItem(
            indice, 6, QtWidgets.QTableWidgetItem(str(diaControlPreventivo)))
        self.tableWidget.setItem(
            indice, 7, QtWidgets.QTableWidgetItem(str(costoControlPreventivo)))
        self.tableWidget.setItem(
            indice, 8, QtWidgets.QTableWidgetItem(str(costoAveriaPrenventiva)))
        self.tableWidget.setItem(
            indice, 9, QtWidgets.QTableWidgetItem(str(costoTotalPreventivo)))
        self.tableWidget.setItem(
            indice, 10, QtWidgets.QTableWidgetItem(str(costoPromedioPreventivo)))
        self.tableWidget.setItem(indice, 11, QtWidgets.QTableWidgetItem(
            str(acumTiempoPreventivo)))
        self.tableWidget.setItem(
            indice, 12, QtWidgets.QTableWidgetItem(str(maxDiasSinAveriasPrventivo)))
        self.tableWidget.setItem(
            indice, 13, QtWidgets.QTableWidgetItem(str(acumAveriasPreventiva)))
        self.tableWidget.setItem(
            indice, 14, QtWidgets.QTableWidgetItem(str(RNDDiaAveria)))
        self.tableWidget.setItem(
            indice, 15, QtWidgets.QTableWidgetItem(str(diaAveriaCorrectivo)))
        self.tableWidget.setItem(
            indice, 16, QtWidgets.QTableWidgetItem(str(costoAveriaCorrectivo)))
        self.tableWidget.setItem(
            indice, 17, QtWidgets.QTableWidgetItem(str(costoTotalCorrectivo)))
        self.tableWidget.setItem(
            indice, 18, QtWidgets.QTableWidgetItem(str(costoPromedioCorrectivo)))
        self.tableWidget.setItem(
            indice, 19, QtWidgets.QTableWidgetItem(str(acumTiempoCorrectivo)))
        self.tableWidget.setItem(indice, 20, QtWidgets.QTableWidgetItem(
            str(maxDiasSinAveriaCorrectivo)))
        self.tableWidget.setItem(indice, 21, QtWidgets.QTableWidgetItem(
            str(acumAveriasCorrectivo)))

    def simulacion(self):

        # leer parametros para la simulacion
        if (self.cantSimLineEdit.text() != "" and
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
            control = int(self.controlLineEdit.text())

            # inicializar variables
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
            acumMaxDiasSinAveriasCorrectivo = 0
            maxDiasSinAveriasCorrectivo = 0
            proxAveriaPreventivo = 0
            proxAveriaCorrectivo = 0
            hayRNDGenerado = False
            hayArreglo = False
            hayControl = False
            proxControl = 0

            for i in range(cantSimulaciones):
                # hacer todos los calculos
                seControlo = False
                seArregloPreventivo = False
                seArregloCorrectivo = False
                reloj = i+1
                # crear cantidad de horas a trabajar
                horasFuncTupla = normalConRandom(media, desvEstandar)

                # este valor no es un random, por ahi deberiamos agregar otra columna y usar el metodo box muller con los 2 rnd dados
                horasFunc = horasFuncTupla[1]
                rndHoras1 = horasFuncTupla[2]
                rndHoras2 = horasFuncTupla[3]

                if not hayRNDGenerado:
                    rndDiaAveria = random.random()
                    diaAveria = self.getDiaAveria(rndDiaAveria)
                    proxAveria = reloj + diaAveria - 1
                    hayRNDGenerado = True
                    if (proxAveriaPreventivo < reloj or proxControl < reloj):
                        proxAveriaPreventivo = proxAveria
                        proxControl = reloj + control - 1
                        if (proxAveriaPreventivo <= proxControl):  # ver si hay control o averia
                            hayArreglo = True
                        else:
                            hayControl = True

                    if (proxAveriaCorrectivo < reloj):
                        proxAveriaCorrectivo = proxAveria

                # Averia Preventiva:
                # es el dia que se rompe y se arregla
                if (hayArreglo and reloj == proxAveriaPreventivo):
                    costoTotalPreventivo += costoArreglo
                    # como se pasa todo el dia arreglando, no se cuentan las horas
                    acumTiempoPreventivo += 0
                    acumAveriasPreventivo += 1
                    acumMaxDiasSinAveriasPreventivo = 0
                    hayRNDGenerado = False
                    hayArreglo = False
                    seArregloPreventivo = True

                # es el dia que hay que hacer el control
                elif (hayControl and reloj == proxControl):
                    costoTotalPreventivo += costoRevision
                    acumTiempoPreventivo += horasFunc
                    acumMaxDiasSinAveriasPreventivo += 1
                    maxDiasSinAveriasPreventivo = self.calcularMaximo(
                        acumMaxDiasSinAveriasPreventivo, maxDiasSinAveriasPreventivo)
                    hayRNDGenerado = False
                    hayControl = False
                    seControlo = True

                # Dia comun
                else:
                    acumTiempoPreventivo += horasFunc
                    acumMaxDiasSinAveriasPreventivo += 1
                    maxDiasSinAveriasPreventivo = self.calcularMaximo(
                        acumMaxDiasSinAveriasPreventivo, maxDiasSinAveriasPreventivo)

                costoPromedioPreventivo = costoTotalPreventivo / reloj

                # AVERIA CORRECTIVA:

                if (reloj == proxAveriaCorrectivo):
                    costoTotalCorrectivo += costoArreglo
                    acumAveriasCorrectivo += 1
                    acumMaxDiasSinAveriasCorrectivo = 0
                    # como se pasa todo el dia arreglando, no se cuentan las horas
                    acumTiempoCorrectivo += 0
                    hayRNDGenerado = False
                    seArregloCorrectivo = True
                else:
                    acumTiempoCorrectivo += horasFunc
                    acumMaxDiasSinAveriasCorrectivo += 1
                    maxDiasSinAveriasCorrectivo = self.calcularMaximo(
                        acumMaxDiasSinAveriasCorrectivo, maxDiasSinAveriasCorrectivo)
                costoPromedioCorrectivo = costoTotalCorrectivo / reloj

                # verificar al final cuando vuelta sea igual a desde, empezar a agregar en la tabla desde +500
                if (reloj >= primeraLineaAVer and reloj <= (primeraLineaAVer + 500)):

                    if (seControlo and not seArregloCorrectivo):
                        self.cargarDatosTabla(reloj-primeraLineaAVer, reloj, rndHoras1, rndHoras2, horasFunc, rndDiaAveria, proxAveriaPreventivo, proxControl, costoRevision, "", costoTotalPreventivo, costoPromedioPreventivo, acumTiempoPreventivo, acumMaxDiasSinAveriasPreventivo,
                                              maxDiasSinAveriasPreventivo, acumAveriasPreventivo, proxAveriaCorrectivo, "", "", costoTotalCorrectivo, costoPromedioCorrectivo, acumTiempoCorrectivo, acumMaxDiasSinAveriasCorrectivo, maxDiasSinAveriasCorrectivo, acumAveriasCorrectivo)
                    elif (seControlo and seArregloCorrectivo):
                        self.cargarDatosTabla(reloj-primeraLineaAVer, reloj, rndHoras1, rndHoras2, horasFunc, rndDiaAveria, proxAveriaPreventivo, proxControl, costoRevision, "", costoTotalPreventivo, costoPromedioPreventivo, acumTiempoPreventivo, acumMaxDiasSinAveriasPreventivo,
                                              maxDiasSinAveriasPreventivo, acumAveriasPreventivo, proxAveriaCorrectivo, 1, costoArreglo, costoTotalCorrectivo, costoPromedioCorrectivo, acumTiempoCorrectivo, acumMaxDiasSinAveriasCorrectivo, maxDiasSinAveriasCorrectivo, acumAveriasCorrectivo)
                    elif (seArregloCorrectivo and not seArregloPreventivo):
                        self.cargarDatosTabla(reloj-primeraLineaAVer, reloj, rndHoras1, rndHoras2, horasFunc, rndDiaAveria, proxAveriaPreventivo, proxControl, "", "", costoTotalPreventivo, costoPromedioPreventivo, acumTiempoPreventivo, acumMaxDiasSinAveriasPreventivo, maxDiasSinAveriasPreventivo,
                                              acumAveriasPreventivo, proxAveriaCorrectivo, 1, costoArreglo, costoTotalCorrectivo, costoPromedioCorrectivo, acumTiempoCorrectivo, acumMaxDiasSinAveriasCorrectivo, maxDiasSinAveriasCorrectivo, acumAveriasCorrectivo)
                    elif (seArregloCorrectivo and seArregloPreventivo):
                        self.cargarDatosTabla(reloj-primeraLineaAVer, reloj, rndHoras1, rndHoras2, horasFunc, rndDiaAveria, proxAveriaPreventivo, proxControl, "", costoArreglo, costoTotalPreventivo, costoPromedioPreventivo, acumTiempoPreventivo, acumMaxDiasSinAveriasPreventivo,
                                              maxDiasSinAveriasPreventivo, acumAveriasPreventivo, proxAveriaCorrectivo, 1, costoArreglo, costoTotalCorrectivo, costoPromedioCorrectivo, acumTiempoCorrectivo, acumMaxDiasSinAveriasCorrectivo, maxDiasSinAveriasCorrectivo, acumAveriasCorrectivo)
                    elif (seArregloPreventivo and not seArregloCorrectivo):
                        self.cargarDatosTabla(reloj-primeraLineaAVer, reloj, rndHoras1, rndHoras2, horasFunc, rndDiaAveria, proxAveriaPreventivo, proxControl, "", costoArreglo, costoTotalPreventivo, costoPromedioPreventivo, acumTiempoPreventivo, acumMaxDiasSinAveriasPreventivo,
                                              maxDiasSinAveriasPreventivo, acumAveriasPreventivo, proxAveriaCorrectivo, "", "", costoTotalCorrectivo, costoPromedioCorrectivo, acumTiempoCorrectivo, acumMaxDiasSinAveriasCorrectivo, maxDiasSinAveriasCorrectivo, acumAveriasCorrectivo)
                    else:
                        self.cargarDatosTabla(reloj-primeraLineaAVer, reloj, rndHoras1, rndHoras2, horasFunc, "", proxAveriaPreventivo, proxControl, "", "", costoTotalPreventivo, costoPromedioPreventivo, acumTiempoPreventivo, acumMaxDiasSinAveriasPreventivo,
                                              maxDiasSinAveriasPreventivo, acumAveriasPreventivo, proxAveriaCorrectivo, "", "", costoTotalCorrectivo, costoPromedioCorrectivo, acumTiempoCorrectivo, acumMaxDiasSinAveriasCorrectivo, maxDiasSinAveriasCorrectivo, acumAveriasCorrectivo)
        # hacer for con las simulaciones

        # mostrar ultima fila en la tabla
            self.cargarDatosTabla(501, reloj, rndHoras1, rndHoras2, horasFunc, rndDiaAveria, proxAveriaPreventivo, proxControl, "", "", costoTotalPreventivo, costoPromedioPreventivo, acumTiempoPreventivo, acumMaxDiasSinAveriasPreventivo,
                                  maxDiasSinAveriasPreventivo, acumAveriasPreventivo, proxAveriaCorrectivo, "", "", costoTotalCorrectivo, costoPromedioCorrectivo, acumTiempoCorrectivo, acumMaxDiasSinAveriasCorrectivo, maxDiasSinAveriasCorrectivo, acumAveriasCorrectivo)
        # pasar resultados a cada textBox de cada mantenimiento
            self.costoPromPrevTextEdit.setPlainText(
                str(costoPromedioPreventivo))
            self.costoPromCorrtextEdit.setPlainText(
                str(costoPromedioCorrectivo))

            self.tiempoTotPrevtextEdit.setPlainText(str(acumTiempoPreventivo))
            self.tiempoTotCorrtextEdit.setPlainText(str(acumTiempoCorrectivo))

            self.maxDiasPrevTextEdit.setPlainText(
                str(maxDiasSinAveriasPreventivo))
            self.maxDiasCorrTextEdit.setPlainText(
                str(maxDiasSinAveriasCorrectivo))

            self.cantAveriasPrevTextEdit.setPlainText(
                str(acumAveriasPreventivo))
            self.cantAveriasCorrTextEdit.setPlainText(
                str(acumAveriasCorrectivo))

        # elaborar conclusion
            if (abs(costoPromedioPreventivo - costoPromedioCorrectivo) < 20):
                self.conclusionTextEdit.setText(
                    "La diferencia de costos promedios es pequeña por lo que consideramos que las demas metricas de la preventiva")
            else:
                if (costoPromedioPreventivo <= costoPromedioCorrectivo):
                    self.conclusionTextEdit.setText(
                        "Conviene usar el método Preventivo ya que su costo es menor")
                else:
                    self.conclusionTextEdit.setText(
                        "El costo promedio del correctivo es menor, pero deberiamos analizar las otras metricas")


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create an instance of the application
    appWin = AppWin()  # create an instance of a window
    appWin.show()  # to make the window visible
    app.exec()  # to start up the event loop
    app = QApplication(sys.argv)  # create an instance of the application
    appWin = AppWin()  # create an instance of a window
    appWin.show()  # to make the window visible
    app.exec()  # to start up the event loop
