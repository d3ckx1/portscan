# coding=utf-8
# auth: d3ckx1

import socket
import IPy
import sys
import threading

banner = '''


                          888                                        
                          888                                        
                          888                                        
88888b.   .d88b.  888d888 888888 .d8888b   .d8888b  8888b.  88888b.  
888 "88b d88""88b 888P"   888    88K      d88P"        "88b 888 "88b 
888  888 888  888 888     888    "Y8888b. 888      .d888888 888  888 
888 d88P Y88..88P 888     Y88b.       X88 Y88b.    888  888 888  888 
88888P"   "Y88P"  888      "Y888  88888P'  "Y8888P "Y888888 888  888 
888                                                                  
888                                                                  
888                                                                  
                                                                                          
                        code by d3ckx1
                    
    默认扫描 1-10000 端口，开放的IP端口保存在本目录下的"ip-port.txt"
                   
                python portscan.py 192.168.0.1/24

'''
print banner

def socket_port(ips):
    for port in range(0, 10000 + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.06)
            rex = sock.connect((str(ips),int(port)))
            print "[+++] "+ str(ips) + ":" + str(port) + " 端口开放 [+++]"
            files = open("ip-port.txt","a+")
            files.write(str(ips) + ":" + str(port) + "\n")
            files.close()
            sock.close()

        except:
            pass



if __name__ == '__main__':
    checkip = IPy.IP(sys.argv[1],make_net=1)
    print "[*] Hi, Boss Start IP Port Scan Work! [*]"
    print "[*] Scaning.... please wait a moment [*]"
    print '-' * 88
    for ips in checkip:
        t1 = threading.Thread(target=socket_port(ips),args=(200,220))
        t1.setDaemon(True)
        t1.start()

    print '-' * 88
    print "[*] Hi, Boss IP Port Scan Work Is Over! [*]"




