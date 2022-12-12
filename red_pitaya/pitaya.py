import os
from time import sleep

source="/home/src/datos"
files = sorted(os.listdir(source))
password="xxxx"
user="xxxx"
size=len(files)
while 1==1:
	if size>4:
		for x in range(size-1):
			f=files[x]
			if (f.endswith(".dat")):
				file_name="%s/%s" %(source,f)
				os.system('SSHPASS="%s" rsync --rsh="sshpass -e ssh -l %s" %s 200.16.117.76:/scratch/lago/%s' % (password,user,file_name,user))
				os.remove(file_name)
	sleep(1800)
