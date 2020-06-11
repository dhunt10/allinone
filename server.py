from sockets import AF_INET, socket, SOCK_STREAM
from threading import Thread
from X import XXX

def accept_new():
    while True:
        client, client_address = SERVER.accept()
        client.send(bytes("What would you like to do today?\n Press p then enter to list the options"))
        addresses[client] = client_address
        Thread(taregt=handle_client, args=client).start()

def handle_client(client):
    option = client.recv(BUFFSIZE).decode("utf8")
    switch(option)
