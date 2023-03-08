#!/bin/sh

var=$(/home/src/lago -a)
#echo $var

prefix="#Trigger Level Ch1 = 500
#Trigger Level Ch2 = 9000
#High Voltage 1    = "
foo=${var#"$prefix"}
suffix=" mV
#High Voltage 2    = 7.7 mV
#Trigger Scaler 1  = 1
#Trigger Scaler 2  = 1
#No GPS device is present or enabled
#Working mode is MASTER

Status from registers complete!"
foo=${foo%"$suffix"}

foo=${foo%\.*}
echo $foo

hv1_i=$foo
hv1_f=300
hv1_a=$((hv1_i))
rest=3

#/home/src/lago -s hv1 ${hv1_a}
sleep $rest

while [ $hv1_a -ge $((hv1_f+1)) ] 
do 
	hv1_a=$((hv1_a-200))
	echo $hv1_a	
	#/home/src/lago -s hv1 ${hv1_a}
	sleep $rest
done
hv1_a=0
echo $hv1_a
#/home/src/lago -s hv1 ${hv1_a}
sleep $rest

echo "Reiniciando" 

#shutdown -r now
