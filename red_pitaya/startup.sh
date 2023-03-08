#!/bin/sh
sleep 10
touch MASTER
sleep 1
cat /home/lago_v1_3.bit > /dev/xdevcfg
sleep 1
/home/src/lago -s t1 170
sleep 1
/home/src/lago -s t2 9000
sleep 1
/home/src/lago -s hv1 0
sleep 1
hv1_i=300
hv1_f=1300
hv1_a=$((hv1_i))

/home/src/lago -s hv1 ${hv1_i}
sleep 5
while [ $((hv1_f-1)) -ge $hv1_a ] 
do 
	hv1_a=$((hv1_a+200))
	echo $hv1_a	
	/home/src/lago -s hv1 ${hv1_a}
	sleep 50
done

/home/src/lago -s hv2 0
sleep 1 
process_id=`/bin/ps -fu $USER| grep "bin/sh /home/src/DAQ.sh" | grep -v "grep" | awk '{print $2}'`	
if [ -z "$process_id" ]
then
	echo "\$var is empty"
    minuto=$(date +%M)  
	segundo=$(date +%S) 
	tiempo_t=$((59 * 60 -minuto*60 - segundo + 58 ))
	echo "$tiempo_t"
	timeout ${tiempo_t}s /home/src/lago -f /home/src/datos/ 
	
else
      echo "\$var is NOT empty"
fi

