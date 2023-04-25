import os
from time import sleep

num=2 #numero de archivos necesarios antes de que empiece a subirlos a la red pitaya
source="/home/src/datos"
files = sorted(os.listdir(source))
size=len(files)
password="xxxx"
user="xxxx"

files = sorted(os.listdir(source))
size=len(files)
if size>num:
	for x in range(size-1):
		f=files[x]
		if (f.endswith(".dat")):
			file_name="%s/%s" %(source,f)
			os.system('SSHPASS="%s" rsync --rsh="sshpass -e ssh -l %s" %s 200.16.117.76:/scratch/lago/%s' % (password,user,file_name,user))
			os.remove(file_name)

