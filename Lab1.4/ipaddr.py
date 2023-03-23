# net = random.randint(0x0b000000, 0xdf000000)
# mask = random.randint(8, 24)
# ipaddress.IPv4Network((net, mask), strict=False))
# n1 = ipaddress.IPv4Network
# print(net)


import ipaddress
import random


# Класс IPv4RandomNetwork
class IPv4RandomNetwork(ipaddress.IPv4Network):
    def __init__(self):

        mask = random.randint(8, 24)

        net = random.randint(int(ipaddress.IPv4Address('11.0.0.0')), int(ipaddress.IPv4Address('223.0.0.0')))

        ipv4_network = ipaddress.IPv4Network((net, mask), strict=False)
        # создаем базовый класс
        super().__init__(ipv4_network)

    # Проверяем, является ли сеть обычной
    def regular(self):
        return (not self.is_multicast and not self.is_reserved and
                not self.is_unspecified and not self.is_loopback and
                not self.is_private)

    # Возвращаем ключ, для сортировки сетей
    def key_value(self):
        return int(self.network_address) + (self.prefixlen * 2 ** 32) # умножаем длину префикса на 2 в степени 32,
        # чтобы получить диапазон доступных адресов в этой сети.


# Генерируем случайные сети
networks = [IPv4RandomNetwork() for i in range(20)]

# Фильтруем сети для дальнейшей сортировки
regular_networks = [n for n in networks if n.regular()]

# Сортируем сети по маске, а затем по адресу
sorted_networks = sorted(regular_networks, key=IPv4RandomNetwork.key_value)

# Выводим список сетей на экран
for network in sorted_networks:
    print(network)
