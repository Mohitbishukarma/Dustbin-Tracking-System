import serial
import time
import datetime

print("Start")  
port="COM5"         #This will be different for various devices and on windows it will probably be a COM port.
try:
	bluetooth=serial.Serial(port, 9600)#Start communications with the bluetooth unit
	print("Connected")

except Exception as exp:
	print(f"Error while connecting, {exit}")
	exit()

bluetooth.flushInput() #This gives the bluetooth a little kick

# if connected sucessfully
if bluetooth:
	bluetooth.write(b"connected")
	time.sleep(0.1)

while True:
	if bluetooth.readline().decode("ascii").replace("\n","").strip() != "NOTFULL":
		code, status = bluetooth.readline().decode("ascii").replace('\n','').strip().split(' ')
		# CALCULATE TIME
		now = datetime.datetime.now()
		time_of_full = now.strftime("%H:%M:%S")
		with open('data.txt', encoding="utf-8", mode="w") as data_file:
			data_file.write(f"{code},{status},{time_of_full}")
			data_file.write('\n')
		print(f"{code},{status},{time_of_full}")
	else:
		with open('data.txt', encoding="utf-8", mode="w") as data_file:
			data_file.write("NOT FULL")
			data_file.write('\n')
		print(f"{code},{status},{time_of_full}")
		


# bluetooth.close() #Otherwise the connection will remain open until a timeout which ties up the /dev/thingamabob
# print("Done")0kooiu08y8y9yh98yuy