#!/bin/sh

process_id=`/bin/ps -fu $USER| grep "bin/sh /home/src/startup.sh" | grep -v "grep" | awk '{print $2}'`	
if [ -z "$process_id" ]
then
	#echo "\$var is empty"
	timeout 1h /home/src/lago -f /home/src/datos/	
else
    #echo "\$var is NOT empty"
fi


