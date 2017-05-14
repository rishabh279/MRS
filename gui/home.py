from Tkinter import *

master = Tk()
master.attributes('-zoomed', True)
master.title("Music Recommendation System")

label = Label(master, text="Music Recommendation System", font=7, pady=20)
label.pack()

label = Label(master, text="Select Singer")
label.pack()

frame = Frame(master, pady=20)
frame.pack()

listbox = Listbox(frame)
listbox.pack(side="left", fill="y")

scrollbar = Scrollbar(frame, orient="vertical")
scrollbar.config(command=listbox.yview)
scrollbar.pack(side="right", fill="y")

listbox.config(yscrollcommand=scrollbar.set)



for item in ["zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]:
    listbox.insert(END,item)

var = StringVar()
label = Message( master, textvariable=var )

def recommend():
	
	sel = listbox.curselection()[0]	
	var.set(str(sel))
		
b = Button(master, text="Recommend", command=recommend)
b.pack()
label.pack()

mainloop()


