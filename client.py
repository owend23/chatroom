from socket import *
from threading import Thread
import tkinter as tk

class Chat(tk.Tk):
	def __init__(self):
		self.title("Chatroom")
		messages = tk.Frame(self)
		my_msg = tk.StringVar()
		my_msg.set("")
		scrollbar = tk.Scrollbar(messages)
		msg_list = tk.Listbox(messages, height=15, width=50, yscrollcommand=scrollbar.set)
		scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
		msg_list.pack(side=tk.LEFT, fill=tk.BOTH)
		messages.pack()
		
		entry = tk.Entry(self, textvariable=my_msg)
		entry.bind("<Return>", send)
		entry.pack()
		send = tk.Button(self, text="Send", command=send)
		send.pack()
		
		self.protocol("WM_DELETE"WINDOW", on_closing)

def receive():
	while True:
		try:
			msg = client_socket.recv(1024).decode('utf8')
			msg_list.insert(tk.END, message)
			
def send(event=None):
	msg = my_msg.get()
	my_msg.set("")
	client_socket.send(bytes(msg, "utf8"))
	if msg == '{quit}':
		client_socket.close()
		top.quit()
		
def on_closing(event=None):
	my_msg.set("{quit}")
	send()
