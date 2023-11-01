#!/usr/bin/python3
import sys
import socket

if len(sys.argv) == 1:
    print(f"{sys.argv} IP START(optional) END(optional)",file=sys.stderr)
    exit(1)


ip = sys.argv[1]

start = 1
end = 65535

if len(sys.argv) >=3:
    start = int(sys.argv[2])
    if len(sys.argv) >=4:
        end= int(sys.argv[3])

    
def check_port_status(port:int) -> bool:
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((ip,port))
        return True
    except (ConnectionRefusedError,socket.timeout):
        return False
    
for port in range(start,end):
    response = check_port_status(port)
    if response:
        print(f"Open Port found [{port}]")


    
