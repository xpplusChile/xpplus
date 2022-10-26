Hay que tener en cuenta que si se fuerza el termino del script ya sea cerrando la consola de comandos o de otra forma hay que desconectar 
y reconectar el DRS4 ya que el computador pierde la capacidad de conectarse con el DRS4.
Otro detalle importante es que cada vez que el dispositivo va a recibir una señal de trigger se le da un time.sleep(0.0001) porque de lo contrario
sucedia que el dispositivo tomaba señales (ruido) y las devolvia sin esperar a la señal de trigger y por ende si queremos tomar datos a la mayor
velocidad de medicion posible se recomienda solo esperar el trigger de forma inicial.

info() sirve para ver si se logro la coneccion don el dispositivo y tambien entrega informacion basica sobre este.

conf_waveform(sampling=5e9,mode="on", rang=0, trig_source="ch1", trig_level=-.1,trig_pol="falling",trig_delay=150e-9)
 Configura la obtencion de datos del DRS4,sampling= es el sampling frecuency, mode= "on" o mode="off" activa o desactiva el transparent mode, 
 el trig_source= es para definir con que canal se usa el trigger(tiene que estar en minusculas el ch1,ch2,ch3 o ch4), trig_level= indica el 
 punto de trigger y esta en  volts, trig_pol=  pone la polaridad del trigger en modo "falling" edge  o "rising" edge, trig_delay= es el tiempo 
 de delay en segundos.

wait_trigger()
 No permite que el programa siga corriendo hasta obtener una señal de trigger que cumpla las condicines entregadas en conf_waveform()

load_waveform(CH=1, wait_trig="OFF")
 retorna los valores de tiempo(t) y el voltaje(v) del canal CH=, wait_trigg= es para definir si se espera o no una señal de trigger ("ON" u "OFF") 

get_data(channel="1",numero_tri="NULL",run_time="NULL",trigger_time="NULL")
 channel= es lo que define los canales cuya informacion sera guardada en un archivo externo .root y el formato de este parametro tiene que ser de la 
 forma "1" ; "1,2" ; "1,2,3" o "1,2,3,4", si queremos que los datos sean guardados en funcion del numero de señales de trigger asignamos este valor 
 en numero_tri=, por otro lado si queremos guardar datos en funcion de un tiempo de toma de datos asignamos el valor deseado en segundos a run_time=,
 finalmenet el ultimo parametro que se puede ingresar es el tiempo por el cual se quiere medir sin considerar trigger luego de recibirlo, se le asigna
 el valor deseado a trigger_time=
 Es muy importante mencionar que el ultimo paremetro mencionado tiene la capicidad de pasarse del tiempo dado en run_time=, por ejemplo si ponemos 
 run_time=20 , trigger_time=20 y recibe una señal de trigger al segundo 18 el drs4 seguira tomando datos hasta el segundo 28.
 Un deta
 

