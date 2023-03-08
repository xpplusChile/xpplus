#!/bin/sh

process_id=`/bin/ps -fu $USER| grep "bin/sh /home/src/startup.sh" | grep -v "grep" | awk '{print $2}'`	
if [ -z "$process_id" ]

hour=$(date +%H)
trigger=$((hour*100))
#/home/src/lago -s t1 ${trigger}
echo $trigger
then
	echo "\$var is empty"
	#timeout 1h /home/src/lago -f /home/src/datos/	
else
    echo "\$var is NOT empty"
fi




