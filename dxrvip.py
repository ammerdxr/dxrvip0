import socket
import sys
#this script coded by: DXR
#DXR
#Telegram(dxr01)
Red="\033[0;31m" # Red
print('Telegram dxr01 ')
print(Red+'dxr Tool developer ')
print ('Enter Your DNS Or Target: ')
hostname = input()
ip=socket.gethostbyname(hostname)
print ('Host Name Is: ',hostname, '\n' 'Target Ip Is: ',ip)

 