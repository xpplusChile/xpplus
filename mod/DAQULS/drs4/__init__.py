import pydrs
import time
from ROOT import TNtuple,TFile,TObject,TH1D
import math

board = pydrs.get_board(0)

def info():	
	print(board.idn)
	
		
def wait_trigger():	
	time.sleep(0.0001)
	print('Waiting for trigger...')
	board.wait_for_single_trigger()
	print("signal received")

def conf_waveform(sampling=5e9,mode="on", rang=0, trig_source="ch1", trig_level=-.1,trig_pol="falling",trig_delay=150e-9):
	board.set_sampling_frequency(Hz=sampling)
	board.set_transparent_mode(mode)
	board.set_input_range(center=rang)
	board.enable_trigger(True,False) # Don't know what this line does, it was in the example `drs_exam.cpp`.
	board.set_trigger_source(trig_source)
	board.set_trigger_level(volts=trig_level)
	board.set_trigger_polarity(edge=trig_pol)
	board.set_trigger_delay(seconds=trig_delay)

def load_waveform(CH=1, wait_trig="OFF"):
	
	
	if wait_trig == "OFF":
		board.transfer()
	
	elif wait_trig == "ON": 
		time.sleep(0.0001)
		print('Waiting for trigger...')
		board.wait_for_single_trigger()
		print("signail obtained")
	else:
		print("variable wait_trig erronea")
	waveform_data = board.get_waveform(n_channel=CH)
	
	
	t=waveform_data['Time (s)']
	v=waveform_data['Amplitude (V)']
	
	return t,v
	



def get_data(channel="1",numero_tri="NULL",run_time="NULL",trigger_time="NULL"):
	temp0=time.time()
	temp2=time.time()
	
	chlist=[int(x) for x in channel.split(",")]
	#print(chlist)
	s=len(chlist)
	#print(s)
	#rint(time.time())
	
	load_data = {}
	
	
	fout=TFile("datafile.root","recreate")
	
	if s==1:
		tupla=TNtuple("drs4data","drs4 data","evn:evn_time:t:v0" )
	elif s==2:
		tupla=TNtuple("drs4data","drs4 data","evn:evn_time:t:v0:v1" )
	elif s==3:
		tupla=TNtuple("drs4data","drs4 data","evn:evn_time:t:v0:v1:v2" )
	else :
		tupla=TNtuple("drs4data","drs4 data","evn:evn_time:t:v0:v1:v2:v3" )
		
	
	if numero_tri != "NULL":
		temp1=numero_tri
		temp2=1
	elif run_time != "NULL":
		temp1=run_time+time.time()
		temp2=time.time()
	else:
		temp2=1
		temp1=temp2
	
	ii=0
	while temp2<=temp1:
		
			
		print('Waiting for trigger...')
		board.wait_for_single_trigger()
		print("signail obtained")
		
		if trigger_time!="NULL":
			temp4=time.time()
			temp5=temp4+trigger_time
		else:
			temp4=1
			temp5=2


		while temp4 <temp5 :
		
			board.transfer()
			
			if numero_tri != "NULL":
				i=temp2
				temp2=temp2+1
			elif run_time != "NULL":
				temp2=time.time()
				i=temp2-temp0
			else:
				i=temp2
				temp2=temp2+1
				
				
			for chidx in chlist:
				t, v = load_waveform(CH=chidx)
				if 'time' not in load_data.keys():
					load_data['time'] = t
				load_data[f'CH{chidx}'] = v


			if s==1:
				for t0, v0 in zip(t,load_data[f'CH{1}']):
					#print(t0)
					tupla.Fill(i,t0,v0)
			elif s==2:
				for t0, v0,v1 in zip(t,load_data[f'CH{1}'],load_data[f'CH{2}']):
					tupla.Fill(ii,i,t0,v0,v1)
			elif s==3:
				for t0, v0,v1,v2 in zip(t,load_data[f'CH{1}'],load_data[f'CH{2}'],load_data[f'CH{3}']):
					tupla.Fill(ii,i,t0,v0,v1,v2)
			else :
				for t0, v0,v1,v2,v3 in zip(t,load_data[f'CH{1}'],load_data[f'CH{2}'],load_data[f'CH{3}'],load_data[f'CH{4}']):
					tupla.Fill(ii,i,t0,v0,v1,v2)

			ii=ii+1
			if trigger_time!="NULL":
				temp4=time.time()
			else:
				temp4=2
			
	fout.Write("",TObject.kOverwrite)
	fout.Close()

