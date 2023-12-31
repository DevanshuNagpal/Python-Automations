#!/usr/bin/python3
from scapy.all import *
from prettytable import PrettyTable
from mac_vendor_lookup import MacLookup
from argparse import ArgumentParser
from sys import exit,stderr,argv

class NetworkScanner:
    def __init__(self,hosts):

        for host in hosts:
            self.host = host
            self.alive = {}
            self.create_packet()
            self.send_packet()
            self.get_alive()
            self.print_alive()

    def create_packet(self):
        layer1 = Ether(dst ="ff:ff:ff:ff:ff:ff")
        layer2 = ARP(pdst=self.host)

        packet = layer1 / layer2
        self.packet = packet

    def send_packet(self):
        answered, unanswered = srp(self.packet,timeout=1,verbose = False)
        if answered:
            self.answered = answered
        else:
            print("No host is up")
            sys.exit(1)

    def get_alive(self):
        for sent,recieved in self.answered:
            self.alive[recieved.psrc] = recieved.hwsrc
            
    def print_alive(self):
        table = PrettyTable(["IP", "MAC", "VENDOR"])
        for ip, mac in self.alive.items():
            try:
                vendor = MacLookup().lookup(mac)
            except:
                vendor = "Unknown"
            table.add_row([ip, mac, vendor])
        print(table)


def get_args():
    parser = ArgumentParser(description = "Network Scanner ")
    parser.add_argument("--h",dest="host",nargs="+",help = "Hosts to scan")
    arg = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    return arg.host

hosts = get_args()
NetworkScanner(hosts)




        