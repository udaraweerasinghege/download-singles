__author__ = 'Pavitheran'
__author__ = 'Udara'

from tkinter import *
from getSongLastFm import *
import os




class Application(Frame):
    ## A GUI Application with a button.

    def __init__(self, master):
        ##initializes the Frame
        Frame.__init__(self, master)

        self.grid()
        self.create_widgets()



    def create_widgets(self):

        ##Create labels
        self.instruction = Label(self, text = "Artist Name/Song")
        self.instruction.grid(row=0, column=1, columnspan=1, sticky=W)

        self.number_song = Label(self, text = "Number of Songs")
        self.number_song.grid(row = 1, column = 1, sticky = W)

        ##Create an area where user can type
        self.name = Entry(self)
        self.name.grid(row=0, column=2, sticky=W)

        ##Creates an area for user to specify number of songs
        self.numSongs = Entry(self)
        self.numSongs.grid(row=1, column = 2, sticky = W)
        self.numSongs.configure(state='disabled')

        ##Creating Radio buttons for each option
        v = IntVar()
        self.getsingle = Radiobutton(self, text="Get Single", variable=v, value=0,
                                     command = lambda: self.disabletext(1))
        self.getsingle.grid(row = 0, column = 0, sticky = W)

        self.topsongs = Radiobutton(self, text="Top Songs", variable=v, value=1,
                                    command = lambda: self.disabletext(3))
        self.topsongs.grid(row = 1, column = 0, sticky = W)

        self.mvid = Radiobutton(self, text="Music Video", variable=v, value=2,
                                command = lambda: self.disabletext(1))
        self.mvid.grid(row = 2, column = 0, sticky = W)

        self.popn = Radiobutton(self, text="Popular Now!", variable=v, value=3,
                                command = lambda: self.disabletext(2))
        self.popn.grid(row = 3, column = 0, sticky = W)



        ##Create a button linked to get_mp3
        self.submit = Button(self, text="Submit", command= lambda: self.download_video(v.get()))
        self.submit.grid(row=3, column=1)

        ##Create an area where text can be output to
        self.text = Text(self, width=49, height=30, wrap=WORD)
        self.text.grid(row=5, column=0, columnspan=5, sticky=W)

        ##Creates music folder on C Drive for downloaded mp3s
        if not os.path.exists("C:\Music"):
            os.makedirs("C:\Music")

        os.chdir("C:\Music")

        self.text.insert(0.0, "To get a single song, enter artist and song name.\n"
                              "Example: Taylor Swift Fifteen\n\n"
                              "To get the top songs by an artist, enter artist name and number of songs.\n\n"
                              "Example: To get top 5 songs by Taylor Swift,\n"
                              "Enter Taylor Swift as artist name and 5 as number of songs.\n"
                              "\nTo get music video, enter artist and song name.\n"
                              "\nPopular Now! downloads the specified number of songs from "
                              "the current top 100 billboards.\n"
                              "If no number specified, top 5 songs downloaded.\n"
                              "\nMade by Udara and Pavi")



    def disabletext(self, on):
        if(on == 1):
            self.numSongs.configure(state='disabled')
            self.name.configure(state='normal')
        elif(on == 2):
            self.numSongs.configure(state='normal')
            self.name.configure(state='disabled')
        elif(on == 3):
            self.numSongs.configure(state='normal')
            self.name.configure(state='normal')




    def download_video(self,flag):
        artist_name = self.name.get()
        num_song = self.numSongs.get()
        self.text.delete(0.0, END)

        if (flag == 0):
            ##Downloads specified song
            get_mp3(artist_name)

        elif (flag == 1):
            ##Downloads top 10 songs
            get_song(artist_name, int(num_song))

        elif (flag == 2):
            ##Downloads music video
            get_music_vid(artist_name)

        elif (flag == 3):
            ##Displays the current top num songs
            try:
                get_charts_top(int(num_song))
            except:
                ##Catches exception where '' is passed as num_songs
                print("Please enter the number of popular songs you want to download.")

        ##Shows the user a message on successful completion

        self.text.insert(0.0, "Song(s) successfully downloaded and placed in your C:\music directory.")

        self.name.delete(0, END)
        self.numSongs.delete(0, END)



##Create and format GUI Window
root = Tk()
root.title("Download Songs")
root.geometry("400x400")
root.resizable(width=FALSE, height=FALSE)

app = Application(root)

##Function that keeps the window open
root.mainloop()

