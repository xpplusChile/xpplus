import matplotlib.pyplot as plt
import mod.DAQULS.drs4 as drs4
import mod.SGULS as signal
from array import array
import mod.HVULS as hv
import mod.LVULS as lv
import numpy as np
import threading
import time
import csv

print("Empezo")

tiempo=10   #tiempo a medir



signal.configGS_ALL(signal="pulse",frec=2000,vhl=0,vll=-0.8,duty=99.999)

lv.LV_Conf(CH=1, volt=5, curr=3, curr_prot="NULL", volt_prot="NULL")
lv.LV_Conf(CH=2, volt=5.23, curr=3, curr_prot="NULL", volt_prot="NULL")

lv.LV_ON(CH=1)
lv.LV_ON(CH=2)
signal.GS_ON_CH1()

hv.HV_Conf(CH=0, vset=1700, iset=330 , rup=30 , rdown=50 , trip= 2  ,imonrange="high", powerdown="kill")
#hv.HV_OFF(CH=0)

def sleep(tim=5):
	ti_i=time.time()
	ti_a=time.time()-ti_i
	ti_f=tim
	while ti_a<ti_f:
		ti_a=time.time()-ti_i
	
	

def conf(num):
	toma_datos=5
	descanso=1 #se le agregan 2.2 segundos aprox por el tiempo de configurado del generador de señales
	startc=time.time()
	signal.configGS_ALL(signal="pulse",frec=2000,vhl=0,vll=-0.8,duty=99.99)
	actualc=time.time()-startc
	k=99.99
	print("Esta tomando datos de duty %f con tiempo de inicio %f" %(k,actualc)) 
	sleep(tim=espera)
	k=99
	i=1
	for x in range (10):
		actualc=time.time()-startc
		print("Termino de tomar datos de duty %f en el tiempo %f" %(k,actualc)) 
		print("")
		k=99-x
		signal.configGS_ALL(signal="pulse",frec=2000,vhl=0,vll=-0.8,duty=k)	
		sleep(tim=descanso)
		signal.GS_ON_CH1()
		actualc=time.time()-startc
		print("Esta tomando datos de duty %f con tiempo de inicio %f" %(k,actualc)) 
		sleep(tim=toma_datos)
		i=i+1
	for x in range (5):
		actualc=time.time()-startc
		print("Termino de tomar datos de duty %f en el tiempo %f" %(k,actualc)) 
		print("")
		k=k-5
		signal.configGS_ALL(signal="pulse",frec=2000,vhl=0,vll=-0.8,duty=k)	
		sleep(tim=descanso)
		signal.GS_ON_CH1()
		actualc=time.time()-startc
		print("Esta tomando datos de duty %f con tiempo de inicio %f" %(k,actualc)) 
		sleep(tim=toma_datos)
		i=i+1
	print(i)
#################################################################################################################

def hl_mon(num):

	volts  = array('d')  
	amperes= array('d')  
	tiempoV= array('d')  
	tiempoI= array('d')  

	fig = plt.figure()

	ax1 = fig.add_subplot(121)
	ax2 = fig.add_subplot(122)

	ax1.set_title('Imon')
	ax1.set_xlabel('time')
	ax1.set_ylabel('micro I')

	ax1.set_xlim([0, tiempo])
	ax1.set_ylim([0, 400])

	ax2.set_title('Vmon')
	ax2.set_xlabel('time')
	ax2.set_ylabel('V')

	ax2.set_xlim([0, tiempo])
	ax2.set_ylim([0, 1800])


	i=0
	start=time.time()
	actual=time.time()-start
	while actual<tiempo:
		actual1=time.time()-start
		imon = hv.get_HV_par(CH=0,par="IMON")
		actual2=time.time()-start
		vmon = hv.get_HV_par(CH=0,par="VMON")
		imon = imon.split(":")[-1].strip()
		vmon = vmon.split(":")[-1].strip()
		imon = imon.rstrip(imon[-1])
		vmon = vmon.rstrip(vmon[-1])
		#print(vmon)
		if imon != "O":
			y = float(imon)
			ax1.scatter(actual1, y,c="b")
			amperes.append(y)
			tiempoI.append(actual1)
			plt.pause(0.005)
		if vmon != "O":
			y = float(vmon)
			ax2.scatter(actual2, y,c="r")
			volts.append(y)
			tiempoV.append(actual2) 
			plt.pause(0.005)
		
		actual=time.time()-start
		i=i+1
	plt.show()

	#print(volts)


	s=len(amperes)
	a=[0]*2

	header=["Time[s]","Amperes[uA]"]

	with open( "Amperes", 'w', encoding='UTF8') as f:
		writerI = csv.writer(f)
		# write the header
		writerI.writerow(header)
		# write the data
		for x in range(s):
			a[0]=tiempoI[x]
			a[1]=amperes[x]
			writerI.writerow(a)

	s=len(volts)
	a=[0]*2

	header=["Time[s]","Volts[V]"]

	with open( "Volts", 'w', encoding='UTF8') as f:
		writerA = csv.writer(f)
		# write the header
		writerA.writerow(header)
		# write the data
		for x in range(s):
			a[0]=tiempoV[x]
			a[1]=volts[x]
			writerA.writerow(a)
				
			
			
#################################################################################################################		

def drs_medir(num):
	#para pmt trig_level=-0.28
	#para led trig_level=
	drs4.conf_waveform(sampling=5e9,mode="on", rang=0, trig_source="ch1", trig_level=-.028,trig_pol="falling",trig_delay=150e-9)
	drs4.get_data(channel="1,2,3,4",numero_tri="NULL",run_time="NULL",trigger_time=132)


def drs_real(num):
	drs4.conf_waveform(sampling=5e9,mode="on", rang=0, trig_source="ch1", trig_level=-.028,trig_pol="falling",trig_delay=150e-9)
	t,v1=drs4.load_waveform(CH=1,wait_trig="OFF")
	t,v2=drs4.load_waveform(CH=2,wait_trig="OFF")	
	fig = plt.figure()
	ax3 = fig.add_subplot(123)
	ax4 = fig.add_subplot(124)
	ax3.plot(t, v1,c="g")
	ax4.plot(t, v2,c="b")
	
	
	
#################################################################################################################		

if __name__ =="__main__":
	# creating threa
	t1 = threading.Thread(target=hl_mon, args=(10,))
	t2 = threading.Thread(target=drs_medir, args=(10,))
	t3 = threading.Thread(target=conf, args=(10,))

	print("inicio todo")

	t1.start()
	t2.start()
	t3.start()
	
	t1.join()
	t2.join()
	t3.join()
	print("fin todo")
	print("Done!")
	

