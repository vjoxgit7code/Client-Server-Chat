
import socket
from tkinter import *

root = Tk()
root.title("Client")
root.geometry('300x400')


def send(listbox, entry):
    message = entry.get()
    listbox.insert('end', "client: " + message)
    entry.delete(0, END)
    s.send(bytes(message, "utf=8"))


def recieve(listbox):
    message = s.recv(100)
    listbox.insert('end', "server: " + message.decode('utf-8'))


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

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

root.mainloop()
