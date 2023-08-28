import pyvisa as visa
import time

DT_READ = 0.4 #s
DT_WRITE = 0.4 #s

rm = visa.ResourceManager()
inst=rm.open_resource("ASRL/dev/ttyACM0::INSTR")
time.sleep(1)

def HV_Recconect():
	global rm
	global inst
	inst.close()
	time.sleep(1)
	rm = visa.ResourceManager()
	inst=rm.open_resource("ASRL/dev/ttyACM0::INSTR")
	time.sleep(1)

def HV_W(command): #write in the high voltage instrument
	inst.write(command)
	time.sleep(DT_WRITE)	
	
def HV_R(command): #read in the high voltage instrument
	res = inst.query(command)
	time.sleep(DT_READ)
	return res
		

def clear_alarm(): #clean trip
	HV_W("$CMD:SET,PAR:BDCLR")

def HV_vset(CH=0, vset=0): #set voltage
	HV_W("$CMD:SET,CH:%f,PAR:VSET,VAL:	%.2f" % (CH, vset))

#ch=canal vset=voltage set i set= current max set , r up= ramp up, ramp down= ramp down, trip= tiempo antes del trip
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
	HV_Recconect()  #importante para evitar problemas cuya razon desconosco
	
#obtiene parametro hv y lo retorna como variable 
def get_HV_par(CH=0, par = "NULL"):
	if par=="NULL":
		print("No ingreso parametro a monitorear")
		return -1111
	return HV_R("$CMD:MON,CH:%f,PAR:%s" % (CH, par)) 
		
#obtiene parametro por un tiempo y lo escribe en pantalla		
def HV_mon(CH=0, seg=DT_READ, par = "NULL"):
	i=DT_READ
	if par=="NULL":
		print("No ingreso parametro a monitorear")
	else:	
		while i <= seg:
			print(HV_R("$CMD:MON,CH:%f,PAR:%s" % (CH, par))) 
			i=i+DT_READ

		
def HV_imon_f(CH=0):
	imon = get_HV_par(CH=CH,par="IMON")
	imon = imon.split(":")[-1].strip()
	while imon=="OK" or imon=="ERR":
		imon = get_HV_par(CH=CH,par="IMON")
		imon = imon.split(":")[-1].strip()

	imon = float(imon)
	return imon
		
def HV_vmon_f(CH=0):
	vmon = get_HV_par(CH=CH,par="VMON")
	vmon = vmon.split(":")[-1].strip()
	while vmon =="OK" or vmon=="ERR":
		vmon = get_HV_par(CH=CH,par="VMON")
		vmon = vmon.split(":")[-1].strip()

	vmon = float(vmon)
	return vmon


def HV_ON(CH=0):
	status=get_HV_par(CH=0, par = "STATUS")
	status = status.split(":")[-1].strip()
	status=float(status)
	if status > pow(2,10)-4 and status < pow(2,10)+4:
		print("Ch %s kill via front and back panel" % CH)
		exit()
	if status > pow(2,12)-4 and status < pow(2,12)+4:
		print("Ch %s disabled " % CH)
		exit()
	HV_W("$CMD:SET,CH:%f,PAR:ON" % CH)
	HV_Recconect()  #importante para evitar problemas cuya razon desconosco
	
def HV_ON_ALL():
	for x in range(0,8):
		status=get_HV_par(CH=0, par = "STATUS")
		status = status.split(":")[-1].strip()
		status=float(status)
		if status > pow(2,10)-4 and status < pow(2,10)+4:
			print("Ch %s kill via front and back panel" % x)
		if status > pow(2,12)-4 and status < pow(2,12)+4:
			print("Ch %s disabled " % x)
	for x in range(0,8):
		HV_W("$CMD:SET,CH:%s,PAR:ON" % x)
		
	HV_Recconect()  #importante para evitar problemas cuya razon desconosco

		
def HV_OFF(CH=0):
	HV_W("$CMD:SET,CH:%f,PAR:OFF" % CH)
	HV_Recconect()  #importante para evitar problemas cuya razon desconosco
	
def HV_OFF_ALL():
	for x in range(0,8):
		HV_W("$CMD:SET,CH:%s,PAR:OFF" % x)
		
	HV_Recconect()  #importante para evitar problemas cuya razon desconosco



	
