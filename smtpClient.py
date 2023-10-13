from socket import *
import socket
from smtplib import SMTP

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called client_socket and establish a TCP connection with mailserver and port

    # Fill in start
    client_socket = socket.socket()
    client_socket.connect((mailserver, port))
    # Fill in end

    recv = client_socket.recv(1024).decode()
    print(recv)  # You can use these print statement to validate return codes from the server.
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    client_socket.send(heloCommand.encode())
    recv1 = client_socket.recv(1024).decode()
    print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mail_from_command = 'MAIL FROM "test@client.net"'
    client_socket.send(mail_from_command.encode())
    recv2 = client_socket.recv(1024).decode()
    print(recv2)
    if recv2[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    recipient_to_command = 'RCPT TO "cj2577@nyu.edu"'
    client_socket.send(recipient_to_command.encode())
    recv3 = client_socket.recv(1024).decode()
    print(recv3)
    if recv3[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    data_command = 'DATA'
    client_socket.send(data_command.encode())
    recv4 = client_socket.recv(1024).decode()
    print(recv4)
    if recv4[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Send message data.
    # Fill in start
    client_socket.send(msg.encode())
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    client_socket.send(endmsg.encode())
    recv5 = client_socket.recv(1024).decode()
    print(recv5)
    if recv5[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quit_command = 'QUIT'
    client_socket.send(quit_command.encode())
    recv6 = client_socket.recv(1024).decode()
    print(recv6)
    if recv6[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
