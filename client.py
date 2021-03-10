# proj0_c

serverPort = 12001
import threading

arrays_ip = []
arrays_id = []
arrays = []

s = input("Enter value for hashing: ")

l1 = [c for c in s]
l2 = [ord(c) for c in s]

cal = 0
for x in l2:
    cal = cal + x
print(cal % 5)

import socket


def get_Host_name_IP():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        print("Hostname :  ", host_name)
        print("IP : ", host_ip)
        # s='Grad01.acs.uwinnipeg.ca' #print(''.join(i for i in host_name if i.isdigit()))
        Host_name = ''.join(i for i in host_name if i.isdigit())
        return host_ip, Host_name
    except:
        print("Unable to get Hostname and IP")


identity = get_Host_name_IP()
print("get_Host_name_IP()", identity[0], identity[1])
identity_str = identity[0] + " " + identity[1]

arrays_id.append(identity[1])
arrays_ip.append(identity[0])


class myThread(threading.Thread):
    def __init__(self, threadIP, msg):
        threading.Thread.__init__(self)
        self.threadIP = threadIP
        self.msg = msg
        string = threadIP
        mylist = string.split('.')
        print(mylist[3])
        lstD = ''.join(i for i in mylist[3] if i.isdigit())
        self.name = int(lstD) - 20

    def run(self):
        print("\nNode IP:", self.threadIP, "Received msg: ", self.msg, "self.name", self.name)
        text = str(self.msg)
        arrays_ip.append(self.threadIP)
        text1 = ''.join(i for i in text if i.isdigit())
        arrays_id.append(text1)
        print("arrays_ip", arrays_ip)
        print("arrays_id", arrays_id)
        if len(arrays) <= 2:
            print("updating ....")
            print("New successor Node", self.name, "With IP", self.threadIP)
            IP=str(self.threadIP)
           # clientSocket.sendto(message.encode(), (IP,serverPort))
        elif len(arrays) <= 4:#
            print("updating ....")#
            print("New successor Node", "03", "With IP", "10.0.130.23")#
        if "join" in self.msg:
            cursor = arrays.index(self.msg)
            cursor = int(cursor) - 1
            print("cursor",cursor)
            #message = arrays[cursor].threadIP

            print("message in run", message)
            #clientSocket.sendto(message.encode(), clientAddress)
            clientSocket.sendto(message.encode(), (IP, serverPort))
            print("cursor", cursor)
            clientSocket.sendto(message.encode(), (IP, serverPort))

from socket import *

serverName = '10.0.130.21'
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
message = input('Input lowercase sentence:')

# message = 'join538'
clientSocket.sendto(message.encode(), (serverName, serverPort))

while True:

    # clientSocket.bind(('', serverPort))
    print('The node is waiting for response...')
    modifiedMessage, clientAddress = clientSocket.recvfrom(2048)
    print('modifiedMessage.decode()', "servertAddress", clientAddress)
    thread1 = myThread(clientAddress[0], modifiedMessage.decode())
    arrays.append(thread1)
    thread1.start()
    if len(arrays) == 1:

        print("my Successor is node", arrays[0].name, "with Ip:", arrays[0].threadIP)
        print("my Precessor is node", arrays[0].name, "with Ip:", arrays[0].threadIP)

        # modifiedMessage = message.decode().upper()
    # clientSocket.close()
    else:
        print("my Successor is node", arrays[1].name, "with Ip:", arrays[1].threadIP)
        print("my Precessor is node", arrays[0].name, "with Ip:", arrays[0].threadIP)
        print("len(arrays)", len(arrays))

        clientSocket.sendto(message.encode(), clientAddress)

        # modifiedMessage = arrays[0].threadIP
        # clientSocket.sendto(modifiedMessage.encode(), clientAddress)

    # clientSocket.close()
    # clientSocket.sendto(modifiedMessage.encode(), clientAddress)
