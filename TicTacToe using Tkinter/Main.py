import tkinter as tk
import tkinter.messagebox as messagebox

from colorlib import Gray,Red
from tkinter.font import Font 

"""
    >Tic Tac Toe created with python tkinter library
    >Version 1.0.1
    >Version 1.0.1 GameChangeLog > added restart question message after somebody is win
                                 > added restart button in the bottom
    >Version 1.0.1 CodeChangeLog > change class(TicTacToe) variable name helv36  to helv29 
                                 > added new font in class(TicTacToe) named helv12
                                 > !NEED new "colorlib.py" module which contains red color (code in repo also) 
    >Created by Aghnat HS
    >Sorry if the code is a big mess and hard to understand.
"""
#to control Board text when clicked
PLAYER_X="X"
PLAYER_O="O"
PLAYER_NOW=PLAYER_X
#win condition
X_WIN="X_WIN"
O_WIN="O_WIN"

#board data TO CHECK WIN
BOARD_DATA=[
            ["-","-","-"],
            ["-","-","-"],
            ["-","-","-"]
           ]



class Board(tk.Button):
    #single board to let player click and draw x or o

    #state available
    DEFAULT_S="default" #default state
    CLICKED_S="clicked" #state when object is clicked
    ISWIN_S="win" #state when either one is wins
    ISWINCAUSE_S="wincause" #state when this object button is cause of winning 
    

    def __init__(self,data,xx,yy,_font,*args,**kwargs):
        super().__init__(*args,**kwargs)
        #position varibale
        self._x = xx
        self._y = yy
        #font variable
        self._font=_font
        #board data variable
        self.b_data=data
        #set default state for this button 
        self.set_state(self.DEFAULT_S)
        #place the button
        self.pack()
        self.place(x=xx,y=yy)
    
    def set_state(self,state):
        global PLAYER_NOW
        global BOARD_DATA
        #function to set board state 
        if state == self.DEFAULT_S:
            #change button appereance
            self.config(relief=tk.RIDGE,width=3,height=1,bg=Gray.slategray,state=tk.NORMAL)
            #set the text to empty
            self.config(text=" ",font=self._font)
            #set command to this button
            self.config(command=lambda:self.set_state(self.CLICKED_S))
        elif state == self.CLICKED_S:
            #set board data to data connected to this button
            BOARD_DATA[self.b_data[0]][self.b_data[1]]=PLAYER_NOW
            #set the text to x or o
            self.config(text=PLAYER_NOW,font=self._font)
            #check if in this state,somebody is wins
            check_win=TicTacToe.check_win()
            if check_win!=None: 
                check_win=list(check_win)
                if check_win[0]:
                    TicTacToe.set_win()
                    if check_win[1]==X_WIN:
                        #ask if user want to restart a game
                        askRestart=messagebox.askyesno("X WIN THE GAME","RESTART GAME?")
                    elif check_win[1]==O_WIN:
                        #ask if user want to restart a game
                        askRestart=messagebox.askyesno("O WIN THE GAME","RESTART GAME?")
                    #restart the game if user select yes
                    if askRestart!=None and askRestart!=False: 
                        TicTacToe.reset_game()
                        return 0
            #change button appereance AND set to disable state
            self.config(bg=Gray.gray,disabledforeground="#000000",state=tk.DISABLED)
            #set PLAYER_NOW to x or o
            if PLAYER_NOW==PLAYER_X: 
                PLAYER_NOW=PLAYER_O
            elif PLAYER_NOW==PLAYER_O: 
                PLAYER_NOW=PLAYER_X
        elif state == self.ISWIN_S:
            #change button appereance AND set to disable state
            self.config(bg=Gray.gray,disabledforeground="#000000",state=tk.DISABLED)
        


class TicTacToe():

    #define list contains board object 
    board_object=[]

    #master window 
    def __init__(self,width,height):
        #set main window
        self.master = tk.Tk()
        self.master.geometry("{}x{}".format(width,height)) 
        self.master.title("Tic Tac Toe")
        #set font
        self.helv29 = Font(root=self.master,family="Helvetica",size=29,weight="bold")
        self.helv12 = Font(root=self.master,family="Helvetica",size=12,weight="bold")
        #create restart button
        self.restartButton = tk.Button(self.master,text="Restart",command=lambda:TicTacToe.reset_game(),bg=Red.crimson,font=self.helv12,relief=tk.RIDGE)
        self.restartButton.pack()
        self.restartButton.place(x=width/2-35,y=300)
        #create clickable Tic tac toe board
        self.create_board()
        #loop the main window
        self.master.mainloop()

    #function to create a board object
    def create_board(self):
        #////init board /////
        x_start=20
        #first row
        f_row_y = 15
        self.board11 = Board([0,0],xx=x_start,yy=f_row_y,_font=self.helv29)
        self.board12 = Board([0,1],xx=self.board11._x + 90,yy=f_row_y,_font=self.helv29)
        self.board13 = Board([0,2],xx=self.board12._x + 90,yy=f_row_y,_font=self.helv29)
        #append to board object list
        TicTacToe.board_object.extend([self.board11,self.board12,self.board13])
        #second row
        s_row_y = f_row_y + 100
        self.board21 = Board([1,0],xx=x_start,yy=s_row_y,_font=self.helv29)
        self.board22 = Board([1,1],xx=self.board21._x + 90,yy=s_row_y,_font=self.helv29)
        self.board23 = Board([1,2],xx=self.board22._x + 90,yy=s_row_y,_font=self.helv29)
        #append to board object list
        TicTacToe.board_object.extend([self.board21,self.board22,self.board23])
        #third row
        t_row_y = s_row_y + 100
        self.board31=Board([2,0],xx=x_start,yy=t_row_y,_font=self.helv29)
        self.board32=Board([2,1],xx=self.board31._x + 90,yy=t_row_y,_font=self.helv29)
        self.board33=Board([2,2],xx=self.board32._x + 90,yy=t_row_y,_font=self.helv29)
        #append to board object list
        TicTacToe.board_object.extend([self.board31,self.board32,self.board33])
    #function to set all board object to disabled-win-state
    @classmethod
    def set_win(cls):
        #set all board object to disabled state if someone is winning
        for obj in cls.board_object:
            obj.set_state(obj.ISWIN_S)
    #function to reset game
    @classmethod
    def reset_game(cls):
        global BOARD_DATA
        #set board data to default
        BOARD_DATA=[
                    ["-","-","-"],
                    ["-","-","-"],
                    ["-","-","-"]
                   ]
        #set all board object to default
        for obj in cls.board_object:
            obj.set_state(obj.DEFAULT_S)
    #function to check win condition from x or o
    @classmethod
    def check_win(cls):
        #CHECK THE X
        if (
            BOARD_DATA[0]==["X","X","X"] or #horizontal row 1
            BOARD_DATA[1]==["X","X","X"] or #horizontal row 2
            BOARD_DATA[2]==["X","X","X"]    #horizontal row 3
           ):
            return True,X_WIN
        if (
            (BOARD_DATA[0][0] + BOARD_DATA[1][0] + BOARD_DATA[2][0]) == "XXX" or  #vertical column 1
            (BOARD_DATA[0][1] + BOARD_DATA[1][1] + BOARD_DATA[2][1]) == "XXX" or  #vertical column 2
            (BOARD_DATA[0][2] + BOARD_DATA[1][2] + BOARD_DATA[2][2]) == "XXX"     #vertical column 3
           ):
            return True,X_WIN
        if (
            (BOARD_DATA[0][0] + BOARD_DATA[1][1] + BOARD_DATA[2][2]) == "XXX" or  #cross right \
            (BOARD_DATA[0][2] + BOARD_DATA[1][1] + BOARD_DATA[2][0]) == "XXX"   #cross left /
           ):
            return True,X_WIN
        
        #CHECK THE O
        if (
            BOARD_DATA[0]==["O","O","O"] or #horizontal row 1
            BOARD_DATA[1]==["O","O","O"] or #horizontal row 2
            BOARD_DATA[2]==["O","O","O"]    #horizontal row 3
           ): 
            return True,O_WIN
        if (
            (BOARD_DATA[0][0] + BOARD_DATA[1][0] + BOARD_DATA[2][0]) == "OOO" or  #vertical column 1
            (BOARD_DATA[0][1] + BOARD_DATA[1][1] + BOARD_DATA[2][1]) == "OOO" or  #vertical column 2
            (BOARD_DATA[0][2] + BOARD_DATA[1][2] + BOARD_DATA[2][2]) == "OOO"     #vertical column 3
           ):
            return True,O_WIN
        if (
            (BOARD_DATA[0][0] + BOARD_DATA[1][1] + BOARD_DATA[2][2]) == "OOO" or  #cross right \
            (BOARD_DATA[0][2] + BOARD_DATA[1][1] + BOARD_DATA[2][0]) == "OOO"   #cross left /
           ):
            return True,O_WIN
        

main=TicTacToe(300,340)