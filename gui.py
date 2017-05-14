from Tkinter import *

class gui:
	master = Tk()
	master.attributes('-zoomed', True)

	frame = Frame(master)
	frame.pack()

	listbox = Listbox(frame)
	listbox.pack(side="left", fill="y")

	scrollbar = Scrollbar(frame, orient="vertical")
	scrollbar.config(command=listbox.yview)
	scrollbar.pack(side="right", fill="y")

	listbox.config(yscrollcommand=scrollbar.set)

