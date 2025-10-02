from tkinter import *
from tkinter import Tk
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import subprocess



def login():
    login_window.destroy()
    subprocess.Popen(["python", "C:/Users/Marjorie Geneve/OneDrive/Desktop/Crud/login.py"])

def exit_login():
    login_window.destroy()


def register():
    name = reg_username_entry.get().strip()
    password = reg_password_entry.get().strip()
    regname = fname_entry.get().strip()
    if (id=='' or name=='' or password=='' or regname==''):
        MessageBox.showwarning("Warning","Please full up all Fields!")
        return
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="student")
        cursor = con.cursor()

    
        cursor.execute("INSERT INTO user (username,password,regname) VALUES (%s, %s,%s)",(name, password,regname,))
        con.commit()
        cursor.close()
        con.close()

    MessageBox.showinfo("Status", f"Registered {name} User Successfully!")
    login_window.destroy()
    subprocess.Popen(["python", "C:/Users/Marjorie Geneve/OneDrive/Desktop/Crud/login.py"])

        
def cancel_button():
    reg_username_entry.delete(0, 'end')
    reg_password_entry.delete(0, 'end')
    fname_entry.delete(0, 'end')

login_window = Tk()
login_window.geometry("400x700")
login_window.config(bg="light grey")
login_window.title("Administrator Sign Up")
login_window.wm_attributes("-transparentcolor", 'green') 

admin_image = tk.PhotoImage(file="C:/Users/Marjorie Geneve/OneDrive/Desktop/Crud/admin1.png")

head = Label(login_window, image=admin_image, font=("Sarif 15")).pack(padx=5,pady=5)



Label(login_window, text="Register Username", bg="light grey", font=("Verdana", 14)).pack(pady=5)
reg_username_entry = Entry(login_window, font=("Verdana", 14))
reg_username_entry.pack(pady=5)

Label(login_window, text="Register Password", bg="light grey", font=("Verdana", 14)).pack(pady=5)
reg_password_entry = Entry(login_window, show='*', font=("Verdana", 14))
reg_password_entry.pack(pady=5)

Label(login_window, text="Register Fullname",bg="light grey", font=("Verdana", 14)).pack(pady=5)
fname_entry = Entry(login_window, font=("Verdana", 14))
fname_entry.pack(pady=5)

Button(login_window, text="Register", command=register,width=23,bg='light green', fg='black', font=("Verdana", 12)).pack(pady=5)
Button(login_window, text="Return Sign In", command=login,width=23,bg='blue', fg='white', font=("Verdana", 12)).pack(pady=5)
Button(login_window, text="Exit", command=exit_login,width=23,bg='red', fg='white',font=("Verdana", 12)).pack(pady=5)
login_window.mainloop()





#LOG IN END CODE



