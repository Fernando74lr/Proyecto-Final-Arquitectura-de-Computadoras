# Proyecto-Final-Arquitectura-de-Computadoras

## Dependencias y observaciones.

### Pantalla OLED.
 - Se debe activar la configuración I2C en la raspberry si es que no se tiene activado.
 - Reiniciar rasp
 - **Instalar:** ***sudo pip3 install adafruit-circuitpython-ssd1306***

### PyQt5.
 - Dependencias de PyQt5, así como el entorno de ***PyQt Designer*** (por si se quiere diseñar o modificar más características).
 - **Instalar:** ***sudo apt-get update***
 - **Instalar:** ***pip3 install --user pyqt5***
 - **Instalar:** ***sudo apt-get install qt5-default***
 - **Instalar:** ***sudo apt-get install python3-pyqt5***
 - **Instalar:** ***sudo apt-get install qttools5-dev-tools***

Una vez hecho el diseño en ***PyQt Designer***, se debe ubicar, mediante consola, en la carpeta donde está el archivo ".ui" y para convertirlo a un archivo de python ".py", se deberá ejecutar el siguiente comando:
**python -m PyQt5.uic.pyuic -x interfaz.ui -o interfaz.py**

### WIA.
 - **Instalar:** ***pip3 install wia***
 - ***Nota:*** *Cambiar los async por _async cuando te marque el error.*

### DHT11 (Sensor de humedad y temperatura).
 - **Instalar:** ***pip3 install adafruit-circuitpython-dht***
 - **Instalar:** ***sudo apt-get install libgpiod2***

## ¿Qué y cómo ejecutar?
 * Los archivos dentro de este repositorio que utilizará son:
   - monitoreo.py
   - interfaz.py
   - sensorDHT11.py
 * Dentro de la carpeta donde se encuentran estos 3 archivos y las dependencias instaladas, deberá abrir una consola y ejecutar el siguiente comando para iniciar el programa con interfaz gráfica: **python3 monitoreo.py**.
