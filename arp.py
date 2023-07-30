from scapy.all import ARP, Ether, srp
from termcolor import colored
import socket

class arp_system():

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Ustawianie kolorów systemowych
        self.color_t = 'green'
        self.color_f = 'red'
        self.color_c = 'magenta'

        self.symbol_t = colored(str('+'), f'{self.color_t}')
        self.symbol_f = colored(str('-'), f'{self.color_f}')
        self.symbol_c = colored(str('<>'), f'{self.color_c}')

        # Ustawianie ustawień sieciowych
        try:
            self.my_ip = socket.gethostbyname(socket.gethostname())
        except socket.error:
            self.my_ip = None

    def arp_hosts(self, *args, **kwargs):
        super().__init__(*args, *kwargs)

        # tworzenie zapytania ARP
        arp = ARP(pdst=f'192.168.0.0/24')
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether/arp

        # wysłanie zapytania ARP i otrzymanie odpowiedzi
        result = srp(packet, timeout=3, verbose=0)[0]

        # wypisanie wyników
        print()
        print(f"[{self.symbol_c}] Devices in the network:")
        for sent, received in result:
            ip = received.psrc
            mac = received.hwsrc
            try:
                hostname = socket.gethostbyaddr(ip)[0]
                color_h = self.color_t
            except socket.herror:
                hostname = "Unknown"
                color_h = self.color_f

            hostname = colored(str(hostname), f'{color_h}')
            ip = colored(str(ip), f'{self.color_t}')
            mac = colored(str(mac), f'{self.color_t}')

            print(f"[{self.symbol_t}] ip: {ip}, hostname: {hostname}, mac: {mac}")

if __name__ == "__main__":
    system = arp_system()

    system.arp_hosts()