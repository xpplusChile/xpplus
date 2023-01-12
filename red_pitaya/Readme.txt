Para conectarse a la red pitaya es necesario estar conectado a la misma red, actualmente es por Lan, cuando este sea el caso se hace "sudo nmap -sP 10.3.84.1-254" y se revisa los resultados, el que nos interesa es la IP asociada a "instrumentation technologies", luego de esto se hace ssh con usuario root y con la ip obtenida, por ejemplo "ssh root@10.3.84.14" y se ingresa la contraseña.

Al ingresar "df -h" en la consola de la red pitaya se encuentra que la memoria en la cual se guardan los datos tiene un maximo de 3.7G, una vez
eliminados todos los datos tomados de la memoria usando nuvamente "df -h" la memoria ocupada es de 845M y se nos indica que la memoria disponible
es de 2.7G a pesar de que con una calculadore podemos ver que la memoria disponible es de 2.87G

Mirando el nombre de los archivos se puede ver que la creacion de un nuevo archivo de datos es cada una hora pero hasta el momento esto es falso, 
es menos de una hora y la hora indicada de cuando se creo el archivo es distinta a la del reloj interno, en un inicio es 3 horas mayor y no cuenta 
el minuto y tambien a medida que se crean mas archivos parace que se va dessincronizando mas pero reduciendose la hora indicada en el archivo, esto 
aun no esta del todo confirmado aun

Cada archivo de "1 hora" tomado por la noche pesaba 709k

Luego de probar de verificar de forma mas atenta la generacion de archivos se aprecia que se genera un archivo cada dos horas (sin que estuviera corriendo
pitaya.py) y aun asi se segun la forma en que estos fueron nombrados dice que solo paso una hora entre la creacion de cada archivo, importante recalcar 
que aparenta ser exactamente dos horas luego de ser ingresado el comando para tomar datos.

Importante mencionar que antes de cerrar la consola hay que ingresar el comando "disown -ah" porque de lo contrario una vez cerrada la consola los 
procesos asociados a esta no continuaran, en estos procesos se incluyen la toma de datos y la rutina para subir los datos al servidor y luego
eliminarlos de pitaya.


