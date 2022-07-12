#!/bin/python3
from os import system
from platform import system as ostype
import socket

def extract_ip():
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        st.connect(('10.255.255.255', 1))
        IP = st.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        st.close()
    return IP

def quicktest(avoid) -> None:
	if avoid[0:2] == '10':
		if ostype() == 'Linux':
			for i in range(1, 255):
				system(f"ping -w 250 -c 2 10.0.0.{i} >> results.txt")
		else:
			for i in range(1, 255):
				system(f"ping -w 250 -n 2 10.0.0.{i} >> results.txt")
	elif avoid[0:6] == '172.16':
		if ostype() == 'Linux':
			for i in range(1, 255):
				system(f"ping -w 250 -c 2 172.16.0.{i} >> results.txt")
		else:
			for i in range(1, 255):
				system(f"ping -w 250 -n 2 172.16.0.{i} >> results.txt")
	elif avoid[0:7] == '192.168':
		if ostype() == 'Linux':
			for i in range(1, 255):
				system(f"ping -w 250 -c 2 192.168.0.{i} >> results.txt")
		else:
			for i in range(1, 255):
				system(f"ping -w 250 -n 2 192.168.0.{i} >> results.txt")
	else:
		raise ValueError("IP Address unable to be handled in this program (non-private address)")
	
def extensivetest(avoid) -> None:
	if avoid[0:2] == '10':
		if ostype() == 'Linux':
			for i in range(1, 255):
				system(f"ping -c 3 10.0.0.{i} >> results.txt")
		else:
			for i in range(1, 255):
				system(f"ping -n 3 10.0.0.{i} >> results.txt")
	elif avoid[0:6] == '172.16':
		if ostype() == 'Linux':
			for i in range(1, 255):
				system(f"ping -c 3 172.16.0.{i} >> results.txt")
		else:
			for i in range(1, 255):
				system(f"ping -n 3 172.16.0.{i} >> results.txt")
	elif avoid[0:7] == '192.168':
		if ostype() == 'Linux':
			for i in range(1, 255):
				system(f"ping -c 3 192.168.0.{i} >> results.txt")
		else:
			for i in range(1, 255):
				system(f"ping -n 3 192.168.0.{i} >> results.txt")
	else:
		raise ValueError("IP Address unable to be handled in this program (non-private address)")

