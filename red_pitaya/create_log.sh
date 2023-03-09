#!/bin/bash

date_=$(date '+%d_%m_%Y')
hour=$(date '+%H:%M')
#var1=$(/home/src/lago -t)
var2=$(/home/src/lago -a)
ping -c 1 -q google.com >&/dev/null; echo $?
printf "\n$hour\n" >> /home/src/logs/log_$date_.txt
#echo $?

if [ $? -eq 0 ]; then
    printf "\nonline\n" >> /home/src/logs/log_$date_.txt
else
    printf "\noffline\n" >> /home/src/logs/log_$date_.txt
fi

#printf "\n$var1" >> /home/src/logs/log_$date_.txt
printf "\n$var2" >> /home/src/logs/log_$date_.txt

process_id=`/bin/ps -fu $USER| grep "/home/src/" | grep -v "grep" | awk '{print $2}'`      
#echo $process_id
printf "\n\nLos procesos relacionados a la adquisicion de datos son \n" >> /home/src/logs/log_$date_.txt
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



printf "\n_________________________________________________________" >> /home/src/logs/log_$date_.txt



