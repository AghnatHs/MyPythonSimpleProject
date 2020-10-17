import tkinter as tk
import tkinter.messagebox as messagebox

from jsonfile import json_processing as jsp

#Constant 
FILE = "acc/account_list.json"
#IMPORTANT
BASE_DATA = jsp.load_json(FILE)
USERNAME_DATA = [username for username in BASE_DATA.keys()]

class App():

    #Main Window Initialization
    def __init__(self):
        #setup main window
        self.app = tk.Tk()
        self.app.resizable(0,0)
        self.app.title("Simple Login/Signup Form")
        self.app.geometry("400x400")
        #base window
        self.base_window()

        #loop main window
        self.app.mainloop()

    #Child Window
    def base_window(self):
        login_button = tk.Button(self.app,text="Login",width=6,command=self.login_window)
        signup_button = tk.Button(self.app,text="Sign Up",command=self.signup_window)
        login_button.pack()
        signup_button.pack()
        login_button.place(anchor=tk.N,x=150,y=150)
        signup_button.place(anchor=tk.N,x=250,y=150)
    def login_window(self):
        #create new window if is not initialized
        try:
            if self.login_base.state() == "normal":
                self.login_base.focus()
        except:
            self.login_base = tk.Toplevel(self.app)
            self.login_base.title("Login")
            self.login_base.geometry("400x400")

        #gui
        username_label = tk.Label(self.login_base,text="Username/Name")
        password_label = tk.Label(self.login_base,text="Password")
        username_entry = tk.Entry(self.login_base)
        password_entry = tk.Entry(self.login_base,show="*")
        login_button   = tk.Button(self.login_base,text="Login",command=lambda:self.login(username_entry.get(),password_entry.get()))
        
        #placing
        username_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        username_entry.place(relx=0.5, rely=0.35, anchor=tk.CENTER)
        password_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        password_entry.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
        login_button.place(relx=0.5, rely=0.55, anchor=tk.CENTER)       
    def signup_window(self):
        #create new window if is not initialized
        try:
            if self.signup_base.state() == "normal":
                self.signup_base.focus()
        except:
            self.signup_base = tk.Toplevel(self.app)
            self.signup_base.title("Sign Up")
            self.signup_base.geometry("400x400")

        #gui
        username_label = tk.Label(self.signup_base,text="Username/Name")
        age_label      = tk.Label(self.signup_base,text="Age")
        password_label = tk.Label(self.signup_base,text="Password")
        confirm_password_label = tk.Label(self.signup_base,text="Confirm Password")
        username_entry = tk.Entry(self.signup_base)
        age_entry      = tk.Entry(self.signup_base)
        password_entry = tk.Entry(self.signup_base,show="*")
        confirm_password_entry = tk.Entry(self.signup_base,show="*")
        signup_button  = tk.Button(self.signup_base,text="Sign Up",command=lambda:self.signup(username_entry.get(),password_entry.get(),confirm_password_entry.get(),age_entry.get()))
        
        #placing
        username_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        username_entry.place(relx=0.5, rely=0.35, anchor=tk.CENTER)
        age_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        age_entry.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
        password_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        password_entry.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
        confirm_password_label.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
        confirm_password_entry.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
        signup_button.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

    #Processing a login or sign up
    def login(self,username,password):
        global BASE_DATA

        try:
            user_password = BASE_DATA[username]["password"]
        except KeyError:
            messagebox.showerror("Failed Login","Wrong password or username")
        else:
            if password == user_password:
                user_age = BASE_DATA[username]["age"]
                messagebox.showinfo("Succesfull Login",f"Login as {username} with age of {user_age}")
                self.login_base.destroy()
            else:
                messagebox.showerror("Failed Login","Wrong password or username")
                self.login_base.focus()    
    def signup(self,username,password,c_password,age):
        global BASE_DATA

        if username == "" or password == "" or age == "":
            messagebox.showwarning("Failed","Please Fill the Empty")
            self.signup_base.focus()
        else:
            if c_password != password:
                messagebox.showwarning("Failed","Confirm Password is Incorrect")
                self.signup_base.focus()
            else:
                if username in USERNAME_DATA:
                    messagebox.showwarning("Failed","Username has Already Taken")
                    self.signup_base.focus()
                else:
                    BASE_DATA [username] = {"age":age,"password":password}
                    jsp.save_json(BASE_DATA,FILE)
                    messagebox.showinfo("Succesfull Sign Up","Sign Up Succesfull")
                    self.signup_base.destroy()





base = App()