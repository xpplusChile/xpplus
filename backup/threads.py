import threading
import mod.SGULS as sg
import mod.DAQULS.drs4 as drs
import time

def print_cube(num):
    sg.configGS_CH1(signal="sin",frec=12000000,vhl=0.4,vll=-0.4)
    for x in range(9):
        sg.GS_ON_CH1()
        sg.GS_OFF_CH1()
        time.sleep(10)
        print("dentro sg")
 
def print_square(num):
    # function to print square of given num
    print("dentro drs" )
    drs.get_data(channel="1",run_time=40)
    print("fin drs")
 
   
 
if __name__ =="__main__":
	# creating threa
	t1 = threading.Thread(target=print_square, args=(10,))
	t2 = threading.Thread(target=print_cube, args=(10,))
	print("inicio todo")
    # starting thread 1
	t1.start()
    # starting thread 2
	t2.start()
	
    # wait until thread 1 is completely executed
	t1.join()
    # wait until thread 2 is completely executed
	t2.join()
	print("fin todo")
    # both threads completely executed
	print("Done!")
