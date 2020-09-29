import tkinter as tk
from tkinter.font import Font 
from tkinter.filedialog import askopenfilename

from pygame import mixer as Playback
from mutagen.wave import WAVE
from mutagen.mp3 import MP3

from math import floor

from pathlib import Path

from colorlib import Gray

"""
    Quick and Simple Music Player using Python
    Created by Aghnat Hasya S
    >only support mp3 
    >update support wave 
"""

class Music():
    #base class for song 
    def __init__(self,fileLocation):
        self.musicLocation = fileLocation
        try:
            self.musicLength = floor(MP3(self.musicLocation).info.length)
        except:
            self.musicLength = floor(WAVE(self.musicLocation).info.length)
        self.musicTitle = Path(self.musicLocation).name

class HoverButton(tk.Button):
    #base button 
    def __init__(self,xx,yy,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.defaultBackground = Gray.gainsboro
        self.activeBackground = Gray.slategray
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        
        #>>SET DEFAULT STATE OF THIS TYPE BUTTON
        self["bg"] = self.defaultBackground
        self["relief"] = tk.RAISED
        self.pack()
        self.place(x=xx,y=yy,anchor=tk.N)

    def on_enter(self, e):
        self['bg'] = self.activeBackground
    def on_leave(self, e):
        self['bg'] = self.defaultBackground


class App():
    #base app 
    def __init__(self,w,h):
        #init window
        self.app = tk.Tk()
        self.app.geometry("{}x{}".format(w,h))
        self.app.resizable(height=False)
        self.app.title("Music Player")
        #init font 
        self.createFont()
        #create label with song title when music object is created later
        self.musicTitle = tk.Label(text="",font=self.hevlLow)
        self.musicTitle.pack()
        self.musicTitle.place(anchor=tk.N,x=320)
        #init button
        self.createButton()
        #init menu file
        self.createMenu()
        #loop the window
        self.app.mainloop()
        #other var
        self.isPlay=False
    #button label font function
    def createFont(self):
        self.hevl = Font(root=self.app,family="Helvetica",size=30,weight="bold")
        self.hevlLow = Font(root=self.app,family="Helvetica",size=14,weight="bold")
    def createButton(self):
        self.playButton = HoverButton(xx=320,yy=300,text="PLAY",font=self.hevl,command=lambda:self.playPauseMusic(),master=self.app)
    def createMenu(self):
        self.MainMenu = tk.Menu(self.app)
        
        #file menu
        self.musicMenu = tk.Menu(self.MainMenu,tearoff=False)
        self.musicMenu.add_command(label="Open",command=lambda:self.openMusic())
        #help menu
        self.helpMenu = tk.Menu(self.MainMenu,tearoff=False)
        self.helpMenu.add_command(label="About",command=lambda:self.createAbout())

        #add to master main menu
        self.MainMenu.add_cascade(label="Music",menu=self.musicMenu)
        self.MainMenu.add_cascade(label="Help",menu=self.helpMenu)
        #add master main menu to master app
        self.app.config(menu=self.MainMenu)
    #main music function
    def openMusic(self):
        #pause the music when select a file and if playback has been initialized
        if (Playback.get_init()): 
            Playback.music.pause()
            self.isPlay=False
            self.playButton["text"] = "RESUME"
        #search for music file
        music_path = str(Path.home() / "Music")
        file = askopenfilename(title="Select a Music",filetypes=[("Music File",("*.mp3","*.wav"))],initialdir=music_path)
        #create music object
        self.music = Music(file)
        #set if music object is created
        if self.music!=None:
            Playback.quit()
            self.isPlay=False
            self.playButton["text"] = "PLAY"
            self.musicTitle.config(text=self.music.musicTitle)
            self.app.title("Music Player ("+file+")")
    def playPauseMusic(self):
        if isinstance(self.music,Music):
            #if playback is initialized
            if (not Playback.get_init()):
                #play the music
                Playback.init()
                Playback.music.load(self.music.musicLocation)
                Playback.music.play()
                self.isPlay=True
                #set play button to pause
                self.playButton["text"] = "PAUSE"
            #if playback is initialized
            else:
                if (self.isPlay):
                    Playback.music.pause()
                    self.isPlay=False
                    #set play button to play
                    self.playButton["text"] = "RESUME"
                else:
                    Playback.music.unpause()
                    self.isPlay=True
                    #set play button to play
                    self.playButton["text"] = "PAUSE"
    def createAbout(self):
        self.about = tk.Toplevel(self.app)
        self.about.title("About")
        self.about.geometry("240x144")
        self.aboutLabel = tk.Label(self.about,text="""Quick and Simple Music Player 
                                                      \n Created by Aghnat HS 
                                                      \n Using Python Libraries
                                                       \n Support .mp3 and .wav""")
        self.aboutLabel.pack()                
_Main = App(640,480)