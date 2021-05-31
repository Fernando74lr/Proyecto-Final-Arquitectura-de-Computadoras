# Proyecto-Final-Arquitectura-de-Computadoras

## Usando los elementos analizados a lo largo del semestre, se debe diseñar un sistema de monitoreo para alguna aplicación específica (usando raspberry como la computadora del sistema), con las siguientes características:

* Lectura de 3 variables físicas diferentes: Los sensores deben de comunicarse por alguno de los protocolos analizados en la clase (I2C, UART). Las variables a medir puede ser humedad, temperatura, posición (GPS), etc.
* La lectura de cada sensor debe de aparecer en la matriz de LEDS o en la pantalla OLED, además de en la interfaz de su proyecto (se especifica más adelante).
* Se debe de incluir una interfaz gráfica para la selección del sensor. Cada elemento gráfico de selección del sensor debe de activarse al hacer click en el ícono. La interfaz gráfica habilita la opción de monitorear cada segundo la medición del valor del sensor y lo despliega en una lista o en una gráfica. La lista o gráfica contiene el valor del sensor y el día y la hora de la medición. Este monitoreo permanece activo hasta que el usuario seleccione un nuevo sensor.
* Todos los valores son publicados en una aplicación dentro de WIA (wia.io) y se actualizan cada 10 segundos en algún elemento gráfico que prefiera (gráfica, tabla, letrero, etc.).
* La documentación del proyecto se deberá hacer en github. Deberán agregar videos demostrativos y una buena descripción de los códigos empleados, así como un diagrama de conexiones, secuencia de configuración y guía de uso.
