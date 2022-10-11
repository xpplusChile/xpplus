import pyvisa as visa
import time
DT_READ=0.1 #s
DT_WRITE=0.2 #s

usb_direction = "USB0::6833::3601::DP8C234806315::0::INSTR"
LV = visa.ResourceManager().open_resource(usb_direction)
print(LV.query('*IDN?').strip())

def LV_W(command):
	LV.write(command)
	time.sleep(DT_WRITE)
	
def LV_R(command):
	res=LV.query(command)
	time.sleep(DT_READ)
	return res


def LV_Conf(CH=1, volt=4, curr=2, curr_prot="NULL", volt_prot="NULL"):
	LV_W(":INST CH%i" 	% CH)
	LV_W(":CURR %.2f" 	% curr)
	LV_W(":VOLT %.2f"	% volt)
	
	if curr_prot == "NULL":
		LV_W("CURR:PROT:STAT OFF")
	else:	
		LV_W(":CURR:PROT %.2f" 	% curr_prot)
		LV_W("CURR:PROT:STAT ON")
		
	if volt_prot == "NULL":
		LV_W("VOLT:PROT:STAT OFF")
	else:
		LV_W(":VOLT:PROT %.2f" 	% volt_prot)
		LV_W("VOLT:PROT:STAT ON")
		
def LV_ON(CH=1):
	LV_W(":OUTP CH%i,ON" % CH)

def LV_ON_ALL():
	LV_W(":OUTP CH1,ON")
	LV_W(":OUTP CH2,ON")
	LV_W(":OUTP CH3,ON")
	
def LV_OFF(CH=1):
	LV_W(":OUTP CH%i,OFF" % CH)

def LV_OFF_ALL():
	LV_W(":OUTP CH1,OFF")
	LV_W(":OUTP CH2,OFF")
	LV_W(":OUTP CH3,OFF")






