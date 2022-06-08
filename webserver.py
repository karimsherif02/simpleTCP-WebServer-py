#import socket module
from socket import * 
serverPort=6789
serverSocket = socket(AF_INET, SOCK_STREAM) #ipv4 w tcp creating socket
print("socket created")
#Prepare a sever socket
#Fill in start
serverSocket.bind(("127.0.0.1",serverPort))# bind ip and port no
serverSocket.listen(1) #one connection at a time
print ("the web server is up on port:",serverPort)
print("waiting for connections....")
#Fill in end

while True:

 #Establish the connection
    print ("Ready to serve...")
    connectionSocket, addr =serverSocket.accept()
    print("connection complete between cilent and server")
    try:
        message = connectionSocket.recv(1024)
        print("\nMESSAGE:\n", message)
        filename = message.split()[1] 
        print("\FILE NAME:\n", filename)
        f = open(filename[1:]) 
    #Send one HTTP header line into socket
        connectionSocket.send(b"\nHTTP/1.1 200 OK\n")
        connectionSocket.send(b"Content-type: text/html\r\n")
        outputdata = f.read()
    #Send the content of the requested file to the client
        for i in range(0, len(outputdata)): 
            connectionSocket.send(bytes(outputdata[i], "UTF-8"))
        connectionSocket.close()
    except IOError:
 #Send response message for file not found
        connectionSocket.send(bytes("HTTP/1.1 404 Not Found\r\n\r\n", "UTF-8"))
        connectionSocket.send(bytes("<html><head></head><body><h1>405 not found</h1></body></html>", "UTF-8"))
        connectionSocket.close()
serverSocket.close() 
