Hay que tener en cuenta que si se fuerza el termino del script ya sea cerrando la consola de comandos o de otra forma hay que desconectar y reconectar el DRS4 ya que 
el computador pierde la capacidad de conectarse con el DRS4.

info() sirve para ver si se logro la coneccion don el dispositivo y tambien entrega informacion basica sobre este.
 
load_waveform(CH=1,sampling=5e9,mode="on", rang=0, trig_source="ch1", trig_level=-.1,trig_pol="falling",trig_delay=150e-9) obtiene la informacion de una sola onda, CH= define
el canal del cual se obtiene la onda, sampling= es el sampling frecuency, mode= "on" o mode="off" activa o desactiva el transparent mode, el trig_source= es para definir 
con que canal se usa el trigger(tiene que estar en minusculas el ch1,ch2,ch3 o ch4), trig_level= indica el el punto de trigger y esta en volts, trig_pol=
