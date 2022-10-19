import pydrs
import time
from ROOT import TNtuple,TFile,TObject,TH1D
import math

board = pydrs.get_board(0)

def info():	
	print(board.idn)

def load_waveform(CH=1,sampling=5e9,mode="on", rang=0, trig_source="ch1", trig_level=-.1,trig_pol="falling",trig_delay=150e-9):
	board.set_sampling_frequency(Hz=sampling)
	board.set_transparent_mode(mode)
	board.set_input_range(center=rang)
	board.enable_trigger(True,False) # Don't know what this line does, it was in the example `drs_exam.cpp`.
	board.set_trigger_source(trig_source)
	board.set_trigger_level(volts=trig_level)
	board.set_trigger_polarity(edge=trig_pol)
	board.set_trigger_delay(seconds=trig_delay)
	start=time.time()
	time.sleep(0.00005)
	finish=time.time()
	#print(finish-start)
	print('Waiting for trigger...')
	board.wait_for_single_trigger()
	print("signail obtained")
	waveform_data = board.get_waveform(n_channel=CH)
	
	
	t=waveform_data['Time (s)']
	v=waveform_data['Amplitude (V)']
	
	return t,v
	
def load_waveform_all(sampling=5e9,mode="on", rang=0, trig_source="ch1", trig_level=-.1,trig_pol="falling",trig_delay=150e-9):
	board.set_sampling_frequency(Hz=sampling)
	board.set_transparent_mode(mode)
	board.set_input_range(center=rang)
	board.enable_trigger(True,False) # Don't know what this line does, it was in the example `drs_exam.cpp`.
	board.set_trigger_source(trig_source)
	board.set_trigger_level(volts=trig_level)
	board.set_trigger_polarity(edge=trig_pol)
	board.set_trigger_delay(seconds=trig_delay)
	start=time.time()
	time.sleep(0.00005)
	finish=time.time()
	#print(finish-start)
	print('Waiting for trigger...')
	board.wait_for_single_trigger()
	print("signail obtained")
	waveform_data = board.get_waveform_all()
	
	
	t=waveform_data['Time (s)']
	v_1=waveform_data['Amplitude_1 (V)']
	v_2=waveform_data['Amplitude_2 (V)']
	v_3=waveform_data['Amplitude_3 (V)']
	v_4=waveform_data['Amplitude_4 (V)']
	return t,v_1,v_2,v_3,v_4
	

def get_data(channel=1,numero_tri="NULL",run_time="NULL",sampling=5e9,mode="on", rang=0, trig_source="CH1", trig_level=-0.1,trig_pol="falling",trig_delay=150e-9):
	chlist=[int(x) for x in channel.split(",")]
	#print(chlist)
	s=len(chlist)
	#print(s)
	#rint(time.time())
	
	load_data = {}
	
	sa=sampling
	mo=mode
	ra=rang
	ts=trig_source
	tl=trig_level
	tp=trig_pol
	td=trig_delay

	fout=TFile("datafile.root","recreate")
	
	if s==1:
		tupla=TNtuple("drs4data","drs4 data","evn:t:v0" )
	elif s==2:
		tupla=TNtuple("drs4data","drs4 data","evn:t:v0:v1" )
	elif s==3:
		tupla=TNtuple("drs4data","drs4 data","evn:t:v0:v1:v2" )
	else :
		tupla=TNtuple("drs4data","drs4 data","evn:t:v0:v1:v2:v3" )
	
	
	temp2=time.time()
	
	if numero_tri != "NULL":
		temp1=numero_tri
		temp2=1
		i=temp2
	elif run_time != "NULL":
		temp1=run_time+time.time()
		temp2=time.time()
		i=temp2
	else:
		temp2=1
		temp1=temp2
		i=temp2
		
	while temp2<=temp1:
	
		for chidx in chlist:
			t, v = load_waveform(CH=chidx,sampling=sa,mode=mo, rang=ra, trig_source=ts, trig_level=tl ,trig_pol=tp ,trig_delay=td)
			if 'time' not in load_data.keys():
				load_data['time'] = t
			load_data[f'CH{chidx}'] = v
		
		if s==1:
			for t0, v0 in zip(t,load_data[f'CH{1}']):
				#print(t0)
				tupla.Fill(i,t0,v0)
		elif s==2:
			for t0, v0,v1 in zip(t,load_data[f'CH{1}'],load_data[f'CH{2}']):
				tupla.Fill(i,t0,v0,v1)
		elif s==3:
			for t0, v0,v1,v2 in zip(t,load_data[f'CH{1}'],load_data[f'CH{2}'],load_data[f'CH{3}']):
				tupla.Fill(i,t0,v0,v1,v2)
		else :
			for t0, v0,v1,v2,v3 in zip(t,load_data[f'CH{1}'],load_data[f'CH{2}'],load_data[f'CH{3}'],load_data[f'CH{4}']):
				tupla.Fill(i,t0,v0,v1,v2)
	
		
		if numero_tri != "NULL":
			temp2=temp2+1
		
		elif run_time != "NULL":
			temp2=time.time()
		else:
			temp2=temp2+1
		i=temp2
		

	fout.Write("",TObject.kOverwrite)
	fout.Close()


def get_data_all(numero_tri="NULL",run_time="NULL",sampling=5e9,mode="on", rang=0, trig_source="CH1", trig_level=-0.1,trig_pol="falling",trig_delay=150e-9):
	chlist=[int(x) for x in channel.split(",")]
	#print(chlist)
	s=len(chlist)
	#print(s)
	#rint(time.time())
	
	load_data = {}
	
	sa=sampling
	mo=mode
	ra=rang
	ts=trig_source
	tl=trig_level
	tp=trig_pol
	td=trig_delay

	fout=TFile("datafile.root","recreate")
	

	tupla=TNtuple("drs4data","drs4 data","evn:t:v0:v1:v2:v3" )
	
	
	temp2=time.time()

	if numero_tri != "NULL":
		temp1=numero_tri
		temp2=1
		i=temp2
	elif run_time != "NULL":
		temp1=run_time+time.time()
		temp2=time.time()
		i=temp2
	else:
		temp2=1
		temp1=temp2
		i=temp2
		
	while temp2<=temp1:
	
		
		t, v_1,v_2,v_3,v_4 = load_waveform(CH=chidx,sampling=sa,mode=mo, rang=ra, trig_source=ts, trig_level=tl ,trig_pol=tp ,trig_delay=td)
		if 'time' not in load_data.keys():
			load_data['time'] = t
		load_data[f'CH{1}'] = v_1
		load_data[f'CH{2}'] = v_2
		load_data[f'CH{3}'] = v_3
		load_data[f'CH{4}'] = v_4
	
		for t0, v0,v1,v2,v3 in zip(t,load_data[f'CH{1}'],load_data[f'CH{2}'],load_data[f'CH{3}'],load_data[f'CH{4}']):
				tupla.Fill(i,t0,v0,v1,v2)
	
		
		if numero_tri != "NULL":
			temp2=temp2+1
		
		elif run_time != "NULL":
			temp2=time.time()
		else:
			temp2=temp2+1
		i=temp2		

	fout.Write("",TObject.kOverwrite)
	fout.Close()
