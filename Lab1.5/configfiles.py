import glob

# Указываем путь к каталогу с файлами
directory = 'C:\\config_files\\*.log'

# Создаем пустой список, в который будем добавлять найденные IP-адреса
ip_addresses = []

# Проходимся по всем файлам с расширением .log в каталоге и находим те, которые имеют расширение .log
for filename in glob.glob(directory):
    # Открываем файл на чтение и считываем его содержимое
    with open(filename, 'r') as f:
        file_contents = f.readlines()
        # Проходимся по каждой строке в файле
        for line in file_contents:
            # Если строка содержит "ip address", то добавляем найденный IP-адрес и маску подсети в список ip_addresses
            if 'ip address' in line:
                # Разбиваем строку на элементы по пробелам
                line_elements = line.split()
                # Если в списке меньше двух элементов, то пропускаем эту строку и переходим к следующей
                if len(line_elements) < 4:
                    continue
                ip_address, subnet_mask = line_elements[2:4]
                ip_addresses.append((ip_address, subnet_mask))

# Избавляемся от дублирующихся IP-адресов с помощью множества (set)
unique_ip_addresses = set(ip_addresses)

# Создаем пустой список, в который будем добавлять IP-адреса и маски подсетей
ip_and_subnet_masks = []

# Проходимся по каждому уникальному IP-адресу и маске подсети
for ip_address, subnet_mask in unique_ip_addresses:
    # Собираем строку в формате "IP-адрес/Маска подсети" и добавляем ее в список ip_and_subnet_masks
    ip_and_subnet_masks.append(ip_address + '/' + subnet_mask)

# Выводим полученный список IP-адресов и масок подсетей на экран
for address in ip_and_subnet_masks:
    print(address)
