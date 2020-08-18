import tkinter as tk
import tkinter.font as tkfont
import tkinter.messagebox as messagebox

#CREATED BY AGHNAT HS
class CurrencyConverter():
    
    __NATIVE_WIDTH=320
    __NATIVE_HEIGHT=420

    __APP_NAME="USD to IDR"

    __KURS=14906 #17-August-2020
    def __init__(self):
        self.master=tk.Tk()
        self.master.title(self.__APP_NAME)
        self.master.geometry("{}x{}".format(self.__NATIVE_WIDTH,self.__NATIVE_HEIGHT))

        #Create Entry and Button
        self.dollarEntry=tk.Entry(self.master)
        self.rupiahEntry=tk.Entry(self.master)
        self.btnDollar_Rupiah=tk.Button(self.master,text="USD-IDR",command=lambda:self.dollar_to_rupiah())
        self.btnRupiah_Dollar=tk.Button(self.master,text="IDR-USD",command=lambda:self.rupiah_to_dollar())
        #Main Variable
        self.dollar=self.dollarEntry.get()
        self.rupiah=self.rupiahEntry.get()
        #Peripheral
        self.usdText=tk.Label(self.master,text="USD")
        self.idrText=tk.Label(self.master,text="IDR")

        self.buttonPlacing()
        self.master.mainloop()

    def buttonPlacing(self):
        self.dollarEntry.pack()
        self.rupiahEntry.pack()
        self.btnDollar_Rupiah.pack()
        self.btnRupiah_Dollar.pack()
        self.usdText.pack()
        self.idrText.pack()
        self.btnDollar_Rupiah.place(x=100,y=175)
        self.btnRupiah_Dollar.place(x=165,y=175)
        self.usdText.place(x=70,y=125)
        self.dollarEntry.place(x=100,y=125)
        self.idrText.place(x=70,y=150)
        self.rupiahEntry.place(x=100,y=150)

    def dollar_to_rupiah(self):
        self.dollar=self.dollarEntry.get()
        try:
            __converted=format(int(self.dollar)*self.__KURS,".2f")
        except ValueError:
            messagebox.showwarning("ERROR","Please Input An Integer")
        #insert to entry
        self.rupiahEntry.delete(0,tk.END)
        self.rupiahEntry.insert(0,__converted)
    
    def rupiah_to_dollar(self):
        self.rupiah=self.rupiahEntry.get()
        try:
            __converted=format(int(self.rupiah)/self.__KURS,".2f")
        except ValueError:
            messagebox.showwarning("ERROR","Please Input An Integer")
        #insert to entry
        self.dollarEntry.delete(0,tk.END)
        self.dollarEntry.insert(0,__converted)

cc=CurrencyConverter()