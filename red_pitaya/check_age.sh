#!/bin/bash

age () { stat=$(stat --printf="%Y %F\n" "$1");days=$((($(date +%s) - ${stat%% *})/86400)) ;  }
delete_age=2

search_dir=/home/sebastian/Documents/Programas/lago/Automatizacion_lab_uls/red_pitaya/
#search_dir=/home/src/logs/
for entry in "$search_dir"/*
do
	age $entry
	if [[ $days -ge $delete_age ]];then
		echo $entry
		#rm $entry
	fi
done
