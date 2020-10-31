import socket
from random import shuffle

print ('Start Server')

###
client = []
all_messages=[]
users={}
black_list=[]
###

s=[str(i) for i in range(100)]
shuffle(s)
password='-'.join(s[:4])
password='1-1-1-1'
print('password:', password)
while 1 :
    try:
        data , addres = sock.recvfrom(1024)
        message=data.decode('utf-8')
        sender=((message.split('>')[0]).replace('<', ''), addres)
        all_messages.append(message)
        if 'connected to the server' not in message:
            users.update([sender])
        else:
            users.update(message.split()[0])
        print(users)
        print(addres, data)

        if 'ban' in message:
            if message.split('@')[1]==password:

                ban_user=users[message.split('$')[1]]

                black_list.append(ban_user)
                sock.sendto(b'OK-010',clients)
                sock.sendto((f'\nUser {message.split("$")[1]} is banned!\n').encode('utf-8'), clients)
            else:
                sock.sendto(b'OK-999',addres)
            continue
        ###

        if addres in black_list:
            sock.sendto(b'You are banned!', addres)
            continue
        ###
        if addres not in client:
            client.append(addres)
        for clients in client:
            if clients != addres:
                if addres not in black_list:
                    sock.sendto(data,clients)

    except KeyboardInterrupt:
        break
    except IndexError:
        sock.sendto(('%s\n\nInvalid command\nTry this:\nban $user$\n\n%s' % ('#'*15, '#'*15)).encode('utf-8') ,addres)
    except KeyError:
       sock.sendto(b'There is no such user in this chat', addres)
