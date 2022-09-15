import usbtmc
import time

g_s =  usbtmc.Instrument(0x400 , 0x09c4)

def GS(command):
    g_s.write(command)
    time.sleep(0.2)
    

def configGS(signal="pulse", frec=24000 ,vhl= 0.5 ,vll= -0.5 ,width= 20  ,impedance=50, duty="NULL"):
	GS_OFF():
	wi=width/1000000000
	GS("func "+ str(signal) )
	GS("VOLT:UNIT VPP")
	GS("OUTP:LOAD %.1f" % impedance)
	GS("FREQ %d" % frec)
	GS("VOLT:HIGH %.1f" % vhl)	
	GS("VOLTage:LOW %.1f" % vll)
	if duty =="NULL":
		GS("PULS:WIDT %.8f" % wi)	
	if duty !="NULL":
		GS("PULSe:DCYCle %.1f" % duty )
		
		 
	GS("SYSTem:LOCal")
	

def GS_ON():
	GS("OUTP ON")
	GS("SYSTem:LOCal")

def GS_OFF():
	GS("OUTP OFF")
	GS("SYSTem:LOCal")

