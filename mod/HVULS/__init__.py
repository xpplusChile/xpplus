import pyvisa as visa
import time

DT_READ = 0.4 #s
DT_WRITE = 0.2 #s

rm = visa.ResourceManager()
inst=rm.open_resource("ASRL/dev/ttyACM0::INSTR")
time.sleep(3)

def HV_W(command):
	inst.write(command)
	time.sleep(DT_WRITE)	
	
def HV_R(command):
	res = inst.query(command)
	time.sleep(DT_READ)
	return res
		


def HV_CH0(vset=1700, iset=400 , rup=30 , rdown=50 , trip= 2  ,imonrange="high", powerdown="kill"):
	HV_W("$CMD:SET,CH:0,PAR:VSET,VAL:	%.2f" % vset)
	HV_W("$CMD:SET,CH:0,PAR:ISET,VAL:	%.2f" % iset)
	HV_W("$CMD:SET,CH:0,PAR:RUP,VAL: 	%.2f" % rup)
	HV_W("$CMD:SET,CH:0,PAR:RDW,VAL:	%.2f" %rdown)
	HV_W("$CMD:SET,CH:0,PAR:TRIP,VAL:	%.2f" %trip)
	
	if imonrange=="high":
		HV_W("$CMD:SET,CH:0,PAR:IMRANGE,VAL:HIGH")
	elif imonrange=="low":
		HV_W("$CMD:SET,CH:0,PAR:IMRANGE,VAL:LOW")
	else:
		print("No se cambio IMON range")
	
	if powerdown=="kill":
		HV_W("$CMD:SET,CH:0,PAR:PDWN,VAL:KILL")
	elif powerdown=="ramp":
		HV_W("$CMD:SET,CH:0,PAR:PDWN,VAL:RAMP ")
	else:
		print("No se cambio Power down")
		

def get_HV_par(CH=0, par = "NULL"):
	if par=="NULL":
		print("No ingreso parametro a monitorear")
		return -1111
	return HV_R("$CMD:MON,CH:%f,PAR:%s" % (CH, par)) 
		
		
def HV_mon(CH=0, seg=DT_READ, par = "NULL"):
	i=DT_READ
	if par=="NULL":
		print("No ingreso parametro a monitorear")
	else:	
		while i <= seg:
			print(HV_R("$CMD:MON,CH:%f,PAR:%s" % (CH, par))) 
			i=i+DT_READ

		
		
def HV_ON(CH=0):
	HV_W("$CMD:SET,CH:%f,PAR:ON" % CH)

def HV_ON_ALL():
	HV_W("$CMD:SET,CH:0,PAR:ON")
	HV_W("$CMD:SET,CH:1,PAR:ON")
	HV_W("$CMD:SET,CH:2,PAR:ON")
	HV_W("$CMD:SET,CH:3,PAR:ON")


		
def HV_OFF(CH=0):
	HV_W("$CMD:SET,CH:%f,PAR:OFF" % CH)

def HV_OFF_ALL():
	HV_W("$CMD:SET,CH:0,PAR:OFF")
	HV_W("$CMD:SET,CH:1,PAR:OFF")
	HV_W("$CMD:SET,CH:2,PAR:OFF")
	HV_W("$CMD:SET,CH:3,PAR:OFF")


