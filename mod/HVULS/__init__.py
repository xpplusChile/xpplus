import pyvisa as visa
import time

DT_READ = 0.2 #s
DT_WRITE = 0.2 #s

rm = visa.ResourceManager()
inst=rm.open_resource("ASRL/dev/ttyACM0::INSTR")
time.sleep(1)

def HV_W(command):
	inst.write(command)
	time.sleep(DT_WRITE)	
	
def HV_R(command):
	res = inst.query(command)
	time.sleep(DT_READ)
	return res
		


def HV_Conf(CH=0, vset=0, iset=0 , rup=30 , rdown=50 , trip= 2  ,imonrange="high", powerdown="kill"):
	HV_W("$CMD:SET,CH:%f,PAR:VSET,VAL:	%.2f" % (CH, vset))
	HV_W("$CMD:SET,CH:%f,PAR:ISET,VAL:	%.2f" % (CH, iset))
	HV_W("$CMD:SET,CH:%f,PAR:RUP,VAL: 	%.2f" % (CH, rup))
	HV_W("$CMD:SET,CH:%f,PAR:RDW,VAL:	%.2f" % (CH, rdown))
	HV_W("$CMD:SET,CH:%f,PAR:TRIP,VAL:	%.2f" % (CH, trip))
	
	if imonrange=="high":
		HV_W("$CMD:SET,CH:%f,PAR:IMRANGE,VAL:HIGH" % CH)
	elif imonrange=="low":
		HV_W("$CMD:SET,CH:%f,PAR:IMRANGE,VAL:LOW"  % CH)
	else:
		print("No se cambio IMON range")
	
	if powerdown=="kill":
		HV_W("$CMD:SET,CH:%f,PAR:PDWN,VAL:KILL" % CH)
	elif powerdown=="ramp":
		HV_W("$CMD:SET,CH:%f,PAR:PDWN,VAL:RAMP" % CH)
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

def HV_imon_f(CH=0):
	imon = hv.get_HV_par(CH=CH,par="IMON")
	imon = imon.split(":")[-1].strip()
	imon = imon.rstrip(imon[-1])
	
	while imon=="O":
		imon = hv.get_HV_par(CH=CH,par="IMON")
		
		imon = imon.split(":")[-1].strip()
		imon = imon.rstrip(imon[-1])

	imon = float(imon)
	return imon
		
def HV_vmon_f(CH=0):
	vmon = hv.get_HV_par(CH=CH,par="VMON")
	vmon = vmon.split(":")[-1].strip()
	vmon = vmon.rstrip(vmon[-1])

	while vmon =="O":
		vmon = hv.get_HV_par(CH=CH,par="VMON")
		
		vmon = vmon.split(":")[-1].strip()
		vmon = vmon.rstrip(vmon[-1])

	vmon = float(vmon)
	return vmon		
		
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

