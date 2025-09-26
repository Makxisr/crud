from tkinter import *
from tkinter import Tk
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql



def open_dashboard(username):
    pass

def login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if username == "" or password == "":
        MessageBox.showwarning("Input Error", "Please fill all fields.")
        return

    try:
        # Connect to MySQL database
        con = mysql.connect(
            host="localhost",
            user="root",       # Default XAMPP user
            password="",       # Default no password
            database="Customer"
        )

        cursor = con.cursor()
        query = "SELECT * FROM user WHERE username=%s AND password=%s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result:
            MessageBox.showinfo("Login Successful", f"Welcome {username}!")
            root.destroy()  # Destroy login window

            # ✅ Now safely create new root window
            open_dashboard(username)
        else:
            MessageBox.showerror("Login Failed", "Invalid username or password")

    except mysql.Error as err:
        MessageBox.showerror("Database Error", str(err))

    finally:
        if con.is_connected():
            cursor.close()
            con.close()

# --- Login Window (root) ---
root = tk.Tk()
root.title("Login Page")
root.geometry("350x250")
root.resizable(False, False)

# Username
tk.Label(root, text="Username", font=("Arial", 12)).place(x=30, y=50)
username_entry = tk.Entry(root, width=25, font=("Arial", 10))
username_entry.place(x=120, y=50)

# Password
tk.Label(root, text="Password", font=("Arial", 12)).place(x=30, y=100)
password_entry = tk.Entry(root, show="*", width=25, font=("Arial", 10))
password_entry.place(x=120, y=100)

# Login Button
login_btn = tk.Button(root, text="Login", font=("Arial", 12), width=15, command=login)
login_btn.place(x=100, y=160)

# Run the login window
root.mainloop()


def Refresh():
    # Clear Treeview
    for row in tree.get_children():
        tree.delete(row)

    # Load latest data
    try:
        con = mysql.connect(host="localhost", user="root", password="", database="Customer")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Customer_data")
        rows = cursor.fetchall()

        for row in rows:
            tree.insert('', 'end', values=row)

    except mysql.Error as err:
        MessageBox.showerror("Database Error", str(err))
    finally:
        if con.is_connected():
            cursor.close()
            con.close()

def on_row_selected(event):
    selected_item = tree.focus()  # Get selected item ID
    if selected_item:
        values = tree.item(selected_item, 'values')  # Get row values
        if values:
            id_entry.delete(0, tk.END)
            id_entry.insert(0, values[0])
            name_entry.delete(0, tk.END)
            name_entry.insert(0, values[1])
            phone_entry.delete(0, tk.END)
            phone_entry.insert(0, values[2])
            gender_ComboBox.delete(0, tk.END)
            gender_ComboBox.insert(0, values[3])



def fetch_data():
    # Clear current data in the Treeview
   
    con = mysql.connect(host="localhost", user="root", password="", database="Customer")
    cursor = con.cursor()
    cursor.execute("SELECT id, name, phone, gender FROM Customer_data")
    rows = cursor.fetchall()
    for row in rows:
        tree.insert("", tk.END, values=row)
    cursor.close()
    con.close()

def Quit():
    
    Answer = MessageBox.askyesno("Status","Are you Sure you want to Exit?")
    if Answer:
        root.destroy()
 
def Search():
    id = id_entry.get().strip()

    if id == "":
        MessageBox.showinfo("ALERT", "ID is required to select row!")
    else:
        try:
            con = mysql.connect(host="localhost", user="root", password="", database="Customer")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM Customer_data WHERE id = %s", (id,))
            row = cursor.fetchone()

            if row:
                # Clear previous entries first
                name_entry.delete(0, 'end')
                phone_entry.delete(0, 'end')
                gender_ComboBox.set('')

                # Insert retrieved data
                name_entry.insert(0, row[1])
                phone_entry.insert(0, row[2])
                gender_ComboBox.set(row[3])
            else:
                MessageBox.showinfo("Not Found", f"No record found with ID '{id}'")

        except mysql.Error as err:
            MessageBox.showerror("Database Error", str(err))

        finally:
            if con.is_connected():
                cursor.close()
                con.close()
 
def Cancel():
    id_entry.delete(0, 'end')
    name_entry.delete(0, 'end')
    phone_entry.delete(0, 'end')
    gender_ComboBox.delete(0, 'end')
    
    
     
def Insert():
    id = id_entry.get().strip()
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    gender= gender_ComboBox.get().strip()
  
    if id == "" or name == "" or phone == "":
        MessageBox.showinfo("ALERT", "Please enter all fields")
        return

    try:
        con = mysql.connect(host="localhost", user="root", password="", database="Customer")
        cursor = con.cursor()

        # Check if ID already exists
        cursor.execute("SELECT * FROM Customer_data WHERE id = %s", (id,))
        result = cursor.fetchone()

        if result:
            MessageBox.showerror("Duplicate ID", f"ID '{id}' already exists! MA double na karun!.")
        else:
            cursor.execute("INSERT INTO Customer_data (id, name, phone, gender) VALUES (%s, %s, %s,%s)", (id, name, phone,gender))
            con.commit()

            MessageBox.showinfo("Status", "Successfully Inserted")

            id_entry.delete(0, 'end')
            name_entry.delete(0, 'end')
            phone_entry.delete(0, 'end')
            gender_ComboBox.delete(0, 'end')
            
            Refresh()

    except mysql.Error as err:
        MessageBox.showerror("Database Error", str(err))
    finally:
        if con.is_connected():
            cursor.close()
            con.close()
       
       
def Update():
   id = id_entry.get()
   name = name_entry.get()
   phone = phone_entry.get()
   gender = gender_ComboBox.get()
  
   if(name == "" or phone == "" or gender==""):
       MessageBox.showinfo("ALERT", "Please Insert All Fields!")
   else:
        con = mysql.connect(host="localhost", user="root", password="", database="Customer")
        cursor = con.cursor()
        cursor.execute("update Customer_data set name = '"+ name +"', phone='"+ phone +"', gender='"+ gender +"' where id ='"+ id +"'")
        cursor.execute("commit")
  
        MessageBox.askyesno("Status", "Are you Sure you want to update Person?")
        Refresh()
        
        id_entry.delete(0, 'end')
        name_entry.delete(0, 'end')
        phone_entry.delete(0, 'end')
        gender_ComboBox.delete(0, 'end')
        con.close()
       
def Del():
  
   if(id_entry.get() == ""):
       MessageBox.showinfo("ALERT", "Please enter ID to delete row")
   else:
       con = mysql.connect(host="localhost", user="root", password="", database="Customer")
       cursor = con.cursor()
       cursor.execute("delete from Customer_data where id='"+ id_entry.get() +"'")
       cursor.execute("commit")
  
       
  
       MessageBox.showwarning("Status", "Record Deleted!")
       Refresh()
       
       id_entry.delete(0, 'end')
       name_entry.delete(0, 'end')
       phone_entry.delete(0, 'end')
       gender_ComboBox.delete(0, 'end')
       con.close()




       
root = Tk()
root.geometry("900x800")
root.title("SIMPLE DATA CRUD Operations")
id = Label(root, text="Enter ID:", font=("verdana 15"))
id.place(x=50, y=30)
id_entry = Entry(root, font=("verdana 15"))
id_entry.place(x=150, y=30)
btnSearch= Button(root, text="Search", command=Search, font=("verdana 10")).place(x=420, y=25)
  
name = Label(root, text="Name:", font=("verdana 15"))
name.place(x=50, y=80)
name_entry = Entry(root, font=("verdana 15"))
name_entry.place(x=150, y=80)
btnInsert = Button(root, text="  Add  ", command=Insert, font=("verdana 10")).place(x=420, y=60)

phone = Label(root, text="Phone:", font=("verdana 15"))
phone.place(x=50, y=130)
phone_entry= Entry(root, font=("verdana 15"))
phone_entry.place(x=150, y=130)

gender_ComboBox = Label(root, text="Gender: ", font=("Verdana 15") )
gender_ComboBox.place(x=50, y=180)
gender_ComboBox=ttk.Combobox(root, text="Gender", values=["Male","Female"],font=("Verdana 14"))
gender_ComboBox.place(x=150, y=180,)
gender_ComboBox.set("")


btnDelete = Button(root, text=" Delete", command=Del, font=("verdana 10")).place(x=420, y=95)
btnUpdate = Button(root, text="Update", command=Update, font=("verdana 10")).place(x=420, y=130)
btnCancel= Button(root, text="  Clear ", command=Cancel, font=("verdana 10")).place(x=420, y=165)
btnSearch= Button(root, text="  Quit  ", command=Quit, font=("verdana 10")).place(x=420, y=200)


Title = Label(root, text="CRUD ", font="Verdana 50")
Title.place(x=500, y=50)
root.configure(bg ="light grey")
subtitle = Label(root, text="SIMPLE DATA ENTRY SYSTEM", font="Arial 18")
subtitle.place(x=500, y=150)


frame = ttk.Frame(root, padding=0)
frame.pack(side=LEFT)

# Treeview widget
tree = ttk.Treeview(frame, columns=("Id", "Name", "Phone","Gender"), show="headings")
tree.heading("Id", text="ID")
tree.heading("Name", text="Name")
tree.heading("Phone", text="Phone")
tree.heading("Gender", text="Gender")
tree.column("Id", anchor=CENTER)
tree.column("Name", anchor=CENTER)
tree.column("Phone", anchor=CENTER)
tree.column("Gender", anchor=CENTER)


scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)
tree.pack(fill=tk.BOTH, expand=True)

tree.bind("<ButtonRelease-1>", on_row_selected)
root.after(0, fetch_data)
root.after(6000, Refresh)

root.mainloop()








