from scapy.all import ARP, Ether, srp


def get_hostname(ip):
    try:
        # Отправляем ARP-запрос для получения имени хоста
        arp_request = ARP(pdst=ip)
        broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_response = srp(broadcast / broadcast, timeout=1, verbose=False)[0]

        # Если получен ответ, возвращаем имя хоста
        if arp_response:
            return arp_response[0][1].psrc
    except Exception as e:
        pass

    return None


def scan_network(target_ip="192.168.2.1/24"):
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    result = srp(packet, timeout=3, verbose=False)[0]

    devices = []
    for sent, received in result:
        ip = received.psrc
        mac = received.hwsrc
        hostname = get_hostname(ip)
        devices.append({'ip': ip, 'mac': mac, 'hostname': hostname})

    return devices


if __name__ == "__main__":
    target_ip = input("Введите IP-диапазон для сканирования (например, 192.168.1.1/24): ")
    print("\nСканирование сети...")
    network_devices = scan_network(target_ip)

    print(f"\nОбнаруженные устройства:\n{'-' * 60}")
    for device in network_devices:
        print(f"{device['ip']} ({device['hostname']}) \t\t {device['mac']}")
