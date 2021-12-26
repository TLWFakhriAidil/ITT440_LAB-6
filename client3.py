#client code
import socket

ClientSocket = socket.socket()
host = '192.168.56.108'
port = 8888

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
print(Response)

while True:
    
    Input = 0
    Math = 0
    Do = 0
    while(Do == 0):
        Input = input('Enter 1 - Logarithmic (Log), 2 - For Square Root, 3 - For Exponential Function || 99 - For Exit : ')
        if(Input == '1'):
            Math = input('Enter the value Logarithmic (Log) : ')
            print('\n')
            Do = 1
        elif(Input == '2'):
            Math = input('Enter the value Square Root : ')
            print('\n')
            Do = 1
        elif(Input == '3'):
            Math = input('Enter the value Exponential Function : ')
            print('\n')
            Do = 1
        elif(Input != '99'):
            print('!Wrong input, try again! ')
            print('\n')
            Do = 0
        else:
            break
    print('\n')
    Choose = Input + " " + Math
    ClientSocket.send(str.encode(Choose))
    Response = ClientSocket.recv(1024)
    print(Response.decode('utf-8'))
    print('\n')
ClientSocket.close()
