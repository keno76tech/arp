from scapy.all import ARP, Ether, srp
import requests

# Interfejs, który ma być użyty do skanowania (zmień na odpowiedni interfejs)
interface = "Wi-Fi"

# Tworzymy pakiet ARP, który będzie wysyłany, aby zidentyfikować urządzenia
arp = ARP(pdst="192.168.1.0/24")

# Tworzymy pakiet Ethernet, który zawiera pakiet ARP
ether = Ether(dst="ff:ff:ff:ff:ff:ff")

# Łączymy pakiet Ethernet z pakietem ARP
packet = ether/arp

# Wysyłamy pakiet ARP i odbieramy odpowiedzi
result = srp(packet, timeout=3, verbose=0, iface=interface)[0]

# Tworzymy słownik do przechowywania wyników
devices = []

# Przetwarzamy otrzymane odpowiedzi
for sent, received in result:
    devices.append({'ip': received.psrc, 'mac': received.hwsrc})

# Pobieramy dostawcę na podstawie adresu MAC z bazy danych OUI
for device in devices:
    mac = device['mac'][:8]  # OUI to pierwsze 3 bajty adresu MAC
    response = requests.get(f"https://macvendors.com/query/{mac}")
    vendor = response.text if response.status_code == 200 else "N/A"
    device['vendor'] = vendor

# Wyświetlamy wyniki
for device in devices:
    print(f"IP Address: {device['ip']}, MAC Address: {device['mac']}, Vendor: {device['vendor']}")
