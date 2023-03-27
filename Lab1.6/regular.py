import glob
import re
import ipaddress

log_files = glob.glob(r'C:\\config_files\\*.log')

ip_addresses = []

# Проходимся по каждому файлу в списке
for file in log_files:
    # Открываем файл и читаем его
    with open(file, 'r') as f:
        lines = f.readlines()

        # Проходимся по каждой строке в файле
        for line in lines:
            # Ищем строку, содержащую IP-адрес
            match = re.match("^ ip address ((?:[0-9]{1,3}\\.?){4}) ((?:[0-9]{1,3}\\.?){4})$", line)

            if match:
                ip_interface = ipaddress.IPv4Interface(match.group())
                ip_addresses.append(ip_interface.ip)

ip_addresses = list(set(ip_addresses))
for ip_address in ip_addresses:
    print(ip_address)
