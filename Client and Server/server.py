
import socket
from tkinter import *

root = Tk()
root.title("Server")
root.geometry('300x400')

def send(listbox, entry):
    message = entry.get()
    listbox.insert('end', "server: " + message)
    entry.delete(0, END)
    client.send(bytes(message, "utf-8"))


def recieve(listbox):
    rec_msg = client.recv(100)
    listbox.insert('end', "client: " + rec_msg.decode("utf-8"))


entry = Entry()
entry.pack(side=BOTTOM)

listbox = Listbox(root)
listbox.pack()

button = Button(root, text="Send", command=lambda: send(listbox, entry))
button.pack(side=BOTTOM)

rec_button = Button(root, text="Recieve", command=lambda: recieve(listbox))
rec_button.pack(side=BOTTOM)

HOST = socket.gethostname()
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    client, address = s.accept()
    print(f"Client is connected and has the address {address}")


root.mainloop()
