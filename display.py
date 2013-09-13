
from Tkinter import *
import sys
import random
#---------------------------------------------------------------------------------------
# Application - GUI code
class Application(Frame):

    def createWidgets(self,filename):
        self.photo = PhotoImage(file=filename)

        self.label = Label(image=self.photo)
        self.label.image = self.photo
        self.label.pack()

    def __init__(self,filename, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets(filename)

title=sys.argv[1]
filename=sys.argv[2]

picfile = open(filename, 'r')
pics = []
for line in picfile.readlines():
    pics.append( line.strip())
picfile.close()

root = Tk()
root.title(title)
pic_filename = random.choice(pics) 
app = Application(pic_filename, master=root)
app.mainloop()
try:
    root.destroy()
except Exception as e:
    pass

