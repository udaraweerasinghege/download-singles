__author__ = 'Pavitheran'
__author__ = 'Udara'

from tkinter import *
from getSongLastFm import *

class Application(Frame):
    ## A GUI Application with a button.

    def __init__(self, master):
        ##initializes the Frame
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        ##Create a label
        self.instruction = Label(self, text = "Enter Artist Name")
        self.instruction.grid(row=0, column=0, columnspan=2, sticky=W)

        ##Create an area where user can type
        self.name = Entry(self)
        self.name.grid(row=0, column=1, sticky=W)

        ##Create a button to call our method
        self.submit = Button(self, text="Submit", command=self.download_video)
        self.submit.grid(row=2, column=0, sticky=W)

        ##Create an area where text can be output to
        self.text = Text(self, width=40, height=5, wrap=WORD)
        self.text.grid(row=3, column=0, columnspan=2, sticky=W)

    def download_video(self):
        artist_name = self.name.get()
        get_song(artist_name)

        ##Shows the user a message on successful completion
        self.text.delete(0.0, END)
        self.text.insert(0.0, "Song successfully downloaded and placed in directory")

##Create and format GUI Window
root = Tk()
root.title("Download Youtube Music Videos")
root.geometry("300x150")
app = Application(root)

##Function that keeps the window open
root.mainloop()

