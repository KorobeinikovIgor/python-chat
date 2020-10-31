from time import sleep
import socket
import threading
def read_sok():
    global server
    while True:
        data = sor.recv(1024)
        if data.decode('utf-8')=='OK-010':
            print('You password is correct!')
            continue
        if data.decode('utf-8')=='OK-999':
            print('Invalid password!')
            continue
        print(data.decode('utf-8'))

server = '192.168.0.102', 8080
alias = input('input yor nick: ')
print('connecting to server...')
print('\nDONE\n')
sor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sor.bind(('', 0)) # Задаем сокет как клиент


sor.sendto((alias+' connected to the server').encode('utf-8'), server)


potok = threading.Thread(target= read_sok)
potok.start()

while True:
    message = input()
    if 'ban' in message:
        password=input('Введите пароль: ')
        usban=(message.split('>')[0]).replace('<', '')
        request=usban+'@'+password
        #пример запроса: 'ban $igor$@3-43-423'
        sor.sendto(request.encode('utf-8'), server)
        print(request)
        continue
    sor.sendto((f'<{alias}> {message}').encode('utf-8'), server)
