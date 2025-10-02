from tkinter import *
from tkinter import Tk
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import subprocess




def exit_login():
    login_window.destroy()


def register():
    login_window.destroy()
    subprocess.Popen(["python", "C:/Users/Marjorie Geneve/OneDrive/Desktop/Crud/register.py"])
     
def check_login():
    username = username_entry.get()
    password = password_entry.get()
    # Simple check, you can replace with MySQL check
    con = mysql.connect(host="localhost", user="root", password="", database="student")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM user WHERE username = %s AND password = %s", (username, password))
    result = cursor.fetchone()
    if result:
        MessageBox.showinfo("Login Success",f"Welcome! {username}")
        login_window.destroy()
        subprocess.Popen(["python", "C:/Users/Marjorie Geneve/OneDrive/Desktop/Crud/simple_data_entry.py"])
    else:
        MessageBox.showerror("Login Failed", "Invalid username or password")

        cursor.close()
        con.close()
        
def cancel_button():
    username_entry.delete(0, 'end')
    password_entry.delete(0, 'end')

login_window = Tk()
login_window.geometry("400x600")
login_window.config(bg="light grey")
login_window.title("Administrator Log In")
login_window.wm_attributes("-transparentcolor", 'green') 

admin_image = tk.PhotoImage(file="C:/Users/Marjorie Geneve/OneDrive/Desktop/Crud/admin1.png")

head = Label(login_window, image=admin_image, font=("Sarif 15")).pack(padx=5,pady=5)



Label(login_window, text="Username", bg="light grey", font=("Verdana", 14)).pack(pady=5)
username_entry = Entry(login_window, font=("Verdana", 14))
username_entry.pack(pady=5)

Label(login_window, text="Password",bg="light grey", font=("Verdana", 14)).pack(pady=5)
password_entry = Entry(login_window, show='*', font=("Verdana", 14))
password_entry.pack(pady=5)



Button(login_window, text="Login", command=check_login,width=23,bg='blue', fg='white', font=("Verdana", 12)).pack(pady=5)
Button(login_window, text="Register", command=register,width=8,bg='light green', fg='black', font=("Verdana", 12)).place(x=300, y=10)
Button(login_window, text="Exit", command=exit_login,width=23,bg='red', fg='white',font=("Verdana", 12)).pack(pady=5)



login_window.mainloop()





#LOG IN END CODE



