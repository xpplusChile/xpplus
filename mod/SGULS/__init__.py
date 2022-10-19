import usbtmc
import time

g_s =  usbtmc.Instrument(0x400 , 0x09c4)



def GS(command):
    g_s.write(command)
    time.sleep(0.1)
    

def configGS_CH1(signal="pulse", frec=24000 ,vhl= 0.5 ,vll= -0.5 ,width="NULL"  ,impedance=50, duty="NULL"):
	GS_OFF_CH1()
	
	GS("func "+ str(signal))
	GS("VOLT:UNIT VPP")
	GS("OUTP:LOAD %.1f" % impedance)
	GS("FREQ %d" % frec)
	GS("VOLT:HIGH %.1f" % vhl)	
	GS("VOLTage:LOW %.1f" % vll)
	if width !="NULL":
		wi=width/1000000000
		GS("PULS:WIDT %.8f" % wi)	
	if duty  !="NULL":
		GS("PULSe:DCYCle %.1f" % duty )
		
		 
	GS("SYSTem:LOCal")
	
def configGS_CH2(signal="pulse", frec=24000 ,vhl= 0.5 ,vll= -0.5 ,width="NULL"  ,impedance=50, duty="NULL"):
	GS_OFF_CH2()
	
	GS("func:CH2 "+ str(signal) )
	GS("VOLT:UNIT:CH2 VPP")
	GS("OUTP:LOAD:CH2 %.1f" % impedance)
	GS("FREQ:CH2 %d" % frec)
	GS("VOLT:HIGH:CH2 %.1f" % vhl)	
	GS("VOLTage:LOW:CH2 %.1f" % vll)
	if width !="NULL":
		wi=width/1000000000
		GS("PULS:WIDT %.8f" % wi)	
	if duty  !="NULL":
		GS("PULSe:DCYCle %.1f" % duty )
		
		 
	GS("SYSTem:LOCal")
	
	
def configGS_ALL(signal="pulse", frec=24000 ,vhl= 0.5 ,vll= -0.5 ,width="NULL"  ,impedance=50, duty="NULL"):
	GS_OFF_ALL()
		
	GS("func "+ str(signal) )
	GS("func:CH2 "+ str(signal) )
	
	GS("VOLT:UNIT VPP")
	GS("VOLT:UNIT:CH2 VPP")
	
	GS("OUTP:LOAD %.1f" % impedance)
	GS("OUTP:LOAD:CH2 %.1f" % impedance)
	
	GS("FREQ %d" % frec)
	GS("FREQ:CH2 %d" % frec)
	
	GS("VOLT:HIGH %.1f" % vhl)	
	GS("VOLT:HIGH:CH2 %.1f" % vhl)	
	
	GS("VOLTage:LOW %.1f" % vll)
	GS("VOLTage:LOW:CH2 %.1f" % vll)
	
	if duty !="NULL":
		wi=width/1000000000
		GS("PULS:WIDT %.8f" % wi)	
		GS("PULS:WIDT:CH2 %.8f" % wi)	
		
	if duty !="NULL":
		GS("PULSe:DCYCle %.1f" % duty )
		GS("PULSe:DCYCle:CH2 %.1f" % duty )
		 
	GS("SYSTem:LOCal")
	
	
	
def GS_ON_ALL():
	GS("OUTP ON")
	GS("OUTP:CH2 ON")
	GS("SYSTem:LOCal")


def GS_OFF_ALL():
	GS("OUTP OFF")
	GS("OUTP:CH2 OFF")
	GS("SYSTem:LOCal")

def GS_ON_CH1():
	GS("OUTP ON")
	GS("SYSTem:LOCal")

def GS_OFF_CH1():
	GS("OUTP OFF")
	GS("SYSTem:LOCal")
	
def GS_ON_CH2():
	GS("OUTP:CH2 ON")
	GS("SYSTem:LOCal")

def GS_OFF_CH2():
	GS("OUTP:CH2 OFF")
	GS("SYSTem:LOCal")
	
