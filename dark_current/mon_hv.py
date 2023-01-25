from array import array
import mod.HVULS as hv
import mod.SGULS as sg
import matplotlib.pyplot as plt
import time
import csv
from ROOT import TNtuple,TFile,TObject,TH1D

	

def plot_Volt_Amp():	

	fname="dark_current_PMT_4_V_2.root"	
	tiempo=60*35 #tiempo inicial de estabilisacion
	tiempo_barrido=60*5
	tiempo_pulser=60
	number_steps=6
	extra_volts_per_step=200
	volt_set=1500
	volt_set_i=700
	CH=0
	
	
	if volt_set >1800:	
		hv.HV_OFF(CH=0)
		volt_Set=500
		print("HV turned off, more HV than PMT can support")
	hv.HV_Conf(CH=0, vset=volt_set, iset=350 , rup=20 , rdown=50 , trip= 2  ,imonrange="high", powerdown="kill")
	sg.configGS_CH1(signal="pulse",polarity="inverted", frec=2000 ,vhl= 0 ,vll= -0.8 ,width="NULL"  ,impedance=50, duty=0.750)
	hv.HV_ON(CH=0)
	#hv.HV_OFF(CH=0)
	
	
	 
	volts  = array('d')  
	amperes= array('d')  
	tiempoV= array('d')  
	tiempoI= array('d')  
	steps   = array('d')  
	
	
	count=0

	i=0
	start=time.time()
	actual=time.time()-start
	
	print("step 0 starting")
	while actual<tiempo:
		#print(actual)
		actual,amperes,volts,tiempoI,tiempoV,steps,y=get_data(actual,start,amperes,volts,tiempoI,tiempoV,steps,count)
		
	print("step 0 ended")
	count=count+1
	#plt.show()
	
	
	###############################################################
	fout=TFile(fname,"recreate")
	tupla=TNtuple("darkdata","dark current data","step:tv:ti:v:i" )
	###############################################################
	for x in range(number_steps):
	
		for step,t0,t1,v1,i1, in zip(steps,tiempoV,tiempoI,volts,amperes):
			tupla.Fill(step,t0,t1,v1,i1)			
					
		volts  = 0  
		amperes= 0  
		tiempoV= 0  
		tiempoI= 0
		steps  = 0
		
		volts  = array('d')  
		amperes= array('d')  
		tiempoV= array('d')  
		tiempoI= array('d')  
		steps  = array('d')  		
	
		volt_set = volt_set_i + x*extra_volts_per_step
		
		if volt_set >1800:	
			hv.HV_OFF(CH=0)
			volt_Set=500
			print("HV turned off, more HV than PMT can support")
		
		hv.HV_vset(CH=0, vset=volt_set)
		hv.HV_vset(CH=0, vset=volt_set)
	
			
		if y > volt_set+2 or y < volt_set-2:
			while y > volt_set+2 or y < volt_set-2:
				actual,amperes,volts,tiempoI,tiempoV,steps,y=get_data(actual,start,amperes,volts,tiempoI,tiempoV,steps,count)
				
		print("step %f fished, set voltage reached" %(count))
		count=count+1
			
		hv.HV_vset(CH=0, vset=volt_set)
		hv.HV_vset(CH=0, vset=volt_set)
		
		
		actual=time.time()-start	
		tiempo=tiempo_barrido+actual
		
		
		while actual<tiempo:
			actual,amperes,volts,tiempoI,tiempoV,steps,y=get_data(actual,start,amperes,volts,tiempoI,tiempoV,steps,count)		
			
		print("step %f finished, voltage stabilized, wave generator is now on" %(count))
		sg.GS_ON_CH1()
		count=count+1
		
		hv.HV_vset(CH=0, vset=volt_set)
		hv.HV_vset(CH=0, vset=volt_set)
		
		
		actual=time.time()-start	
		tiempo=tiempo_pulser+actual
		
		
		while actual<tiempo:
			actual,amperes,volts,tiempoI,tiempoV,steps,y=get_data(actual,start,amperes,volts,tiempoI,tiempoV,steps,count)		
			
		print("step %f finished, wave generator is now off" %(count))
		sg.GS_OFF_CH1()
		count=count+1
	for step,t0,t1,v1,i1, in zip(steps,tiempoV,tiempoI,volts,amperes):
			print(step)
			tupla.Fill(step,t0,t1,v1,i1)	
			
	fout.Write("",TObject.kOverwrite)
	fout.Close()
	
	print("terminando y apagando HV")
	hv.HV_OFF(CH=0)
		
		

def get_data(actual,start,amperes,volts,tiempoI,tiempoV,steps,count):
	actual1=time.time()-start
	imon = hv.get_HV_par(CH=0,par="IMON")
	actual2=time.time()-start
	vmon = hv.get_HV_par(CH=0,par="VMON")
		
	imon = imon.split(":")[-1].strip()
	vmon = vmon.split(":")[-1].strip()
	
	imon = imon.rstrip(imon[-1])
	vmon = vmon.rstrip(vmon[-1])
	
	#print(count)
	y=-1
	
	if imon != "O":
		y = float(imon)
		amperes.append(y)
		tiempoI.append(actual1)
	if vmon != "O":
		y = float(vmon)
		volts.append(y)
		tiempoV.append(actual2) 
		steps.append(count)	
	actual=time.time()-start
	return actual,amperes,volts,tiempoI,tiempoV,steps,y


plot_Volt_Amp()
