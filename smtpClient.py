from socket import *
import socket


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    client_socket = socket.socket()
    client_socket.connect((mailserver, port))

    recv = client_socket.recv(1024).decode()
    # print(recv)
    # if recv[:3] != '220':
    #    print('220 reply not received from server.')

    heloCommand = 'HELO Alice\r\n'
    client_socket.send(heloCommand.encode())
    recv1 = client_socket.recv(1024).decode()
    # print(recv1)
    # if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    mail_from_command = 'MAIL FROM "test@client.net"'
    client_socket.send(mail_from_command.encode())
    recv2 = client_socket.recv(1024).decode()
    # print(recv2)
    # if recv2[:3] != '250':
    #    print('250 reply not received from server.')

    recipient_to_command = 'RCPT TO "cj2577@nyu.edu"'
    client_socket.send(recipient_to_command.encode())
    recv3 = client_socket.recv(1024).decode()
    # print(recv3)
    # if recv3[:3] != '250':
    #    print('250 reply not received from server.')

    data_command = 'DATA'
    client_socket.send(data_command.encode())
    recv4 = client_socket.recv(1024).decode()
    # print(recv4)
    # if recv4[:3] != '250':
    #    print('250 reply not received from server.')

    client_socket.send(msg.encode())

    client_socket.send(endmsg.encode())
    recv5 = client_socket.recv(1024).decode()
    # print(recv5)
    # if recv5[:3] != '250':
    #    print('250 reply not received from server.')

    quit_command = 'QUIT'
    client_socket.send(quit_command.encode())
    recv6 = client_socket.recv(1024).decode()
    # print(recv6)
    # if recv6[:3] != '250':
    #    print('250 reply not received from server.')


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
