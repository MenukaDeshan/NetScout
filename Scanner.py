#!/usr/bin/python3
#etScout is intended for educational purposes only. Scanning a network without permission is illegal and unethical. Please use this tool responsibly.
import nmap

scanner = nmap.PortScanner()

print("NMAP automation tool")
print("<----------------------------------------------------->")

ip_addr = input("Please enter the IP address you want to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)

resp = input("""\n
            ············································
            : _   _      _   ____                  _   :
            :| \ | | ___| |_/ ___|  ___ ___  _   _| |_ :
            :|  \| |/ _ \ __\___ \ / __/ _ \| | | | __|:
            :| |\  |  __/ |_ ___) | (_| (_) | |_| | |_ :
            :|_| \_|\___|\__|____/ \___\___/ \__,_|\__|:
            ············································
            :                                By D3SH4N :
            :..........................................:
             Please enter the type of scan you want to run
                1)Default Scan
                2)Default UDP Scan
                3)Full Scan \n""")

print("You have selected option: ", resp)

resp_dict={'1':['-v -sS','tcp'],'2':['-v -sU','udp'],'3':['-v -sS -sV -sC -A -O','tcp']}

if resp not in resp_dict.keys():
    print("enter a valid option")
else:
    print("nmap version: "scanner.nmap_version())
    scanner.scan(ip_addr,"1-1024",resp_dict[resp][0]) 
    print(scanner.scaninfo())
    if scanner.scaninfo()=='up':
        print("Scanner Status: ",scanner[ip_addr].state())
        print(scanner[ip_addr].all_protocols())
        #all open Ports
        print("Open Ports: ",scanner[ip_addr][resp_dict[resp][1]].keys())

