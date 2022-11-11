import mod.DAQULS.osci as adq
import mod.SGULS as signal
from time import sleep
import time

#fname="pmtbase_T2_noRInDynodes.root"
#fname="data_test.root"
fname="data_test.root"
odir = "raw_data/"

PWMIN=20 #pulse width in ns
#PWMAX = 120
#NPW = 5
#DPW = (PWMAX-PWMIN)/NPW
#PW = [int(PMIN + DPW*x) for x in range(NPW)]
PWs = [20, 40, 60, 80, 100, 120]

signal.configGS_ALL(signal="pulse",polarity="inverted",frec=30000,vhl=0.0,vll=-1.16,width=PWMIN)
signal.GS_ON_ALL()
sleep(2)

startc=time.time()
actualc=time.time()-startc

Ntrig = 1600
print("starting the data taking") 
k=1
for PW in PWs:
	signal.configGS_ALL(signal="pulse",polarity="inverted",frec=30000,vhl=0.0,vll=-1.16,width=PW)
	signal.GS_ON_ALL()
	sleep(0.5)
	prefix = str(PW)+"ns_"
	adq.get_data(channel="1,2,3",numero_tri=Ntrig,point_number=1000000,fname=odir + prefix+fname)
	actualc=time.time()-startc
	etc = actualc*(len(PWs)-k)/k
	print("width %f, time elapsed %f, pw point -- %d/%d, ETC: %.2f s" %(PW,actualc,k,len(PWs),etc)) 
	k+=1

actualc=time.time()-startc
print("finished total elapsed time: %.2f",actualc)
