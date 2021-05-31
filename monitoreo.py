#pip install wia
import sys
import os
import time
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import threading
#OLED
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
#WIA
from wia import Wia
#Sensor Digital de Luz
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#Dia y hora
from datetime import date
from datetime import datetime

#Sensor de luz
LIGHT_PIN = 23
GPIO.setup(LIGHT_PIN, GPIO.IN)

#OLED
i2c = busio.I2C(SCL, SDA)
# Crea la clase y define el ancho y alto de pantalla
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

#interfaz
from interfaz import *
#Sensor ultrasonico
#from sensorDistancia import *
#Sensor temperatura y humedad
from sensorDHT11 import *
distancia = 0
temperatura = 0
humedad = 0
luz = -1
distanciaTemp = 0
temperaturaTemp = 0
humedadTemp = 0
luzTemp = -1
bloqueador = threading.Lock()
stop = 0

class Ui_MainWindow(QtWidgets.QMainWindow,Ui_MainWindow, Tools):
    def __init__(self, *args, **kwargs):
        #Setup
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)      
        
        self.cont = 0 #Inicializamos variable contador 
        self.contWia = 0 #Contador para actualizar datos en la Wia 
        #self.pahotime() #Inicializamos timer
        #Conexiones
        self.labelTemperatura.setText('-- °C')
        self.labelProximidad.setText('---')
        self.progressBar.setValue(0)
        
        #RECORDATORIO DE BORRAR EL BOTON AAAA
        thread = threading.Thread(target=self.getData)
        thread.start()
        
        thread2 = threading.Thread(target=self.printData)
        thread2.start()

        
    
    #Metodos
    def getData(self):
        global distanciaTemp, temperaturaTemp, humedadTemp, luzTemp, bloqueador ,stop
        while stop==0:
            bloqueador.acquire()
            #distanciaTemp = self.sensorUltrasonico()
            luzTemp = self.getLight()
            dht11Datos = self.sensorHumedadYTemperatura()
            if(dht11Datos != None):
                temperaturaTemp = dht11Datos[0]
                humedadTemp = dht11Datos[1]
            bloqueador.release()
            time.sleep(2)

    def getLight(self):
        if GPIO.input(LIGHT_PIN):
          return 0
        else:
          return 1
        
    #
    def printData(self):
        global distancia, temperatura, humedad, luz, bloqueador, distanciaTemp, temperaturaTemp, humedadTemp, luzTemp, stop
        while stop==0:
            self.labelRefresh.setText('Actualizado hace: %d s' %self.cont)
            self.cont+=1 #Contador aumenta en 1
            self.contWia+=1
            
            now = datetime.now()
            format = now.strftime('%d/%m/%Y, Hora: %H:%M:%S')
            self.labelFecha.setText('Fecha: ' + format)
            
            if(self.contWia >= 10):
                wia = Wia()
                wia.access_token = "d_sk_dVqXRe0P4kFURX4z9hyJ7NfE"
                wia.Event.publish(name="temperature", data=temperatura)
                wia.Event.publish(name="humedad", data=humedad)
                wia.Event.publish(name="iluminacion", data=luz)
                self.contWia=0
            
            bloqueador.acquire()
            '''if(distancia != distanciaTemp):
                distancia = distanciaTemp
                self.labelProximidad.setText('%.2f cm' %distancia)'''
            
            if(luz != luzTemp):
                luz = luzTemp
                self.showOLED()
                if(luz == 0):
                    self.labelProximidad.setText('No hay luz')
                    self.labelProximidad.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(148, 176, 218, 255), stop:1 rgba(129, 10, 232, 255)); border-radius: 20px; color: white")
                elif (luz == 1):
                    self.labelProximidad.setText('Si hay luz')
                    self.labelProximidad.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(249, 224, 27, 255), stop:0.973214 rgba(255, 170, 0, 255), stop:1 rgba(239, 152, 1, 255)); border-radius: 20px; color: white")
                self.cont = 0
                
            if(humedad != humedadTemp):
                humedad = humedadTemp 
                self.showOLED()  
                #self.labelTemperatura.setText(f'{temperatura} °C')
                self.progressBar.setValue(humedad)
                self.cont = 0
            
            if(temperatura != temperaturaTemp):
                temperatura = temperaturaTemp
                self.showOLED()
                self.labelTemperatura.setText(f'{temperatura} °C')
                self.cont = 0
            
            bloqueador.release()
            time.sleep(1)
      
    #Funcion para imprimir en la pantala OLED 
    def showOLED(self):
        global distancia, temperatura, humedad, luz
        #Limpiamos OLED
        disp.fill(0)
        disp.show()
        image = Image.new('1', (128, 64))
        draw = ImageDraw.Draw(image)

        font = ImageFont.load_default()

        #Iluminacion
        if(luz == 0):
            draw.text((10, 12),  'No hay luz',  font=font, fill=255)
        elif (luz == 1):
            draw.text((10, 12),  'Si hay luz',  font=font, fill=255)
            
        #Temperatura
        draw.text((10, 24),  'T: ' + str(temperatura) + ' °C',  font=font, fill=255)
        
        #Humedad
        draw.text((10, 36),  'H: ' + str(humedad) + '%',  font=font, fill=255)
        

        # Muestra Texto
        disp.image(image)
        disp.show()
        #Limpia El OLED
        '''time.sleep(t)
        disp.fill(0)
        disp.show()  '''
    
    def closeEvent(self, event):
        global stop
        stop=1
        disp.fill(0)
        disp.show()
        GPIO.cleanup()
        event.accept()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Ui_MainWindow()
    window.show()
    app.exec_()
