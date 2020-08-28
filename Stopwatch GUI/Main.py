import tkinter as tk
import tkinter.font as tkfont

from datetime import datetime

class Stopwatch:

    __Author__="Aghnat HS"

    __NATIVE_WIDTH=480
    __NATIVE_HEIGTH=480

    __TITLE="Stopwatch by {}".format(__Author__)

    __RESET=666000
    __RESET_VALUE=666000
    __HOURS_FORMAT="%H:%M:%S"

    __SECONDS=1000
    def __init__(self):
        #main window
        self.Master=tk.Tk()
        self.Master.title(self.__TITLE)
        self.Master.geometry("{}x{}".format(self.__NATIVE_WIDTH,self.__NATIVE_HEIGTH))
        
        #font
        self.isrunning=False
        self.timeFont=tkfont.Font(family="Helvetica",size=46,weight="bold")
        self.buttonFont=tkfont.Font(family="Helvetica",size=16,weight="bold")

        #time variable
        self.time=datetime.fromtimestamp(self.__RESET).strftime(self.__HOURS_FORMAT)

        #displaying time
        self.timeDisplay=tk.Label(self.Master,text=self.time,font=self.timeFont)

        #create button
        self.btnStart=tk.Button(self.Master,text="Start",command=lambda:self.startStopwatch(),font=self.buttonFont,relief=tk.GROOVE)
        self.btnStop=tk.Button(self.Master,text="Stop",command=lambda:self.stopStopwatch(),font=self.buttonFont,state=tk.DISABLED,relief=tk.GROOVE)
        self.btnReset=tk.Button(self.Master,text="Reset",command=lambda:self.resetStopwatch(),font=self.buttonFont,state=tk.DISABLED,relief=tk.GROOVE)

        #placing button
        self.placeButton()
        self.Master.mainloop()
    
    def placeButton(self):
        #function to place the button 
        self.timeDisplay.pack()
        self.timeDisplay.place(x=240,y=200,anchor=tk.CENTER)
        self.btnStart.pack()
        self.btnStart.place(x=167,y=260,anchor=tk.W)
        self.btnStop.pack()
        self.btnStop.place(x=243,y=260,anchor=tk.W)
        self.btnReset.pack()
        self.btnReset.place(x=200,y=310,anchor=tk.W)

    def timeRunning(self):
        #change time
        self.__RESET+=1
        self.time=datetime.fromtimestamp(self.__RESET).strftime(self.__HOURS_FORMAT)
        self.timeDisplay.config(text=self.time)

        #call this function again  if true
        if (self.isrunning==True):
            self.Master.after(self.__SECONDS,self.timeRunning)

    def startStopwatch(self):
        #set button state
        self.btnStart["state"]=tk.DISABLED
        self.btnStop["state"]=tk.NORMAL
        self.btnReset["state"]=tk.NORMAL
        #start 
        self.isrunning=True

        #start the watch
        if (self.isrunning):
            self.Master.after(self.__SECONDS,self.timeRunning)
        
    def stopStopwatch(self):
        #set button state
        self.btnStart["state"]=tk.DISABLED
        self.btnStop.config(state=tk.NORMAL,text="Resume")
        self.btnReset["state"]=tk.DISABLED
        #stop
        if self.isrunning==True: 
            self.isrunning=False
        elif self.isrunning==False: 
            self.isrunning=True
            #increment by 1 to normalized
            self.__RESET=self.__RESET+1 
            #change button state and text
            self.btnReset["state"]=tk.NORMAL
            self.btnStop["text"]="Stop"
            #continue ticking
            self.Master.after(self.__SECONDS,self.timeRunning)

        #decrement by 1 to avoid + 00:00:01
        self.__RESET=self.__RESET-1
    
    def resetStopwatch(self):
        self.btnStart["state"]=tk.NORMAL
        self.btnStop.config(state=tk.DISABLED,text="Stop")
        self.btnReset["state"]=tk.DISABLED

        self.isrunning=False

        #reset value and decrement by 1 to avoid 00:00:01
        self.__RESET=self.__RESET_VALUE-1


stopwatch=Stopwatch()