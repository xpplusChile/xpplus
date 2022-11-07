import time
import mod.SGULS as signal
import numpy as np 
import matplotlib.pyplot as plt
#import pydrs
import mod.DAQULS.drs4 as drs4
print("Empezo")


signal.configGS_ALL(signal="pulse",frec=2000,vhl=0,vll=-0.8,duty=99.999)
#signal.configGS_CH2(signal="sin",frec=12000000,vhl=0.5,vll=-0.5)
signal.GS_ON_ALL()

#signal.configGS_CH1()

drs4.conf_waveform(sampling=5e9,mode="on", rang=0, trig_source="ch1", trig_level=-.028,trig_pol="falling",trig_delay=150e-9)

"""
s=time.time()
a=s
for x in range(0):
	time.sleep(10)
	a=time.time()-s
	print(a)
"""
t,v1=drs4.load_waveform(CH=1,wait_trig="ON")
t,v2=drs4.load_waveform(CH=2,wait_trig="ON")
t,v3=drs4.load_waveform(CH=3,wait_trig="ON")
t,v4=drs4.load_waveform(CH=4,wait_trig="ON")



drs4.get_data(channel="1,2",numero_tri="NULL",run_time="NULL",trigger_time=5)

#board = pydrs.get_board(0) 
#t=board.transfer()

if 2==1:
	plt.plot(t,v1)
	plt.show()

	plt.plot(t,v2)
	plt.show()

	plt.plot(t,v3)
	plt.show()

	plt.plot(t,v4)
	plt.show()
#print(t)

