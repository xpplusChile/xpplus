#!/bin/bash

date_=$(date '+%d_%m_%Y')
hour=$(date '+%H')
day=$(date '+%d')
minute=$(date '+%M')
#var1=$(/home/src/lago -t)
var2=$(/home/src/lago -a)

####################################################################
#Check online
ping -c 1 -q google.com >&/dev/null; echo $?
printf "\n$hour:$minute\n" >> /home/src/logs/log_$date_.txt
#echo $?

if [ $? -eq 0 ]; then
    printf "\nonline\n" >> /home/src/logs/log_$date_.txt
else
    printf "\noffline\n" >> /home/src/logs/log_$date_.txt
fi

#printf "\n$var1" >> /home/src/logs/log_$date_.txt
printf "\n$var2" >> /home/src/logs/log_$date_.txt
#######################################################################
#check process
process_id=`/bin/ps -fu $USER| grep "/home/src/" | grep -v "grep" | awk '{print $2}'`      
#echo $process_id
printf "\n\nLos procesos relacionados a la adquisicion de datos son: \n" >> /home/src/logs/log_$date_.txt
#printf "123" >> /home/src/logs/log_$date_.txt
#printf "\n$process_id\n" >> /home/src/logs/log_$date_.txt
for numbers in $process_id
do
        command=$(ps -p $numbers -o command)
        prefix="COMMAND
"
        command=${command#"$prefix"}
        suffix="COMMAND"
        command=${command%"$suffix"}
        printf "\n$command" >> /home/src/logs/log_$date_.txt
        #echo $numbers
done

process_id=`/bin/ps -fu $USER| grep "/home/cron_script/" | grep -v "grep" | awk '{print $2}'`      
#echo $process_id
#printf "123" >> /home/src/logs/log_$date_.txt
#printf "\n$process_id\n" >> /home/src/logs/log_$date_.txt
for numbers in $process_id
do
        command=$(ps -p $numbers -o command)
        prefix="COMMAND
"
        command=${command#"$prefix"}
        suffix="COMMAND"
        command=${command%"$suffix"}
        printf "\n$command" >> /home/src/logs/log_$date_.txt
        #echo $numbers
done
#######################################################################
#check memory

printf "\n\nEl estado de la memoria usada por la adquisicion de datos es: \n" >$

grep="dev/root"
log=$(df -h | grep "$grep")
#dmesg -T | grep "$grep"
printf "Filesystem      Size  Used Avail Use%% \n" >> /home/src/logs/log_$date_.txt
#printf "\n" >> /home/src/logs/log_$date_.txt
echo "$log" >> /home/src/logs/log_$date_.txt

########################################################################
#Check dmesg

printf "\n\nLos mensajes generados por dmesg en el ultimo minuto son: \n" >> /home/src/logs/log_$date_.txt

if [ $minute = 0 ];then
	if [ $hour =0 ];then
		grep= "$((day-1)) 23:59"
		log=$(dmesg -T | grep "$grep")
		#dmesg -T | grep "$grep"
		printf "$log" >> /home/src/logs/log_$date_.txt
		#printf dmesg -T | grep "$grep" >> /home/src/logs/log_$date_.txt
	else	
		grep="$day $hour:59"
		log=$(dmesg -T | grep "$grep")
		#dmesg -T | grep "$grep"
		printf "$log" >> /home/src/logs/log_$date_.txt
		#printf dmesg -T | grep "$grep" >> /home/src/logs/log_$date_.txt
	fi
else
	grep="$day $hour:$((minute-1))"
 	log=$(dmesg -T | grep "$grep")
	#dmesg -T | grep "$grep"
	printf "$log" >> /home/src/logs/log_$date_.txt
	#printf dmesg -T | grep "$grep" >> /home/src/logs/log_$date_.txt

fi
printf "\n_________________________________________________________" >> /home/src/logs/log_$date_.txt



