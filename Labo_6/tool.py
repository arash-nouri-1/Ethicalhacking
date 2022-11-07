import argparse
from scapy.all import (
    ARP,
    Ether,
    conf,
    sniff,
    srp,
    sr1,
    UDP,
    ICMP,
    IP,
    TCP,
    sr,
    wrpcap,
    rdpcap,
)
import socket


def host_discovery(target):
    """Performs a network scan by sending ARP requests range of IP addresses."""

    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=target), timeout=5)
    f = open("log.txt", "a")
    f.write("1. Host discovery \n")
    f.write("---------------------------------------- \n")
    for sent, received in ans:
        f.write(f"IP: {received.psrc} MAC: {received.hwsrc} \n")
    f.write("---------------------------------------- \n")


def port_discovery(target):
    """Performs a port discovery."""

    f = open("log.txt", "a")
    f.write("2. Port discovery \n")
    f.write("---------------------------------------- \n")
    for port in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        p = s.connect_ex((target, port))
        if p == 0:
            f.write(f"Port {port} is open \n")
        else:
            f.write(f"Port {port} is closed \n")
        s.close()
    f.write("---------------------------------------- \n")

    # Ik heb met verschillende methodes van scapy gebruikt, maar helaas kreeg ik steeds gesloten poorten
    # Hieronder zie je een voorbeeld methode die ik heb gebruikt

    # """ Performs a port scan by sending TCP SYN packets to a range of ports. """
    # for x in range(0 , 1024):
    #     packet = IP(dst=target)/TCP(dport=x,flags='S')
    #     res = sr1(packet ,timeout=0)
    #     if res == None:
    #         print(f"Port {x} is closed")
    #     elif res.haslayer(TCP):
    #         if res.getlayer(TCP).flags == 0x12:
    #             send_rst = sr(IP(dst=target)/TCP(dport=x,flags='R'),timeout=0)
    #             print(f"Port {x} is open")
    #         elif res.getlayer(TCP).flags == 0x14:
    #             print(f"Port {x} is closed")


def os_detection(target):
    """Performs a OS detection by sending a TCP SYN packet to port 80."""

    f = open("log.txt", "a")
    f.write("3. OS detection \n")
    f.write("---------------------------------------- \n")
    res = sr1(IP(dst=target) / ICMP(id=100))
    if IP in res:
        ttl = res.getlayer(IP).ttl
        if ttl == 64:
            os = "Linux"
        elif ttl == 128:
            os = "Windows"
        else:
            os = "Other"
        f.write(f"OS: {os} \n")
    f.write("---------------------------------------- \n")


def sniff_http(target):
    """Sniffs HTTP packets."""

    f = open("log.txt", "a")
    f.write("4. Sniff HTTP \n")
    f.write("------------------------------------------------------------ \n")
    f.close()
    sniff(filter="tcp port 80", prn=packet_callback, count=10)


def packet_callback(packet):
    """Shows HTTP packets."""

    f = open("log.txt", "a")
    f.write(f"{packet.summary()} \n")
    f.close()


def main():
    """Main function."""

    parser = argparse.ArgumentParser(description="Networking Tool")
    parser.add_argument("-t", "--target", help="Target IP address")
    parser.add_argument("-d", "--hostdiscovery", action="store_true", help="Host Discovery")
    parser.add_argument("-p", "--portdiscovery", action="store_true", help="Port Discovery")
    parser.add_argument("-o", "--osdetection", action="store_true", help="OS Detection")
    parser.add_argument("-c", "--pcap", action="store_true", help="Pcap")
    args = parser.parse_args()

    if args.hostdiscovery:
        host_discovery(args.target)

    if args.portdiscovery:
        port_discovery(args.target)

    if args.osdetection:
        os_detection(args.target)

    if args.pcap:
        sniff_http(args.target)

    if (
        not args.target
        or not args.hostdiscovery
        and not args.portdiscovery
        and not args.osdetection
        and not args.pcap
    ):
        user_input = 0
        while user_input != "5":
            print("Wat wil je doen? \n")
            print("1. Host discovery \n")
            print("2. Port discovery \n")
            print("3. OS detection \n")
            print("4. Pcap \n")
            print("5. Exit \n")
            user_input = input("Voer een nummer in: ")
            if user_input == "1":
                target = input("Voer een ip adres met subnet in VB:192.168.0.0/24 : ")
                host_discovery(target)
            elif user_input == "2":
                target = input("Voer een ip adres in: ")
                port_discovery(target)
            elif user_input == "3":
                target = input("Voer een ip adres in: ")
                os_detection(target)
            elif user_input == "4":
                target = input("Voer een ip adres in: ")
                sniff_http(target)
            elif user_input == "5":
                print("Tot ziens!")


if __name__ == "__main__":
    main()
