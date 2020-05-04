#!/usr/bin/python3
import os, threading, requests

'''q1'''
print("pid:",os.getpid())

'''q2'''
if(os.name =="posix"):
	print("loadavg:",os.getloadavg())
	
'''q3'''
load1,load5,load15 = os.getloadavg()
cpu_core=os.cpu_count()
print("5 min loadavg:",load5)
print("cpu:",cpu_core)
if (cpu_core - load5<1):
		
	'''q4'''
def url(url_array):
	response = requests.get(url_array)
	if(response.status_code==200):
		print("valid")
	elif(response.status_code==404):
		print("invalid")
		
		
thread1=threading.Thread(target=url, args=('https://api.github.com',))
thread2=threading.Thread(target=url, args=('http://bilgisayar.mu.edu.tr/',))
thread3=threading.Thread(target=url, args=('https://www.python.org/',))
thread4=threading.Thread(target=url, args=('http://akrepnalan.com/ceng2034',))
thread5=threading.Thread(target=url, args=('https://github.com/caesarsalad/wow',))

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
