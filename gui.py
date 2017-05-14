from Tkinter import *

class gui:
	master = Tk()
	master.attributes('-zoomed', True)
	master.title("Music Recommendation System")

	label = Label(master, text="Music Recommendation System", font=7, pady=20)
	label.pack()

	label = Label(master, text="Select Singer")
	label.pack()

	frame = Frame(master, pady=20)
	frame.pack()

	listbox = Listbox(frame, width=33, height=15)
	listbox.pack(side="left", fill="y")

	scrollbar = Scrollbar(frame, orient="vertical")
	scrollbar.config(command=listbox.yview)
	scrollbar.pack(side="right", fill="y")

	listbox.config(yscrollcommand=scrollbar.set)

