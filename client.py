from socket import *
import ssl


context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
secureSocket = context.wrap_socket(clientSocket)
sentence = input('Input sentence: ')
secureSocket.send(sentence.encode())
modifiedSentence = secureSocket.recv(1024)
print('From server: ', modifiedSentence.decode())
secureSocket.close()
