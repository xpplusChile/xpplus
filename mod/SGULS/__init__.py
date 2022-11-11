import usbtmc
import time

g_s =  usbtmc.Instrument(0x400 , 0x09c4)



def GS(command):
    g_s.write(command)
    time.sleep(0.1)
    

def configGS_CH1(signal="pulse",polarity="inverted", frec=24000 ,vhl= 0.5 ,vll= -0.5 ,width="NULL"  ,impedance=50, duty="NULL"):
	GS_OFF_CH1()
	
	vamp=vhl-vll
	
	GS("OUTP:POL %s" % polarity)
	GS("func "+ str(signal))
	GS("VOLT:UNIT VPP")
	GS("OUTP:LOAD %.3f" % impedance)
	GS("FREQ %d" % frec)
	GS("VOLT %.3f" % vamp)
	GS("VOLT:HIGH %.3f" % vhl)	
	GS("VOLTage:LOW %.3f" % vll)
	if width !="NULL":
		wi=width/1000000000
		GS("PULS:WIDT %.9f" % wi)	
	if duty  !="NULL":
		GS("PULSe:DCYCle %.3f" % duty )
		
		 
	GS("SYSTem:LOCal")
	
def configGS_CH2(signal="pulse",polarity="norm", frec=24000 ,vhl= 0.5 ,vll= -0.5 ,width="NULL"  ,impedance=50, duty="NULL"):
	GS_OFF_CH2()
	
	vamp=vhl-vll
	
	GS("OUTP:POL:CH2 %s" % polarity)
	GS("func:CH2 "+ str(signal) )
	GS("VOLT:UNIT:CH2 VPP")
	GS("OUTP:LOAD:CH2 %.3f" % impedance)
	GS("FREQ:CH2 %d" % frec)
	GS("VOLT %.3f" % vamp)
	GS("VOLT:HIGH:CH2 %.3f" % vhl)	
	GS("VOLTage:LOW:CH2 %.3f" % vll)
	if width !="NULL":
		wi=width/1000000000
		GS("PULS:WIDT %.9f" % wi)	
	if duty  !="NULL":
		GS("PULSe:DCYCle %.3f" % duty )
		
		 
	GS("SYSTem:LOCal")
	
	
def configGS_ALL(signal="pulse",polarity="norm", frec=24000 ,vhl= 0.5 ,vll= -0.5 ,width="NULL"  ,impedance=50, duty="NULL"):
	GS_OFF_ALL()
		
	vamp=vhl-vll	
	
	GS("OUTP:POL %s" % polarity)
	GS("OUTP:POL:CH2 %s" % polarity)
	
	GS("func "+ str(signal) )
	GS("func:CH2 "+ str(signal) )
	
	GS("VOLT:UNIT VPP")
	GS("VOLT:UNIT:CH2 VPP")
	
	GS("OUTP:LOAD %.3f" % impedance)
	GS("OUTP:LOAD:CH2 %.3f" % impedance)
	
	GS("FREQ %d" % frec)
	GS("FREQ:CH2 %d" % frec)
	
	GS("VOLT %.3f" % vamp)
	GS("VOLT:CH2 %.3f" % vamp)
	
	GS("VOLT:HIGH %.3f" % vhl)	
	GS("VOLT:HIGH:CH2 %.3f" % vhl)	
	
	GS("VOLTage:LOW %.3f" % vll)
	GS("VOLTage:LOW:CH2 %.3f" % vll)
	
	if width !="NULL":
		wi=width/1000000000
		GS("PULS:WIDT %.9f" % wi)	
		GS("PULS:WIDT:CH2 %.9f" % wi)	
		
	if duty !="NULL":
		GS("PULSe:DCYCle %.3f" % duty )
		GS("PULSe:DCYCle:CH2 %.3f" % duty )
		 
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
	
