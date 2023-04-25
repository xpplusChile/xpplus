#!/bin/sh

#####################################################################################################
## LOG

date_=$(date '+%d_%m_%Y')
hour=$(date '+%H')
day=$(date '+%d')
minute=$(date '+%M')

printf "\n_________________________________________________________" >> /home/src/logs/log_$date_.txt
printf "\n_________________________________________________________" >> /home/src/logs/log_$date_.txt
printf "\n_________________________________________________________" >> /home/src/logs/log_$date_.txt
printf "\n_________________________________________________________" >> /home/src/logs/log_$date_.txt

printf "\n$hour:$minute\n" >> /home/src/logs/log_$date_.txt
printf "\n SE ENCENDIO LA RED PITAYA" >> /home/src/logs/log_$date_.txt

printf "\n_________________________________________________________" >> /home/src/logs/log_$date_.txt
printf "\n_________________________________________________________" >> /home/src/logs/log_$date_.txt
printf "\n_________________________________________________________" >> /home/src/logs/log_$date_.txt
printf "\n_________________________________________________________" >> /home/src/logs/log_$date_.txt

#####################################################################################################
## startup

hv1_i=300
hv1_f=1300
t1=1000
hv1_a=$((hv1_i))

sleep 10
touch MASTER
sleep 1
cat /home/src/lago_v1_2.bit > /dev/xdevcfg
sleep 1
/home/src/lago -s t1 ${t1}
sleep 1
/home/src/lago -s t2 9000
sleep 1
/home/src/lago -s hv1 0
sleep 1

/home/src/lago -s hv1 ${hv1_i}
sleep 5
while [ $((hv1_f-1)) -ge $hv1_a ] 
do 
	hv1_a=$((hv1_a+200))
	echo $hv1_a	
	/home/src/lago -s hv1 ${hv1_a}
	sleep 10
done
/home/src/lago -s hv1 ${hv1_f}
sleep 10
	
/home/src/lago -s hv2 0
sleep 1 
#timeout 60s /home/src/lago -f /home/src/datos/hv1_${hv1_f}_t1_${t1}
/home/src/lago -f /home/src/datos/hv1_${hv1_f}_t1_${t1}

	
