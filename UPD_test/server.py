# Модуль socket для сетевого программирования
from socket import *

# данные сервера
host = 'localhost'
port = 777
addr = (host, port)

# socket - функция создания сокета
# первый параметр socket_family может быть AF_INET или AF_UNIX
# второй параметр socket_type может быть SOCK_STREAM(для TCP) или SOCK_DGRAM(для UDP)
udp_socket = socket(AF_INET, SOCK_DGRAM)
# bind - связывает адрес и порт с сокетом
udp_socket.bind(addr)

# Бесконечный цикл работы программы
while True:

    # Если мы захотели выйти из программы
    question = input('Do you want to quit? y\\n: ')
    if question == 'y': break

    print('wait data...')

    # recvfrom - получает UDP сообщения
    data, addr = udp_socket.recvfrom(1024)
    data = bytes.decode(data)
    print('client addr: ', addr)
    print('client data: ', data)


    # sendto - передача сообщения UDP
    udp_socket.sendto(b'message received by the server', addr)

udp_socket.close()
