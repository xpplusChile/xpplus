import csv
import os
from datetime import datetime
import random
import time

def random_array():
	i=[0]*25
	for x in range(25):
		i[x]=random.randint(0,9)
	return i


def create_dir():
	now = datetime.now()
 
	#print("now =", now)

	# dd/mm/YY H:M:S
	dt_string = now.strftime("%d/%m/%Y %H:%M:%S") 
	directory=now.strftime("%d|%m|%Y")
	parent_dir="/home/particulas/Desktop/prueba_mover/source"
	path = os.path.join(parent_dir, directory)
	try: 
		os.mkdir(path) 
	except OSError as error: 
		print(error)
	
	#print("Directory location=",parent_dir)		  
	#print("Directory name=", directory)	
	return directory

def csv_file():
	header=["numeros_aleatorios"]
	now = datetime.now()
	file_name = now.strftime("%H:%M:%S") 
	data=random_array()
	with open( file_name, 'w', encoding='UTF8') as f:
		writer = csv.writer(f)

		# write the header
		writer.writerow(header)

		# write the data
		for x in zip(data):
			writer.writerow(x)
	return file_name

def move_file(file_name="algo",directory=""):
	d=directory
	f=file_name
	source="/home/particulas/Desktop/Scrips/%s" % f
	#print(source)
	destin="/home/particulas/Desktop/prueba_mover/source/%s/%s" % (d,f)
	#print(destin)
	os.rename(source, destin)
		
def move_dir(directory=""):
	d=directory
	source="/home/particulas/Desktop/prueba_mover/source/%s" % d
	#print(source)
	destin="/home/particulas/Desktop/prueba_mover/destination/%s" % d
	os.rename(source, destin)


	
directory=create_dir()
print(directory)
for x in range(60):
	file_name=csv_file()
	move_file(file_name=file_name,directory=directory)
	time.sleep(60)
move_dir(directory=directory)


    
    
#os.rename('old_directory/test_file.txt', 'new_directory/test_file.txt')
