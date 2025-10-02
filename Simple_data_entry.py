from tkinter import *
from tkinter import Tk
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import subprocess



def exit_login():
    login_window.destroy()
    root.destroy()
    

def get_row_count():
     
     con = mysql.connect(host="localhost", user="root", password="", database="student")
     cursor = con.cursor()
     cursor.execute("SELECT COUNT(*) FROM student_data")
     row_count = cursor.fetchone()[0]
     return (row_count)
     cursor.close()
     con.close()




def update_count():
    count = get_row_count()
    if count is not None:
        label_result.config(text=f"Number of Students: {count}")
     
     
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
        subprocess.Popen(["python", "toplevel.py"])
    else:
        MessageBox.showerror("Login Failed", "Invalid username or password")

        cursor.close()
        con.close()
        
def cancel_button():
    username_entry.delete(0, 'end')
    password_entry.delete(0, 'end')


#LOG IN END CODE





def Refresh():
    # Clear Treeview
    for row in tree.get_children():
        tree.delete(row)

    # Load latest data
    try:
        con = mysql.connect(host="localhost", user="root", password="", database="student")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM student_data")
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
            course_ComboBox.delete(0, tk.END)
            course_ComboBox.insert(0, values[4])



def fetch_data():
    # Clear current data in the Treeview
   
    con = mysql.connect(host="localhost", user="root", password="", database="student")
    cursor = con.cursor()
    cursor.execute("SELECT id, name, phone, gender, course FROM student_data")
    rows = cursor.fetchall()
    for row in rows:
        tree.insert("", tk.END, values=row)
    cursor.close()
    con.close()

def Quit():
    
    Answer = MessageBox.askyesno("Status","Are you Sure you want to Exit?")
    if Answer:
        root.destroy()
        subprocess.Popen(["python", "C:/Users/Marjorie Geneve/OneDrive/Desktop/Crud/login.py"])
 
def Search():
    id = id_entry.get().strip()

    if id == "":
        MessageBox.showinfo("ALERT", "ID is required to select row!")
    else:
        try:
            con = mysql.connect(host="localhost", user="root", password="", database="student")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM student_data WHERE id = %s", (id,))
            row = cursor.fetchone()

            if row:
                # Clear previous entries first
                name_entry.delete(0, 'end')
                phone_entry.delete(0, 'end')
                gender_ComboBox.set('')
                course_ComboBox.set('')

                # Insert retrieved data
                name_entry.insert(0, row[1])
                phone_entry.insert(0, row[2])
                gender_ComboBox.set(row[3])
                course_ComboBox.set(row[4])
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
    course_ComboBox.delete(0, 'end')
    
    
     
def Insert():
    id = id_entry.get().strip()
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    gender= gender_ComboBox.get().strip()
    course= course_ComboBox.get().strip()
  
    if id == "" or name == "" or phone == "" or gender == "" or course == "":
        MessageBox.showinfo("ALERT", "Please enter all fields")
        return

    try:
        con = mysql.connect(host="localhost", user="root", password="", database="student")
        cursor = con.cursor()

        # Check if ID already exists
        cursor.execute("SELECT * FROM student_data WHERE id = %s", (id,))
        result = cursor.fetchone()

        if result:
            MessageBox.showerror("Duplicate ID", f"ID '{id}' already exists! MA double na karun!.")
        else:
            cursor.execute("INSERT INTO student_data (id, name, phone, gender,course) VALUES (%s, %s, %s,%s,%s)", (id, name, phone,gender,course))
            con.commit()

            MessageBox.showinfo("Status", "New Student Successfully Added!")

            id_entry.delete(0, 'end')
            name_entry.delete(0, 'end')
            phone_entry.delete(0, 'end')
            gender_ComboBox.delete(0, 'end')
            course_ComboBox.delete(0, 'end')
            
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
   course = course_ComboBox.get()
  
   if(name == "" or phone == "" or gender=="" or course==""):
       MessageBox.showinfo("ALERT", "Please Insert All Fields!")
   else:
        con = mysql.connect(host="localhost", user="root", password="", database="student")
        cursor = con.cursor()
        cursor.execute("update student_data set name ='"+ name +"', phone='"+ phone +"', gender='"+ gender +"', course='"+ course +"' where id ='"+ id +"'")
        cursor.execute("commit")
  
        MessageBox.showwarning("Status", "Record has been Change!")
        Refresh()
        
        id_entry.delete(0, 'end')        
        name_entry.delete(0, 'end')
        phone_entry.delete(0, 'end')
        gender_ComboBox.delete(0, 'end')
        course_ComboBox.delete(0, 'end')
        con.close()
       
def Del():
  
   if(id_entry.get() == ""):
       MessageBox.showinfo("ALERT", "Please enter ID to delete row")
   else:
       con = mysql.connect(host="localhost", user="root", password="", database="student")
       cursor = con.cursor()
       cursor.execute("delete from student_data where id='"+ id_entry.get() +"'")
       cursor.execute("commit")
  
       
  
       MessageBox.showwarning("Status", "Record Deleted!")
       Refresh()
       
       id_entry.delete(0, 'end')
       name_entry.delete(0, 'end')
       phone_entry.delete(0, 'end')
       gender_ComboBox.delete(0, 'end')
       course_ComboBox.delete(0, 'end')
       con.close()




       
root = Tk()
root.geometry("1000x510")
root.title("SIMPLE DATA CRUD Operations")
id = Label(root, text="Enter ID:", font=("verdana 15"))
id.place(x=50, y=50)
id_entry = Entry(root, font=("verdana 15"))
id_entry.place(x=150, y=50)
s_icon =tk.PhotoImage(file="C:/Users/Marjorie Geneve/OneDrive/Desktop/Crud/search.png" , height=30, width=30)
btnSearch= Button(root, text="Search", command=Search, image=s_icon, height= 30, width=30, font=("verdana 10")).place(x=50, y=5)
  
name = Label(root, text="Name:", font=("verdana 15"))
name.place(x=50, y=90)
name_entry = Entry(root, font=("verdana 15"))
name_entry.place(x=150, y=90)
a_icon =tk.PhotoImage(file="C:/Users/Marjorie Geneve/OneDrive/Desktop/Crud/add.png" , height=30, width=80)
btnInsert = Button(root, text="  Add  ", command=Insert, bg="blue",fg="white", font=("verdana 10")).place(x=90, y=5)

phone = Label(root, text="Phone:", font=("verdana 15"))
phone.place(x=50, y=130)
phone_entry= Entry(root, font=("verdana 15"))
phone_entry.place(x=150, y=130)

gender_ComboBox = Label(root, text="Gender: ", font=("Verdana 15"))
gender_ComboBox.place(x=50, y=170)
gender_ComboBox=ttk.Combobox(root, text="Gender", values=["Male","Female"],font=("Verdana 14"))
gender_ComboBox.place(x=150, y=170,)
gender_ComboBox.set("")

course_ComboBox = Label(root, text="Course: ", font=("Verdana 15") )
course_ComboBox.place(x=50, y=210)
course_ComboBox=ttk.Combobox(root, text="Course", values=["BSA","BSBA","BSHM","BSCRIM","BSED","BEED","BSPSYCH","BSCE","BSECE","BSIT","BLIS","BSP","BSMT","BSRT","BSMID","CARGIVING"],font=("Verdana 14"))
course_ComboBox.place(x=150, y=210,)

d_icon =tk.PhotoImage(file="C:/Users/Marjorie Geneve/OneDrive/Desktop/Crud/delete.png" , height=30, width=90)
btnDelete = Button(root, text=" Delete", command=Del,bg="red",fg="black", font=("verdana 10")).place(x=150, y=5)
u_icon =tk.PhotoImage(file="C:/Users/Marjorie Geneve/OneDrive/Desktop/Crud/update.png" , height=30, width=80)
btnUpdate = Button(root, text="Update", command=Update,bg="green",fg="white", font=("verdana 10")).place(x=212, y=5)
c_icon =tk.PhotoImage(file="C:/Users/Marjorie Geneve/OneDrive/Desktop/Crud/clear.png" , height=30, width=80)
btnCancel= Button(root, text="  Clear ", command=Cancel,bg="grey",fg="white", font=("verdana 10")).place(x=273, y=5)
e_icon =tk.PhotoImage(file="C:/Users/Marjorie Geneve/OneDrive/Desktop/Crud/exit.png" , height=30, width=80)
btnSearch= Button(root, text="  Quit  ", command=Quit, bg="yellow",fg="black", font=("verdana 10")).place(x=400, y=5)
r_icon =tk.PhotoImage(file="C:/Users/Marjorie Geneve/OneDrive/Desktop/Crud/refresh.png" , height=30, width=80)
btn_refresh = tk.Button(root, text="Refresh", bg="light blue",fg="black",command=update_count, font=("verdana 10")).place(x=336,y=5)

Title = Label(root, text="CRUD ", font="Verdana 53")
Title.place(x=750, y=25)
root.configure(bg ="light grey")
subtitle = Label(root, text="SIMPLE DATA ENTRY SYSTEM", font="Arial 12")
subtitle.place(x=750, y=100)




label_result = tk.Label(root, text="List: --", font=("Arial", 12))
label_result.place(x=5, y=250)




# Initial fetch
update_count()

frame = ttk.Frame(root, padding=5)
frame.pack(side=BOTTOM)

# Treeview widget
tree = ttk.Treeview(frame, columns=("Id", "Name", "Phone","Gender","Course"), show="headings")
tree.heading("Id", text="ID")
tree.heading("Name", text="Name")
tree.heading("Phone", text="Phone")
tree.heading("Gender", text="Gender")
tree.heading("Course", text="Course")
tree.column("Id", anchor=CENTER)
tree.column("Name", anchor=CENTER)
tree.column("Phone", anchor=CENTER)
tree.column("Gender", anchor=CENTER)
tree.column("Course", anchor=CENTER)


scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tree.pack(fill=tk.BOTH, expand=True)

tree.bind("<ButtonRelease-1>", on_row_selected)
root.after(0, fetch_data)
root.after(6000, Refresh)

root.mainloop()








