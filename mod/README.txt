Un aspecto en comun que tienen todos los modulos es que en las funciones si no se pone un termino se tomaran los por defecto, por ejemplo 
si queremos programar el generador de señales y este ya tenia configurada la funcion de salida como un seno al usar la funcion:

configGS(frec=28000) para dejar la frecuencia en 28khz sera como si usted hubiera escrito la funcion:
configGS(signal="pulse", frec=24000 ,vhl= 0.5 ,vll= -0.5 ,width= 20  ,impedance=50, duty="NULL")

En general cuando se documento como usar las funciones se usaron los valores que estas traen por defecto.

