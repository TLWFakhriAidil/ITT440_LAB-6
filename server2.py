#code server
import socket
import sys
import time
import errno
import math
from multiprocessing import Process

def calcLog(Math):
	Math = int(Math)
	try:
		Total = math.log(Math)
	except:
		Total = "Enter other number"

	return Total

def calcSqrt(Math):
	Math = int(Math)
	if(Math >= 0):
		try:
			Total = math.sqrt(Math)
		except:
			Total = "Enter other number"
	else:
		Total = "You enter negatif number"

	return Total

def calcExp(Math):
	Math = float(Math)
	try:
		Total = math.exp(Math)
	except:
		Total = "Enter other number"

	return Total
    
def process_start(s_sock):
    s_sock.send(str.encode('Welcome to the Server\n'))
    while True:
        data = s_sock.recv(2048)
        print(data)
        data = data.decode('utf-8')
        try:
            Input, Math = data.split(" ", 2)
        except:
            print("Unable to calculate")
        if not data:
            break
        if(Input == '1'): #for logartithm
            Total = calcLog(Math)
        elif(Input == '2'): #For Square Root 
            Total = calcLog(Math)
        else: #Exponential Function
            Total = calcLog(Math)
        message = "[*] The answer is  %s." % str(Total)
        s_sock.send(str.encode(message))
    s_sock.close()

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8888))
    print("listening...")
    s.listen(3)
    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,))
                p.start()

            except socket.error:

                print('got a socket error')

    except Exception as e:
        print('an exception occurred!')
        print(e)
        sys.exit(1)
    finally:
           s.close()
