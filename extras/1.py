from Tkinter import *
from ttk import *
from tkintertable.Tables import TableCanvas
from tkintertable.TableModels import TableModel

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.model = TableModel()
        self.table = TableCanvas(self, model=self.model)
        self.table.createTableFrame()
        root.bind('<ButtonRelease-1>', self.clicked)   #Bind the click release event

        self.create_widgets()

    def create_widgets(self):
        self.table.model.load('save.table')  #You don't have to load a model, but I usually
        self.table.redrawTable()             #Create a base model for my tables.

        d = dir(self.table)  #Will show you what you can do with tables.  add .model
                             #to the end to see what you can do with the models.
        for i in d:
            print i

    def clicked(self, event):  #Click event callback function.
        #Probably needs better exception handling, but w/e.
        try:
            rclicked = self.table.get_row_clicked(event)
            cclicked = self.table.get_col_clicked(event)
            clicks = (rclicked, cclicked)
            print 'clicks:', clicks
        except: 
            print 'Error'
        if clicks:
            #Now we try to get the value of the row+col that was clicked.
            try: print 'single cell:', self.table.model.getValueAt(clicks[0], clicks[1])
            except: print 'No record at:', clicks

            #This is how you can get the entire contents of a row.
            try: print 'entire record:', self.table.model.getRecordAtRow(clicks[0])
            except: print 'No record at:', clicks

root = Tk()
root.title('Table Test')
app = Application(master=root)
print 'Starting mainloop()'
app.mainloop()


