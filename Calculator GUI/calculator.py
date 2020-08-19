import tkinter as tk
import tkinter.font as font
import tkinter.messagebox as messagebox

from colorlib import Gray,White
from math import sqrt,pi

import numpy as np


class Calculator():
	
	#NATIVE MAIN WINDOW SIZE
	__NATIVE_WIDTH=640
	__NATIVE_HEIGHT=360
	#ERROR MESSAGE
	__ERROR_ZERO_DIVISION="Cannot Divide By Zero"
	__ERROR_SYNTAX="Wrong Calculation or Calculation Is Not Complete"
	__ERROR_SQRT="Negative Number Cannot Be Rooted"
	__ERROR_PHI="Wrong Function "
	__ERROR_DRAW="Coordinate Is Not Complete/Wrong Format,Format:x1.x2.y1.y2"
	__ERROR_NAMES="Wrong Math Symbol"
	#VERSION
	__VERSION="1.1.2"
	#CANVAS FOR DRAWING GRAPHIC
	__CANVAS_X=250
	__CANVAS_Y=10
	def __init__(self):
		#Main Window
		self.master=tk.Tk()
		self.master.title("Simple Calculator by Aghnat")
		self.master.geometry("{}x{}".format(self.__NATIVE_WIDTH,self.__NATIVE_HEIGHT))
		self.master.config(bg="#DCDCDC")
		#Set Fonts
		self.fontValue=font.Font(family="helvetica",size=12,weight="bold")
		self.fontAbout=font.Font(family="helvetica",size=8,weight="bold")
		#Evaluation And Equation
		self.evaluation=[]
		self.evaluationLabel="".join(self.evaluation)
		self.value=tk.Label(self.master,text=self.evaluationLabel,bg="#DCDCDC",font=self.fontValue)
		#Packing
		self.value.pack()
		self.value.place(x=1,y=12)

		self.createButton()
		self.createMenu()
		#Create Canvas
		self.createCanvas()

		#Looping The Main Window
		self.master.mainloop()

	#ABOUT_WINDOW
	def createAbout(self):
		self.about=tk.Toplevel(self.master)
		self.about.title("About")
		self.about.geometry("240x144")

		self.aboutLabel=tk.Label(self.about,text="Simple Calculator by Aghnat HS \n{} \nCreated Using Python And Tkinter Library"
								 .format(self.__VERSION),font=self.fontAbout)
		self.aboutLabel.pack()
	#TIPS_WINDOW
	def createTips(self):
		self.tips=tk.Toplevel(self.master)
		self.tips.title("Tips")
		self.tips.geometry("240x144")

		self.tipsLabel=tk.Label(self.tips,text="""Testing
												  \n Testing
													""")
		self.tipsLabel.pack()
	#CREATE MENU
	def createMenu(self):
		self.MainMenu=tk.Menu(self.master)

		#ChangeRelief
		self.ChangeRelief=tk.Menu(self.MainMenu)
		self.ChangeRelief.add_command(label="Sunken",command=lambda:self.changeReliefButton(_relief=tk.SUNKEN))
		self.ChangeRelief.add_command(label="Raised",command=lambda:self.changeReliefButton(_relief=tk.RAISED))
		self.ChangeRelief.add_command(label="Flat",command=lambda:self.changeReliefButton(_relief=tk.FLAT))
		#Change Color
		self.ChangeColor=tk.Menu(self.MainMenu)
		self.ChangeColor.add_command(label="Default",command=lambda:self.changeTheme(_masterbg="#DCDCDC",_valuebg="#DCDCDC",_canvasbg="#DCDCDC"))
		self.ChangeColor.add_command(label="Green Dark",command=lambda:self.changeTheme(_colorbtn=Gray.darkgray,_masterbg=Gray.darkslategray,_valuebg=Gray.darkslategray,_canvasbg=Gray.darkslategray))


		#CASCADE
		self.MainMenu.add_cascade(label="Relief",menu=self.ChangeRelief)
		self.MainMenu.add_cascade(label="Theme",menu=self.ChangeColor)
		self.master.config(menu=self.MainMenu)
	#CREATE BUTTON	
	def createButton(self):
		self.btn1=tk.Button(self.master,text=" 1 ",command=lambda:self.insertValue("1"))
		self.btn2=tk.Button(self.master,text=" 2 ",command=lambda:self.insertValue("2"))
		self.btn3=tk.Button(self.master,text=" 3 ",command=lambda:self.insertValue("3"))
		self.btn4=tk.Button(self.master,text=" 4 ",command=lambda:self.insertValue("4"))
		self.btn5=tk.Button(self.master,text=" 5 ",command=lambda:self.insertValue("5"))
		self.btn6=tk.Button(self.master,text=" 6 ",command=lambda:self.insertValue("6"))
		self.btn7=tk.Button(self.master,text=" 7 ",command=lambda:self.insertValue("7"))
		self.btn8=tk.Button(self.master,text=" 8 ",command=lambda:self.insertValue("8"))
		self.btn9=tk.Button(self.master,text=" 9 ",command=lambda:self.insertValue("9"))
		self.btn0=tk.Button(self.master,text=" 0 ",command=lambda:self.insertValue("0"))
		self.btnFloat=tk.Button(self.master,text=" ,  ",command=lambda:self.insertValue(","))

		self.btnDelete=tk.Button(self.master,text="<<",command=lambda:self.deleteValue(),width=2)
		self.btnClear=tk.Button(self.master,text="Clr",command=lambda:self.clearValue(),width=2)
		self.btnEqual=tk.Button(self.master,text=" = ",command=lambda:self.equalValue(),width=6)
		self.btnPlus=tk.Button(self.master,text=" + ",command=lambda:self.insertValue("+"))
		self.btnMinus=tk.Button(self.master,text="  - ",command=lambda:self.insertValue("-"))
		self.btnTimes=tk.Button(self.master,text="  x ",command=lambda:self.insertValue("x"))
		self.btnTimesDot=tk.Button(self.master,text="  .  ",command=lambda:self.insertValue("."),width=2)
		self.btnDivide=tk.Button(self.master,text="  : ",command=lambda:self.insertValue(":"))
		self.btnSqrt=tk.Button(self.master,text="  sqrt  ",command=lambda:self.insertValue("sqrt("))
		self.btnPhi=tk.Button(self.master,text="phi",command=lambda:self.insertValue("PI"))
		self.btnOpBracket=tk.Button(self.master,text=" ( ",command=lambda:self.insertValue("("))
		self.btnClBracket=tk.Button(self.master,text=" ) ",command=lambda:self.insertValue(")"))

		self.btnDrawRect=tk.Button(self.master,text="Draw Rectangle",command=lambda:self.drawCanvas())
		self.btnClrDraw=tk.Button(self.master,text="Clr Draw",command=lambda:self.clearCanvas())
		self.btnAbout=tk.Button(self.master,text="About",command=self.createAbout
								,width=6,bg=Gray.lightgray,takefocus="on",relief=tk.FLAT)
		self.btnTips=tk.Button(self.master,text="Tips",command=self.createTips
								,width=6,bg=Gray.lightgray,takefocus="on",relief=tk.FLAT)

		#LIST CONTAIN OF BUTTON OBJECT 
		self.__LIST_BUTTON=[self.btn1,self.btn2,self.btn3,self.btn4,
							self.btn5,self.btn6,self.btn7,self.btn8
							,self.btn9,self.btn0,self.btnDelete,self.btnClear,self.btnEqual,self.btnPlus
							,self.btnMinus,self.btnTimes,self.btnTimesDot,self.btnDivide,self.btnSqrt
							,self.btnPhi,self.btnOpBracket,self.btnClBracket,self.btnFloat,self.btnDrawRect,
							self.btnClrDraw]

		self.changeTheme()
		self.packButton()
		self.placeButton()
	def packButton(self):
		self.btn1.pack()
		self.btn2.pack()
		self.btn3.pack()
		self.btn4.pack()
		self.btn5.pack()
		self.btn6.pack()
		self.btn7.pack()
		self.btn8.pack()
		self.btn9.pack()
		self.btn0.pack()
		self.btnFloat.pack()
		self.btnDelete.pack()
		self.btnClear.pack()
		self.btnEqual.pack()
		self.btnPlus.pack()
		self.btnMinus.pack()
		self.btnTimes.pack()
		self.btnTimesDot.pack()
		self.btnDivide.pack()
		self.btnSqrt.pack()
		self.btnPhi.pack()
		self.btnOpBracket.pack()
		self.btnClBracket.pack()
		self.btnDrawRect.pack()
		self.btnClrDraw.pack()
		self.btnAbout.pack()
		self.btnTips.pack()
	def placeButton(self):
		self.btn1.place(x=10,y=60)
		self.btn2.place(x=40,y=60)
		self.btn3.place(x=70,y=60)
		self.btn4.place(x=100,y=60)
		self.btn5.place(x=10,y=95)
		self.btn6.place(x=40,y=95)
		self.btn7.place(x=70,y=95)
		self.btn8.place(x=100,y=95)
		self.btn9.place(x=10,y=130)
		self.btn0.place(x=40,y=130)
		self.btnFloat.place(x=70,y=130)
		self.btnDelete.place(x=70,y=160)
		self.btnClear.place(x=100,y=160)
		self.btnEqual.place(x=10,y=160)
		self.btnPlus.place(x=140,y=60)
		self.btnMinus.place(x=140,y=95)
		self.btnTimes.place(x=170,y=95)
		self.btnDivide.place(x=170,y=60)
		self.btnSqrt.place(x=200,y=95)
		self.btnTimesDot.place(x=140,y=130)
		self.btnPhi.place(x=170,y=130)
		self.btnOpBracket.place(x=200,y=60)
		self.btnClBracket.place(x=222,y=60)

		self.btnAbout.place(x=10,y=self.__NATIVE_HEIGHT-35)
		self.btnTips.place(x=65,y=self.__NATIVE_HEIGHT-35)

		self.btnClrDraw.place(x=self.__CANVAS_X+95,y=280)
		self.btnDrawRect.place(x=self.__CANVAS_X,y=280)

	#MANIPULATE BUTTON PROPERTY
	def changeTheme(self,_colorbtn=Gray.lightgray,_masterbg=None,_valuebg=None,_canvasbg=None):
		for index in range(len(self.__LIST_BUTTON)):
			self.__LIST_BUTTON[index]["bg"]=_colorbtn

		if _masterbg!=None: self.master.config(bg=_masterbg)
		if _valuebg!=None: self.value.config(bg=_valuebg)
		if _canvasbg!=None: self.canvas.config(bg=_canvasbg)
	def changeReliefButton(self,_relief):
		for index in range(len(self.__LIST_BUTTON)):
			self.__LIST_BUTTON[index]["relief"]=_relief

	#CREATE CANVAS
	def createCanvas(self):
		#Canvas Master
		self.canvas=tk.Canvas(self.master,bg="white",borderwidth=0,insertborderwidth=0)
		self.canvas.pack()
		self.canvas.place(x=self.__CANVAS_X,y=self.__CANVAS_Y)\
		#Stored Canvas Width and Height
		self.canvasW=int(self.canvas.cget("width"))
		self.canvasH=int(self.canvas.cget("height"))
		#DRAW X AND Y COORDINATE
		self.__XCOORDINATE=self.canvas.create_line(0,self.canvasH/2,self.canvasW+2,self.canvasH/2,fill="red")
		self.__YCOORDINATE=self.canvas.create_line(self.canvasW/2,0,self.canvasW/2,self.canvasH,fill="red")
	def drawCanvas(self):
		try:
			self.RectCoordinate="".join(self.evaluationLabel).split(".")
			self.rect=self.canvas.create_rectangle(self.RectCoordinate,width=4)
			self.canvas.addtag_withtag("rect",self.rect)
		except tk.TclError:
			messagebox.showerror("Error",self.__ERROR_DRAW)
	def clearCanvas(self):
		self.canvas.delete("rect")
		pass

	#VALUE CHANGEs
	def equalValue(self):
		self.evaluationLabel=self.evaluationLabel.replace("x","*")
		self.evaluationLabel=self.evaluationLabel.replace(":","/")
		self.evaluationLabel=self.evaluationLabel.replace(".","*")
		self.evaluationLabel=self.evaluationLabel.replace(",",".")
		self.evaluationLabel=self.evaluationLabel.lower()
		try:
			self.equal=eval(self.evaluationLabel)
			self.value["text"]=self.equal
		except SyntaxError:
			messagebox.showerror("Error",self.__ERROR_SYNTAX)
			self.clearValue()
		except NameError:
			messagebox.showerror("Error",self.__ERROR_NAMES)
			self.clearValue()
		except ZeroDivisionError:
			messagebox.showerror("Error",self.__ERROR_ZERO_DIVISION)
			self.clearValue()
		except ValueError:
			messagebox.showerror("Error",self.__ERROR_SQRT)
		except TypeError:
			messagebox.showerror("Error",self.__ERROR_PHI)
			self.clearValue()
		else:
			self.evaluation.clear()
			self.evaluation.append(str(self.equal))
	def insertValue(self,arg):
		self.evaluation.append(arg)
		self.update()
	def deleteValue(self):
		try:
			self.evaluation.pop(len(self.evaluation)-1)
		except IndexError:
			pass
		self.update()
	def clearValue(self):
		self.evaluation.clear()
		self.update()

	#UPDATING VALUE REGULARLY
	def update(self):
		self.evaluationLabel="".join(self.evaluation)
		self.value["text"]=self.evaluationLabel


calculators=Calculator()