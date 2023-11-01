#!/usr/bin/python3

from argparse import ArgumentParser
import socket
from threading import Thread

from time import time

open_ports =[]

def prepare_args():
    """prepare arguments

        return:
            args(argparse.Namespace)
    
    """
    parser = ArgumentParser(description="Python based fast port Scanner" , usage ="%(prog)s 193.168.2.1",epilog="Example - %(prog)s -s 20 -e 40000 -t 500 -V 192.168.2.1")
    
    parser.add_argument(metavar="IPv4",dest = "ip",help="host to scan")
    parser.add_argument("-s","--start",type = int,metavar="",help="starting Port",default=1)
    parser.add_argument("-e","--end",dest="end",type=int,metavar="",help="ending port",default=65535)
    parser.add_argument("-t","--threads",dest="threads",metavar="",type=int,help="threads to use",default=500)
    parser.add_argument("-V","--vebose",dest="verbose",action="store_true",help="verbose output")
    parser.add_argument("-v","--version",action="version",version="%(prog)s 1.0",help="display version")
    args=parser.parse_args()    
    return args
    
def prepare_ports(start:int,end:int):
    """generator function for ports

    Args:
        start (int): starting port
        end (int): ending port
    """
    for port in range(start,end+1):
        yield port
        

def prepare_threads(threads:int):
    """create, start  ad join threads
    

    Args:
        threads (int): number of threads to use
    """
    
    thread_list = []
    for _ in range(threads +1):
        thread_list.append(Thread(target=scan_port))
    
    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()
        
        
def scan_port():
    """Scan ports
    """
    while True:
        try:
            s = socket.socket()
            s.settimeout(1)
            port = next(ports)
            s.connect((arguments.ip,port))
            open_ports.append(port)
            if arguments.verbose:
                print(f"\r{open_ports}",end="")
        except (ConnectionRefusedError,socket.timeout):
            continue
        except StopIteration:
            break

if __name__ == "__main__": 
    arguments= prepare_args()
    ports = prepare_ports(arguments.start,arguments.end)
    start_time =time()
    prepare_threads(arguments.threads)    
    end_time = time()
    if arguments.verbose:
        print()
    
    print(f"Open Ports found - {open_ports}")
    print(f"Time Taken - {round(end_time - start_time) }")
    