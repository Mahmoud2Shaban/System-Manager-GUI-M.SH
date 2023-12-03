from tkinter import *
from tkinter import messagebox
import os
import sqlite3
from tkinter import ttk
import tempfile
import time


roots= Tk()
roots.title("Login System ")
roots.geometry("1500x800+0+0")
roots.config(bg="#03a9f4")

        #========== login frame ======
employee_id = StringVar()
password = StringVar()

login_frame = Frame(roots,bd=2,relief=RIDGE,bg="white")
login_frame.place(x=650,y=90,width=350,height=500)

#======================= All Function ==================

def login():
    con = sqlite3.connect(database=r'ims.db')
    cur = con.cursor()
    try:
        if employee_id.get()=="" or password.get()=="":
            messagebox.showerror("Error","All fields are required",parent=roots)
        else:
            cur.execute("select utype from employee where eid=? and pass=?",(employee_id.get(),password.get()))
            user = cur.fetchone()
            if user ==None:
                messagebox.showerror("Error","Invalid Username/Password",parent=roots)
            else:
                if user[0]== "Admin":
                    roots.destroy()
                    #os.system("python text.py")
                    #=============================================================================
                    root = Tk()
                    root.geometry("1500x800+0+0")
                    root.title("Management System *** Developed M.SH ")
                    root.config(bg="white")
                    # ----------title----------
                    title = Label(root, text="***** Management System *****", font=("times new roman", 40, "bold"),
                                  bg="#010c48", fg="white", anchor="w", padx=20)
                    title.place(x=0, y=0, relwidth=1, height=70)

                    def logout():
                        root.destroy()
                        os.system("python electronics.py")

                        # --------btn_logout----------

                    btn_logout = Button(root, text="Logout", command=logout, font=("times new roman", 15, "bold"),
                                        bg="yellow", cursor="hand2")
                    btn_logout.place(x=1250, y=10, height=50, width=150)
                    # -------clock---------------
                    lbl_clock = Label(root,
                                      text="**Welcome to Management System***\t\t Data: DD/MM/YYYY\t\t Time: HH:MM:SS",
                                      font=("times new roman", 15), bg="#4d636d", fg="white")
                    lbl_clock.place(x=0, y=70, relwidth=1, height=30)

                    # ============= Functions==========
                    def employee():
                        roots = Toplevel()
                        roots.geometry("1280x500+220+130")
                        roots.title("Management System *** Developed M.SH ")
                        roots.config(bg="white")
                        roots.focus_force()
                        roots.resizable(False, False)
                        # =========================
                        con = sqlite3.connect(database=r'ims.db')
                        cur = con.cursor()
                        cur.execute(
                            "CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,contact text,dob text,doj text,pass text,utype text,address text,salary text)")
                        con.commit()
                        # ======All Variables=======
                        var_searchby = StringVar()
                        var_searchtxt = StringVar()

                        var_emp_id = StringVar()
                        var_gender = StringVar()
                        var_contact = StringVar()
                        var_name = StringVar()
                        var_dob = StringVar()
                        var_doj = StringVar()
                        var_email = StringVar()
                        var_pass = StringVar()
                        var_utype = StringVar()
                        var_salary = StringVar()

                        # =============================================================================
                        # =============================================================================

                        # =====searchframe=========
                        searchframe = LabelFrame(roots, text="Search Employee", font=("goudy old style", 12, "bold"),
                                                 bd=2, relief=RIDGE, bg="white")
                        searchframe.place(x=250, y=20, width=600, height=70)

                        # =========================================================================================================
                        def show():
                            con = sqlite3.connect(database=r'ims.db')
                            cur = con.cursor()
                            try:
                                cur.execute("select * from employee")
                                rows = cur.fetchall()
                                Employeetable.delete(*Employeetable.get_children())
                                for row in rows:
                                    Employeetable.insert("", END, values=row)
                            except Exception as ex:
                                messagebox.showerror("Error", f"Error due to : {str(ex)}")

                        def add():
                            con = sqlite3.connect(database=r'ims.db')
                            cur = con.cursor()
                            try:
                                if var_emp_id.get() == "":
                                    messagebox.showerror("Error", "Employee ID Must be required", parent=roots)
                                else:
                                    cur.execute("Select * from employee where eid=?", (var_emp_id.get(),))
                                    row = cur.fetchone()
                                    if row != None:
                                        messagebox.showerror("Error",
                                                             "This Employee Id already assigned , try different",
                                                             parent=roots)
                                    else:
                                        cur.execute(
                                            "Insert into employee (eid,name,email,gender,contact,dob,doj,pass,utype,address,salary) values(?,?,?,?,?,?,?,?,?,?,?)",
                                            (
                                                var_emp_id.get(),
                                                var_name.get(),
                                                var_email.get(),
                                                var_gender.get(),
                                                var_contact.get(),
                                                var_dob.get(),
                                                var_doj.get(),
                                                var_pass.get(),
                                                var_utype.get(),
                                                txt_address.get('1.0', END),
                                                var_salary.get(),
                                            ))
                                        con.commit()
                                        messagebox.showinfo("Success", "Employee Addedd Successfully", parent=roots)
                                        show()
                            except Exception as ex:
                                messagebox.showerror("Error", f"Error due to : {str(ex)}")

                        def get_date(ev):
                            f = Employeetable.focus()
                            content = (Employeetable.item(f))
                            row = content['values']
                            var_emp_id.set(row[0])
                            var_name.set(row[1])
                            var_email.set(row[2])
                            var_gender.set(row[3])
                            var_contact.set(row[4])
                            var_dob.set(row[5])
                            var_doj.set(row[6])
                            var_pass.set(row[7])
                            var_utype.set(row[8])
                            txt_address.delete('1.0', END)
                            txt_address.insert(END, row[9])
                            var_salary.set(row[10])

                        def update():
                            con = sqlite3.connect(database=r'ims.db')
                            cur = con.cursor()
                            try:
                                if var_emp_id.get() == "":
                                    messagebox.showerror("Error", "Employee ID Must be required", parent=roots)
                                else:
                                    cur.execute("Select * from employee where eid=?", (var_emp_id.get(),))
                                    row = cur.fetchone()
                                    if row == None:
                                        messagebox.showerror("Error", "Invalid Employee ID", parent=roots)
                                    else:
                                        cur.execute(
                                            "Update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? where eid=?",
                                            (
                                                var_name.get(),
                                                var_email.get(),
                                                var_gender.get(),
                                                var_contact.get(),
                                                var_dob.get(),
                                                var_doj.get(),
                                                var_pass.get(),
                                                var_utype.get(),
                                                txt_address.get('1.0', END),
                                                var_salary.get(),
                                                var_emp_id.get(),
                                            ))
                                        con.commit()
                                        messagebox.showinfo("Success", "Employee Updated Successfully", parent=roots)
                                        show()
                            except Exception as ex:
                                messagebox.showerror("Error", f"Error due to : {str(ex)}")

                        def delete():
                            con = sqlite3.connect(database=r'ims.db')
                            cur = con.cursor()
                            try:
                                if var_emp_id.get() == "":
                                    messagebox.showerror("Error", "Employee ID Must be required", parent=roots)
                                else:
                                    cur.execute("Select * from employee where eid=?", (var_emp_id.get(),))
                                    row = cur.fetchone()
                                    if row == None:
                                        messagebox.showerror("Error", "Invalid Employee ID", parent=roots)
                                    else:
                                        op = messagebox.askyesno("Confirm", "Do you really want to delete?",
                                                                 parent=roots)
                                        if op == True:
                                            cur.execute("delete from employee where eid=?", (var_emp_id.get(),))
                                            con.commit()
                                            messagebox.showinfo("Delete", "Employee Deleted Successfully", parent=roots)
                                            clear()
                            except Exception as ex:
                                messagebox.showerror("Error", f"Error due to : {str(ex)}")

                        def clear():
                            var_emp_id.set("")
                            var_name.set("")
                            var_email.set("")
                            var_gender.set("Select")
                            var_contact.set("")
                            var_dob.set("")
                            var_doj.set("")
                            var_pass.set("")
                            var_utype.set("Admin")
                            txt_address.delete('1.0', END)
                            var_salary.set("")
                            var_searchtxt.set("")
                            var_searchby.set("Select")
                            show()

                        def search():
                            con = sqlite3.connect(database=r'ims.db')
                            cur = con.cursor()
                            try:
                                if var_searchby.get() == "Select":
                                    messagebox.showerror("Error", "Select Search By option", parent=roots)
                                elif var_searchtxt.get() == "":
                                    messagebox.showerror("Error", "Search input should be required", parent=roots)

                                    # cur.execute("select * from employee where"+str(self.var_searchby.get()+" LIKE '%")+str(self.var_searchtxt.get())+"%'")


                                else:
                                    cur.execute(
                                        "select * from employee where " + str(var_searchby.get() + " LIKE '%") + str(
                                            var_searchtxt.get()) + "%'")
                                    rows = cur.fetchall()
                                    if len(rows) != 0:
                                        Employeetable.delete(*Employeetable.get_children())
                                        for row in rows:
                                            Employeetable.insert("", END, values=row)
                                    else:
                                        messagebox.showerror("Error", "No record found!", parent=roots)
                            except Exception as ex:
                                messagebox.showerror("Error", f"Error due to : {str(ex)}")

                        # ===options===
                        cmb_search = ttk.Combobox(searchframe, textvariable=var_searchby,
                                                  values=("Select", "Email", "Name", "Contact"), state="readonly",
                                                  justify=CENTER,
                                                  font=("goudy old style", 15))
                        cmb_search.place(x=10, y=10, width=180)
                        cmb_search.current(0)

                        txt_search = Entry(searchframe, textvariable=var_searchtxt, font=("goudy old style", 15),
                                           bg="lightyellow")
                        txt_search.place(x=200, y=10)

                        btn_search = Button(searchframe, text="Search", command=search, font=("goudy old style", 15),
                                            bg="#4caf50",
                                            fg="white", cursor="hand2")
                        btn_search.place(x=410, y=9, width=150, height=30)

                        # ======title=======
                        title = Label(roots, text="Employee Details", bg="#0f4d7d", font=("goudy old style", 15),
                                      fg="white")
                        title.place(x=50, y=100, width=1180)

                        # ======content========
                        # ======row1===========
                        lbl_empid = Label(roots, text="Emp ID", bg="white", font=("goudy old style", 15))
                        lbl_empid.place(x=50, y=150)
                        lbl_gender = Label(roots, text="Gender", bg="white", font=("goudy old style", 15))
                        lbl_gender.place(x=350, y=150)
                        lbl_contact = Label(roots, text="Contact", bg="white", font=("goudy old style", 15))
                        lbl_contact.place(x=750, y=150)

                        txt_empid = Entry(roots, textvariable=var_emp_id, bg="lightyellow",
                                          font=("goudy old style", 15))
                        txt_empid.place(x=150, y=150, width=180)
                        cmb_gender = ttk.Combobox(roots, textvariable=var_gender,
                                                  values=("Select", "Male", "Female", "Other"),
                                                  state="readonly", justify=CENTER, font=("goudy old style", 15))
                        cmb_gender.place(x=500, y=150, width=180)
                        cmb_gender.current(0)
                        txt_contact = Entry(roots, textvariable=var_contact, bg="lightyellow",
                                            font=("goudy old style", 15))
                        txt_contact.place(x=850, y=150, width=180)

                        # ======row2===========
                        lbl_name = Label(roots, text="Name", bg="white", font=("goudy old style", 15))
                        lbl_name.place(x=50, y=190)
                        lbl_dob = Label(roots, text="D.O.B", bg="white", font=("goudy old style", 15))
                        lbl_dob.place(x=350, y=190)
                        lbl_doj = Label(roots, text="D.O.J", bg="white", font=("goudy old style", 15))
                        lbl_doj.place(x=750, y=190)

                        txt_name = Entry(roots, textvariable=var_name, bg="lightyellow", font=("goudy old style", 15))
                        txt_name.place(x=150, y=190, width=180)
                        txt_dob = Entry(roots, textvariable=var_dob, bg="lightyellow", font=("goudy old style", 15))
                        txt_dob.place(x=500, y=190, width=180)
                        txt_doj = Entry(roots, textvariable=var_doj, bg="lightyellow", font=("goudy old style", 15))
                        txt_doj.place(x=850, y=190, width=180)

                        # ======row3===========
                        lbl_email = Label(roots, text="Email", bg="white", font=("goudy old style", 15))
                        lbl_email.place(x=50, y=230)
                        lbl_pass = Label(roots, text="Password", bg="white", font=("goudy old style", 15))
                        lbl_pass.place(x=350, y=230)
                        lbl_utype = Label(roots, text="User Type", bg="white", font=("goudy old style", 15))
                        lbl_utype.place(x=750, y=230)

                        txt_email = Entry(roots, textvariable=var_email, bg="lightyellow", font=("goudy old style", 15))
                        txt_email.place(x=150, y=230, width=180)
                        cmb_utype = ttk.Combobox(roots, textvariable=var_utype, values=("Admin", "Employee"),
                                                 state="readonly",
                                                 justify=CENTER, font=("goudy old style", 15))
                        cmb_utype.place(x=850, y=230, width=180)
                        cmb_utype.current(0)
                        txt_pass = Entry(roots, textvariable=var_pass, bg="lightyellow", font=("goudy old style", 15))
                        txt_pass.place(x=500, y=230, width=180)

                        # ======row4===========
                        lbl_address = Label(roots, text="Address", bg="white", font=("goudy old style", 15))
                        lbl_address.place(x=50, y=270)
                        lbl_salary = Label(roots, text="Salary", bg="white", font=("goudy old style", 15))
                        lbl_salary.place(x=500, y=270)

                        txt_address = Text(roots, bg="lightyellow", font=("goudy old style", 15))
                        txt_address.place(x=150, y=270, width=300, height=60)
                        txt_salary = Entry(roots, textvariable=var_salary, bg="lightyellow",
                                           font=("goudy old style", 15))
                        txt_salary.place(x=600, y=270, width=180)

                        # ======Buttons=========
                        btn_add = Button(roots, text="Save", command=add, font=("goudy old style", 15), bg="#2196f3",
                                         fg="white",
                                         cursor="hand2")
                        btn_add.place(x=500, y=305, width=110, height=28)
                        btn_update = Button(roots, text="Update", command=update, font=("goudy old style", 15),
                                            bg="#4caf50",
                                            fg="white", cursor="hand2")
                        btn_update.place(x=620, y=305, width=110, height=28)
                        btn_delete = Button(roots, text="Delete", command=delete, font=("goudy old style", 15),
                                            bg="#f44336",
                                            fg="white", cursor="hand2")
                        btn_delete.place(x=740, y=305, width=110, height=28)
                        btn_clear = Button(roots, text="Clear", command=clear, font=("goudy old style", 15),
                                           bg="#607d8b",
                                           fg="white", cursor="hand2")
                        btn_clear.place(x=860, y=305, width=110, height=28)

                        # =========Employee Details===
                        emp_frame = Frame(roots, bd=3, relief=RIDGE)
                        emp_frame.place(x=0, y=350, relwidth=1, height=150)

                        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
                        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

                        Employeetable = ttk.Treeview(emp_frame, columns=(
                        "eid", "name", "email", "gender", "contact", "dob", "doj", "pass", "utype", "address",
                        "salary"),
                                                     yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
                        scrollx.pack(side=BOTTOM, fill=X)
                        scrolly.pack(side=RIGHT, fill=Y)
                        scrollx.config(command=Employeetable.xview)
                        scrolly.config(command=Employeetable.yview)

                        Employeetable.heading("eid", text="EMP ID")
                        Employeetable.heading("name", text="Name")
                        Employeetable.heading("email", text="Email")
                        Employeetable.heading("gender", text="Gender")
                        Employeetable.heading("contact", text="Contact")
                        Employeetable.heading("dob", text="D.O.B")
                        Employeetable.heading("doj", text="D.O.J")
                        Employeetable.heading("pass", text="Password")
                        Employeetable.heading("utype", text="User Type")
                        Employeetable.heading("address", text="Address")
                        Employeetable.heading("salary", text="Salary")

                        Employeetable["show"] = "headings"

                        Employeetable.column("eid", width=90)
                        Employeetable.column("name", width=200)
                        Employeetable.column("email", width=200)
                        Employeetable.column("gender", width=100)
                        Employeetable.column("contact", width=140)
                        Employeetable.column("dob", width=100)
                        Employeetable.column("doj", width=100)
                        Employeetable.column("pass", width=150)
                        Employeetable.column("utype", width=100)
                        Employeetable.column("address", width=200)
                        Employeetable.column("salary", width=200)

                        Employeetable.pack(fill=BOTH, expand=1)
                        Employeetable.bind("<ButtonRelease-1>", get_date)
                        show()

                    # ==================================================================================
                    def supplier():
                        frm = Toplevel()
                        frm.geometry("1280x500+220+130")
                        frm.title("Management System *** Developed M.SH ")
                        frm.config(bg="white")
                        frm.focus_force()
                        frm.resizable(False, False)
                        # =========================
                        con = sqlite3.connect(database=r'ims.db')
                        cur = con.cursor()
                        cur.execute(
                            "CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT,name text,contact text,desc text)")
                        con.commit()
                        # ======All Variables=======
                        var_searchtxt = StringVar()

                        var_sup_invoice = StringVar()
                        var_name = StringVar()
                        var_contact = StringVar()

                        # ====================================================================================
                        def add():
                            con = sqlite3.connect(database=r'ims.db')
                            cur = con.cursor()
                            try:
                                if var_sup_invoice.get() == "":
                                    messagebox.showerror("Error", "Invoice no. must be required", parent=frm)
                                else:
                                    cur.execute("Select * from supplier where invoice=?", (var_sup_invoice.get(),))
                                    row = cur.fetchone()
                                    if row != None:
                                        messagebox.showerror("Error", "Invoice no. already assigned , try different",
                                                             parent=frm)
                                    else:
                                        cur.execute("Insert into supplier (invoice,name,contact,desc) values(?,?,?,?)",
                                                    (
                                                        var_sup_invoice.get(),
                                                        var_name.get(),
                                                        var_contact.get(),
                                                        txt_desc.get('1.0', END),

                                                    ))
                                        con.commit()
                                        messagebox.showinfo("Success", "Supplier Addedd Successfully", parent=frm)
                                        show()



                            except Exception as ex:
                                messagebox.showerror("Error", f"Error due to : {str(ex)}")

                        def show():
                            con = sqlite3.connect(database=r'ims.db')
                            cur = con.cursor()
                            try:
                                cur.execute("select * from supplier")
                                rows = cur.fetchall()
                                Suppliertable.delete(*Suppliertable.get_children())
                                for row in rows:
                                    Suppliertable.insert("", END, values=row)
                            except Exception as ex:
                                messagebox.showerror("Error", f"Error due to : {str(ex)}")

                        def get_date(ev):
                            f = Suppliertable.focus()
                            content = (Suppliertable.item(f))
                            row = content['values']
                            var_sup_invoice.set(row[0])
                            var_name.set(row[1])
                            var_contact.set(row[2])
                            txt_desc.delete('1.0', END)
                            txt_desc.insert(END, row[3])

                        def update():
                            con = sqlite3.connect(database=r'ims.db')
                            cur = con.cursor()
                            try:
                                if var_sup_invoice.get() == "":
                                    messagebox.showerror("Error", "Invoicev no. must be required", parent=frm)
                                else:
                                    cur.execute("Select * from supplier where invoice=?", (var_sup_invoice.get(),))
                                    row = cur.fetchone()
                                    if row == None:
                                        messagebox.showerror("Error", "Invalid Invoice no.", parent=frm)
                                    else:
                                        cur.execute("Update supplier set name=?,contact=?,desc=? where invoice=?",
                                                    (
                                                        var_name.get(),
                                                        var_contact.get(),
                                                        txt_desc.get('1.0', END),
                                                        var_sup_invoice.get(),
                                                    ))
                                        con.commit()
                                        messagebox.showinfo("Success", "Supplier Updated Successfully", parent=frm)
                                        show()
                            except Exception as ex:
                                messagebox.showerror("Error", f"Error due to : {str(ex)}")

                        def delete():
                            con = sqlite3.connect(database=r'ims.db')
                            cur = con.cursor()
                            try:
                                if var_sup_invoice.get() == "":
                                    messagebox.showerror("Error", "Invoice no. must be required", parent=frm)
                                else:
                                    cur.execute("Select * from supplier where invoice=?", (var_sup_invoice.get(),))
                                    row = cur.fetchone()
                                    if row == None:
                                        messagebox.showerror("Error", "Invalid Invoice no.", parent=frm)
                                    else:
                                        op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=frm)
                                        if op == True:
                                            cur.execute("delete from supplier where invoice=?",
                                                        (var_sup_invoice.get(),))
                                            con.commit()
                                            messagebox.showinfo("Delete", "Supplier Deleted Successfully", parent=frm)
                                            clear()
                            except Exception as ex:
                                messagebox.showerror("Error", f"Error due to : {str(ex)}")

                        def clear():
                            var_sup_invoice.set("")
                            var_name.set("")
                            var_contact.set("")
                            txt_desc.delete('1.0', END)
                            var_searchtxt.set("")
                            show()

                        def search():
                            con = sqlite3.connect(database=r'ims.db')
                            cur = con.cursor()
                            try:
                                if var_searchtxt.get() == "":
                                    messagebox.showerror("Error", "Invoice no. should be required", parent=frm)
                                else:
                                    cur.execute("select * from supplier where invoice=? ", (var_searchtxt.get(),))
                                    row = cur.fetchone()
                                    if row != None:
                                        Suppliertable.delete(*Suppliertable.get_children())
                                        Suppliertable.insert("", END, values=row)
                                    else:
                                        messagebox.showerror("Error", "No record found!", parent=frm)
                            except Exception as ex:
                                messagebox.showerror("Error", f"Error due to : {str(ex)}")

                        # =====searchframe=========

                        # ===options===
                        lbl_search = Label(frm, text="Invoice No:", bg="white", font=("goudy old style", 15))
                        lbl_search.place(x=790, y=75, width=180)

                        txt_search = Entry(frm, textvariable=var_searchtxt, font=("goudy old style", 15),
                                           bg="lightyellow")
                        txt_search.place(x=940, y=80, width=160)

                        btn_search = Button(frm, text="Search", command=search, font=("goudy old style", 15),
                                            bg="#4caf50",
                                            fg="white", cursor="hand2")
                        btn_search.place(x=1110, y=79, width=110, height=30)

                        # ======title=======
                        title = Label(frm, text="Supplier Details", bg="#0f4d7d", font=("goudy old style", 20, "bold"),
                                      fg="white")
                        title.place(x=50, y=10, width=1180, height=40)

                        # ======content========
                        # ======row1===========
                        lbl_supplier_invoice = Label(frm, text="Invoice NO", bg="white", font=("goudy old style", 15))
                        lbl_supplier_invoice.place(x=50, y=80)
                        txt_supplier_invoice = Entry(frm, textvariable=var_sup_invoice, bg="lightyellow",
                                                     font=("goudy old style", 15))
                        txt_supplier_invoice.place(x=180, y=80, width=180)

                        # ======row2===========
                        lbl_name = Label(frm, text="Name", bg="white", font=("goudy old style", 15))
                        lbl_name.place(x=50, y=120)

                        txt_name = Entry(frm, textvariable=var_name, bg="lightyellow", font=("goudy old style", 15))
                        txt_name.place(x=180, y=120, width=180)

                        # ======row3===========
                        lbl_contact = Label(frm, text="Contact", bg="white", font=("goudy old style", 15))
                        lbl_contact.place(x=50, y=160)

                        txt_contact = Entry(frm, textvariable=var_contact, bg="lightyellow",
                                            font=("goudy old style", 15))
                        txt_contact.place(x=180, y=160, width=180)

                        # ======row4===========
                        lbl_desc = Label(frm, text="Description", bg="white", font=("goudy old style", 15))
                        lbl_desc.place(x=50, y=200)

                        txt_desc = Text(frm, bg="lightyellow", font=("goudy old style", 15))
                        txt_desc.place(x=180, y=200, width=470, height=120)

                        # ======Buttons=========
                        btn_add = Button(frm, text="Save", command=add, font=("goudy old style", 15), bg="#2196f3",
                                         fg="white",
                                         cursor="hand2")
                        btn_add.place(x=180, y=370, width=110, height=35)
                        btn_update = Button(frm, text="Update", command=update, font=("goudy old style", 15),
                                            bg="#4caf50",
                                            fg="white", cursor="hand2")
                        btn_update.place(x=300, y=370, width=110, height=35)
                        btn_delete = Button(frm, text="Delete", command=delete, font=("goudy old style", 15),
                                            bg="#f44336",
                                            fg="white", cursor="hand2")
                        btn_delete.place(x=420, y=370, width=110, height=35)
                        btn_clear = Button(frm, text="Clear", command=clear, font=("goudy old style", 15), bg="#607d8b",
                                           fg="white", cursor="hand2")
                        btn_clear.place(x=540, y=370, width=110, height=35)

                        # =========Supplier Details===
                        emp_frame = Frame(frm, bd=3, relief=RIDGE)
                        emp_frame.place(x=850, y=120, width=380, height=350)

                        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
                        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

                        Suppliertable = ttk.Treeview(emp_frame, columns=("invoice", "name", "contact", "desc"),
                                                     yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
                        scrollx.pack(side=BOTTOM, fill=X)
                        scrolly.pack(side=RIGHT, fill=Y)
                        scrollx.config(command=Suppliertable.xview)
                        scrolly.config(command=Suppliertable.yview)

                        Suppliertable.heading("invoice", text="Invoice No")
                        Suppliertable.heading("name", text="Name")
                        Suppliertable.heading("contact", text="Contact")
                        Suppliertable.heading("desc", text="Description")

                        Suppliertable["show"] = "headings"

                        Suppliertable.column("invoice", width=90)
                        Suppliertable.column("name", width=200)
                        Suppliertable.column("contact", width=200)
                        Suppliertable.column("desc", width=100)

                        Suppliertable.pack(fill=BOTH, expand=1)
                        Suppliertable.bind("<ButtonRelease-1>", get_date)

                        show()

                    # ==========================================================================================
                    def category():
                        frms = Toplevel()
                        frms.geometry("1280x500+220+130")
                        frms.title("Management System *** Developed M.SH ")
                        frms.config(bg="white")
                        frms.focus_force()
                        frms.resizable(False, False)
                        # =========================
                        con = sqlite3.connect(database=r'ims.db')
                        cur = con.cursor()
                        cur.execute(
                            "CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text)")
                        con.commit()
                        # =========================
                        # ---------variable-------------
                        var_cat_id = StringVar()
                        var_name = StringVar()

                        # ----------title--------------
                        title = Label(frms, text="Manage Product Category", bg="#184a45", font=("goudy old style", 30),
                                      fg="white", bd=3, relief=RIDGE)
                        title.pack(side=TOP, fill=X, padx=10, pady=20)

                        # ====================================================================================================
                        def add():
                            con = sqlite3.connect(database=r'ims.db')
                            cur = con.cursor()
                            try:
                                if var_name.get() == "":
                                    messagebox.showerror("Error", "Category Name Should must be required", parent=frms)
                                else:
                                    cur.execute("Select * from category where name=?", (var_name.get(),))
                                    row = cur.fetchone()
                                    if row != None:
                                        messagebox.showerror("Error", "Category already present,try different",
                                                             parent=frms)
                                    else:
                                        cur.execute("Insert into category (name) values(?)", (
                                            var_name.get(),
                                        ))
                                        con.commit()
                                        messagebox.showinfo("Success", "Category Addedd Successfully", parent=frms)
                                        show()

                            except Exception as ex:
                                messagebox.showerror("Error", f"Error due to : {str(ex)}")

                        def show():
                            con = sqlite3.connect(database=r'ims.db')
                            cur = con.cursor()
                            try:
                                cur.execute("select * from category")
                                rows = cur.fetchall()
                                categorytable.delete(*categorytable.get_children())
                                for row in rows:
                                    categorytable.insert("", END, values=row)
                            except Exception as ex:
                                messagebox.showerror("Error", f"Error due to : {str(ex)}")

                        def get_date(ev):
                            f = categorytable.focus()
                            content = (categorytable.item(f))
                            row = content['values']
                            var_cat_id.set(row[1])
                            var_name.set(row[1])

                        def delete():
                            con = sqlite3.connect(database=r'ims.db')
                            cur = con.cursor()
                            try:
                                if var_name.get() == "":
                                    messagebox.showerror("Error", "please select or category from the list",
                                                         parent=frms)
                                else:
                                    cur.execute("Select * from category where name=?", (var_name.get(),))
                                    row = cur.fetchone()
                                    if row == None:
                                        messagebox.showerror("Error", "Error, please try again", parent=frms)
                                    else:
                                        op = messagebox.askyesno("Confirm", "Do you really want to delete?",
                                                                 parent=frms)
                                        if op == True:
                                            cur.execute("delete from category where name=?", (var_name.get(),))
                                            con.commit()
                                            messagebox.showinfo("Delete", "category Deleted Successfully", parent=frms)
                                            show()
                                            var_cat_id.set("")
                                            var_name.set("")
                            except Exception as ex:
                                messagebox.showerror("Error", f"Error due to : {str(ex)}")

                        lbl_name = Label(frms, text="Enter Category Name", bg="white", font=("goudy old style", 30))
                        lbl_name.place(x=50, y=100)
                        txt_name = Entry(frms, textvariable=var_name, bg="lightyellow", font=("goudy old style", 18))
                        txt_name.place(x=50, y=170, width=300)

                        btn_add = Button(frms, text="ADD", command=add, bg="#4caf50", fg="white", cursor="hand2",
                                         font=("goudy old style", 18))
                        btn_add.place(x=360, y=170, width=150, height=30)
                        btn_delete = Button(frms, text="Delete", command=delete, bg="red", fg="white", cursor="hand2",
                                            font=("goudy old style", 18))
                        btn_delete.place(x=520, y=170, width=150, height=30)

                        # =========Category Details===

                        cat_frame = Frame(frms, bd=3, relief=RIDGE)
                        cat_frame.place(x=850, y=100, width=380, height=200)

                        scrolly = Scrollbar(cat_frame, orient=VERTICAL)
                        scrollx = Scrollbar(cat_frame, orient=HORIZONTAL)

                        categorytable = ttk.Treeview(cat_frame, columns=("cid", "name"), yscrollcommand=scrolly.set,
                                                     xscrollcommand=scrollx.set)
                        scrollx.pack(side=BOTTOM, fill=X)
                        scrolly.pack(side=RIGHT, fill=Y)
                        scrollx.config(command=categorytable.xview)
                        scrolly.config(command=categorytable.yview)

                        categorytable.heading("cid", text="C ID")
                        categorytable.heading("name", text="Name")

                        categorytable["show"] = "headings"

                        categorytable.column("cid", width=200)
                        categorytable.column("name", width=200)

                        categorytable.pack(fill=BOTH, expand=1)
                        categorytable.bind("<ButtonRelease-1>", get_date)
                        show()

                    def product():
                        fram = Toplevel()
                        fram.geometry("1280x500+220+130")
                        fram.title("Management System *** Developed M.SH ")
                        fram.config(bg="white")
                        fram.focus_force()
                        fram.resizable(False, False)
                        # =========================
                        con = sqlite3.connect(database=r'ims.db')
                        cur = con.cursor()
                        cur.execute(
                            "CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT,Category text,Supplier text,name text,price text,qty text,status text)")
                        con.commit()

                        # =========================
                        def fetch_cat_sup():
                            cat_list.append("Empty")
                            sup_list.append("Empty")
                            con = sqlite3.connect(database=r'ims.db')
                            cur = con.cursor()
                            try:
                                cur.execute("Select name from category ")
                                cat = cur.fetchall()
                                if len(cat) > 0:
                                    del cat_list[:]
                                    cat_list.append("Select")
                                    for i in cat:
                                        cat_list.append(i[0])
                                cur.execute("Select name from supplier ")
                                sup = cur.fetchall()
                                if len(sup) > 0:
                                    del sup_list[:]
                                    sup_list.append("Select")
                                    for i in sup:
                                        sup_list.append(i[0])
                            except Exception as ex:
                                messagebox.showerror("Error", f"Error due to : {str(ex)}")

                        # --------------variables----------------
                        var_searchby = StringVar()
                        var_searchtxt = StringVar()
                        var_pid = StringVar()
                        var_cat = StringVar()
                        var_supplier = StringVar()
                        cat_list = []
                        sup_list = []
                        fetch_cat_sup()
                        var_name = StringVar()
                        var_price = StringVar()
                        var_qty = StringVar()
                        var_status = StringVar()

                        product_frame = Frame(fram, bd=2, relief=RIDGE, bg="white")
                        product_frame.place(x=10, y=10, width=450, height=480)

                        # ----------title--------------
                        title = Label(product_frame, text="Manage Products Details", bg="#0f4d7d",
                                      font=("goudy old style", 18), fg="white", bd=3, relief=RIDGE)
                        title.pack(side=TOP, fill=X)

                        # ==========================================================================
                        def add():
                            con = sqlite3.connect(database=r'ims.db')
                            cur = con.cursor()
                            try:
                                if var_cat.get() == "Select" or var_cat.get() == "Empty" or var_supplier.get() == "Select" or var_supplier.get() == "Empty" or var_name.get() == "":
                                    messagebox.showerror("Error", "All fields are required", parent=fram)
                                else:
                                    cur.execute("Select * from product where name=?", (var_name.get(),))
                                    row = cur.fetchone()
                                    if row != None:
                                        messagebox.showerror("Error", "Product already present, try different",
                                                             parent=fram)
                                    else:
                                        cur.execute(
                                            "Insert into product (Category,Supplier,name,price,qty,status) values(?,?,?,?,?,?)",
                                            (
                                                var_cat.get(),
                                                var_supplier.get(),
                                                var_name.get(),
                                                var_price.get(),
                                                var_qty.get(),
                                                var_status.get(),
                                            ))
                                        con.commit()
                                        messagebox.showinfo("Success", "Product Addedd Successfully", parent=fram)
                                        show()

                            except Exception as ex:
                                messagebox.showerror("Error", f"Error due to : {str(ex)}")

                        def show():
                            con = sqlite3.connect(database=r'ims.db')
                            cur = con.cursor()
                            try:
                                cur.execute("select * from product")
                                rows = cur.fetchall()
                                Producttable.delete(*Producttable.get_children())
                                for row in rows:
                                    Producttable.insert("", END, values=row)
                            except Exception as ex:
                                messagebox.showerror("Error", f"Error due to : {str(ex)}")

                        def get_date(ev):
                            f = Producttable.focus()
                            content = (Producttable.item(f))
                            row = content['values']
                            var_pid.set(row[0])
                            var_cat.set(row[1])
                            var_supplier.set(row[2])
                            var_name.set(row[3])
                            var_price.set(row[4])
                            var_qty.set(row[5])
                            var_status.set(row[6])

                        def update():
                            con = sqlite3.connect(database=r'ims.db')
                            cur = con.cursor()
                            try:
                                if var_pid.get() == "":
                                    messagebox.showerror("Error", "Please select product from list", parent=fram)
                                else:
                                    cur.execute("Select * from product where pid=?", (var_pid.get(),))
                                    row = cur.fetchone()
                                    if row == None:
                                        messagebox.showerror("Error", "Invalid Product", parent=fram)
                                    else:
                                        cur.execute(
                                            "Update product set Category=?,Supplier=?,name=?,price=?,qty=?,status=? where pid=?",
                                            (
                                                var_cat.get(),
                                                var_supplier.get(),
                                                var_name.get(),
                                                var_price.get(),
                                                var_qty.get(),
                                                var_status.get(),
                                                var_pid.get(),
                                            ))
                                        con.commit()
                                        messagebox.showinfo("Success", "Product Updated Successfully", parent=fram)
                                        show()
                            except Exception as ex:
                                messagebox.showerror("Error", f"Error due to : {str(ex)}")

                        def delete():
                            con = sqlite3.connect(database=r'ims.db')
                            cur = con.cursor()
                            try:
                                if var_pid.get() == "":
                                    messagebox.showerror("Error", "Select Product from the list", parent=fram)
                                else:
                                    cur.execute("Select * from product where pid=?", (var_pid.get(),))
                                    row = cur.fetchone()
                                    if row == None:
                                        messagebox.showerror("Error", "Invalid Product", parent=fram)
                                    else:
                                        op = messagebox.askyesno("Confirm", "Do you really want to delete?",
                                                                 parent=fram)
                                        if op == True:
                                            cur.execute("delete from product where pid=?", (var_pid.get(),))
                                            con.commit()
                                            messagebox.showinfo("Delete", "Product Deleted Successfully", parent=fram)
                                            clear()
                            except Exception as ex:
                                messagebox.showerror("Error", f"Error due to : {str(ex)}")

                        def clear():
                            var_cat.set("Select")
                            var_supplier.set("Select")
                            var_name.set("")
                            var_price.set("")
                            var_qty.set("")
                            var_status.set("Active")
                            show()

                        def search():
                            con = sqlite3.connect(database=r'ims.db')
                            cur = con.cursor()
                            try:
                                if var_searchby.get() == "Select":
                                    messagebox.showerror("Error", "Select Search By option", parent=fram)
                                elif var_searchtxt.get() == "":
                                    messagebox.showerror("Error", "Search input should be required", parent=fram)
                                else:
                                    cur.execute(
                                        "select * from product where " + str(var_searchby.get() + " LIKE '%") + str(
                                            var_searchtxt.get()) + "%'")
                                    rows = cur.fetchall()
                                    if len(rows) != 0:
                                        Producttable.delete(*Producttable.get_children())
                                        for row in rows:
                                            Producttable.insert("", END, values=row)
                                    else:
                                        messagebox.showerror("Error", "No record found!", parent=fram)
                            except Exception as ex:
                                messagebox.showerror("Error", f"Error due to : {str(ex)}")

                        # ===column1===
                        lbl_category = Label(product_frame, text="Category", bg="white", font=("goudy old style", 18))
                        lbl_category.place(x=30, y=60)
                        lbl_supplier = Label(product_frame, text="Supplier", bg="white", font=("goudy old style", 18))
                        lbl_supplier.place(x=30, y=110)
                        lbl_product = Label(product_frame, text="Name", bg="white", font=("goudy old style", 18))
                        lbl_product.place(x=30, y=160)
                        lbl_price = Label(product_frame, text="Price", bg="white", font=("goudy old style", 18))
                        lbl_price.place(x=30, y=210)
                        lbl_quantity = Label(product_frame, text="Quantity", bg="white", font=("goudy old style", 18))
                        lbl_quantity.place(x=30, y=260)
                        lbl_status = Label(product_frame, text="Status", bg="white", font=("goudy old style", 18))
                        lbl_status.place(x=30, y=310)

                        # ===column2===
                        cmb_category = ttk.Combobox(product_frame, textvariable=var_cat,
                                                    values=cat_list, state="readonly", justify=CENTER,
                                                    font=("goudy old style", 15))
                        cmb_category.place(x=150, y=60, width=200)
                        cmb_category.current(0)

                        cmb_sup = ttk.Combobox(product_frame, textvariable=var_supplier, values=sup_list,
                                               state="readonly", justify=CENTER,
                                               font=("goudy old style", 15))
                        cmb_sup.place(x=150, y=110, width=200)
                        cmb_sup.current(0)

                        txt_name = Entry(product_frame, textvariable=var_name, font=("goudy old style", 15),
                                         bg="lightyellow")
                        txt_name.place(x=150, y=160, width=200)
                        txt_price = Entry(product_frame, textvariable=var_price, font=("goudy old style", 15),
                                          bg="lightyellow")
                        txt_price.place(x=150, y=210, width=200)
                        txt_qty = Entry(product_frame, textvariable=var_qty, font=("goudy old style", 15),
                                        bg="lightyellow")
                        txt_qty.place(x=150, y=260, width=200)

                        cmb_status = ttk.Combobox(product_frame, textvariable=var_status, values=("Active", "Inactive"),
                                                  state="readonly", justify=CENTER,
                                                  font=("goudy old style", 15))
                        cmb_status.place(x=150, y=310, width=200)
                        cmb_status.current(0)

                        # ======Buttons=========
                        btn_add = Button(product_frame, text="Save", command=add, font=("goudy old style", 15),
                                         bg="#2196f3", fg="white", cursor="hand2")
                        btn_add.place(x=10, y=400, width=100, height=40)
                        btn_update = Button(product_frame, text="Update", command=update, font=("goudy old style", 15),
                                            bg="#4caf50", fg="white", cursor="hand2")
                        btn_update.place(x=120, y=400, width=100, height=40)
                        btn_delete = Button(product_frame, text="Delete", command=delete, font=("goudy old style", 15),
                                            bg="#f44336", fg="white", cursor="hand2")
                        btn_delete.place(x=230, y=400, width=100, height=40)
                        btn_clear = Button(product_frame, text="Clear", command=clear, font=("goudy old style", 15),
                                           bg="#607d8b", fg="white", cursor="hand2")
                        btn_clear.place(x=340, y=400, width=100, height=40)
                        # =====searchframe=========
                        searchframe = LabelFrame(fram, text="Search Employee", font=("goudy old style", 12, "bold"),
                                                 bd=2, relief=RIDGE, bg="white")
                        searchframe.place(x=580, y=10, width=600, height=80)
                        # ===options===
                        cmb_search = ttk.Combobox(searchframe, textvariable=var_searchby,
                                                  values=("Select", "Category", "Supplier", "Name"), state="readonly",
                                                  justify=CENTER,
                                                  font=("goudy old style", 15))
                        cmb_search.place(x=10, y=10, width=180)
                        cmb_search.current(0)
                        txt_search = Entry(searchframe, textvariable=var_searchtxt, font=("goudy old style", 15),
                                           bg="lightyellow")
                        txt_search.place(x=200, y=10)
                        btn_search = Button(searchframe, text="Search", command=search, font=("goudy old style", 15),
                                            bg="#4caf50",
                                            fg="white", cursor="hand2")
                        btn_search.place(x=410, y=9, width=150, height=30)

                        # =========Product Details===

                        p_frame = Frame(fram, bd=3, relief=RIDGE)
                        p_frame.place(x=480, y=100, width=780, height=390)

                        scrolly = Scrollbar(p_frame, orient=VERTICAL)
                        scrollx = Scrollbar(p_frame, orient=HORIZONTAL)

                        Producttable = ttk.Treeview(p_frame, columns=(
                        "pid", "Category", "Supplier", "name", "price", "qty", "status"),
                                                    yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
                        scrollx.pack(side=BOTTOM, fill=X)
                        scrolly.pack(side=RIGHT, fill=Y)
                        scrollx.config(command=Producttable.xview)
                        scrolly.config(command=Producttable.yview)

                        Producttable.heading("pid", text="P ID")
                        Producttable.heading("Category", text="Category")
                        Producttable.heading("Supplier", text="Supplier")
                        Producttable.heading("name", text="Name")
                        Producttable.heading("price", text="Price")
                        Producttable.heading("qty", text="Qty")
                        Producttable.heading("status", text="Status")

                        Producttable["show"] = "headings"

                        Producttable.column("pid", width=90)
                        Producttable.column("Category", width=200)
                        Producttable.column("Supplier", width=200)
                        Producttable.column("name", width=200)
                        Producttable.column("price", width=100)
                        Producttable.column("qty", width=140)
                        Producttable.column("status", width=100)

                        Producttable.pack(fill=BOTH, expand=1)
                        Producttable.bind("<ButtonRelease-1>", get_date)

                        show()

                    def sales():
                        frams = Toplevel()
                        frams.geometry("1280x500+220+130")
                        frams.title("Management System *** Developed M.SH ")
                        frams.config(bg="white")
                        frams.focus_force()
                        frams.resizable(False, False)

                        # =========================
                        def show():
                            del bill_list[:]
                            sales_list.delete(0, END)
                            for i in os.listdir('bill'):
                                if i.split('.')[-1] == 'txt':
                                    sales_list.insert(END, i)
                                    bill_list.append(i.split('.')[0])

                        def get_data(ev):
                            index_ = sales_list.curselection()
                            file_name = sales_list.get(index_)
                            bill_area.delete('1.0', END)
                            fp = open(f'bill/{file_name}', 'r',encoding="utf-8")
                            for i in fp:
                                bill_area.insert(END, i)
                            fp.close()

                        def search():
                            if var_invoice.get() == "":
                                messagebox.showerror("Error", "Invoice no.Should be required", parent=frams)
                            else:
                                if var_invoice.get() in bill_list:
                                    fp = open(f'bill/{var_invoice.get()}.txt', 'r')
                                    bill_area.delete('1.0', END)
                                    for i in fp:
                                        bill_area.insert(END, i)
                                    fp.close()
                                else:
                                    messagebox.showerror("Error", "Invalid Invoice No.", parent=frams)

                        def clear():
                            show()
                            bill_area.delete('1.0', END)

                        # ---------variables-----------
                        bill_list = []
                        var_invoice = StringVar()

                        # ----------title--------------
                        title = Label(frams, text="View Customer BILLs", bg="#184a45", font=("goudy old style", 30),
                                      fg="white", bd=3, relief=RIDGE)
                        title.pack(side=TOP, fill=X, padx=10, pady=20)

                        lbl_invoice = Label(frams, text="Invoice No:", bg="white", font=("times new roman", 15))
                        lbl_invoice.place(x=50, y=100)
                        txt_invoice = Entry(frams, textvariable=var_invoice, bg="lightyellow",
                                            font=("times new roman", 15))
                        txt_invoice.place(x=160, y=100, width=180, height=28)

                        btn_search = Button(frams, text="Search", command=search, font=("times new roman", 15, "bold"),
                                            bg="#2196f3", fg="white", cursor="hand2")
                        btn_search.place(x=360, y=100, width=120, height=28)
                        btn_clear = Button(frams, text="Clear", command=clear, font=("times new roman", 15, "bold"),
                                           bg="lightgray", cursor="hand2")
                        btn_clear.place(x=490, y=100, width=120, height=28)

                        # ====Bill List=====
                        sales_frame = Frame(frams, bd=3, relief=RIDGE)
                        sales_frame.place(x=50, y=140, width=200, height=330)

                        scrolly = Scrollbar(sales_frame, orient=VERTICAL)
                        sales_list = Listbox(sales_frame, font=("goudy old style", 15), bg="white",
                                             yscrollcommand=scrolly.set)
                        scrolly.pack(side=RIGHT, fill=Y)
                        scrolly.config(command=sales_list.yview)
                        sales_list.pack(fill=BOTH, expand=1)
                        sales_list.bind("<ButtonRelease-1>", get_data)

                        # ====Bill Area=====
                        bill_frame = Frame(frams, bd=3, relief=RIDGE)
                        bill_frame.place(x=280, y=140, width=500, height=330)

                        title2 = Label(bill_frame, text="Customer BILL Area", bg="orange", font=("goudy old style", 20))
                        title2.pack(side=TOP, fill=X)

                        scrolly2 = Scrollbar(bill_frame, orient=VERTICAL)
                        bill_area = Text(bill_frame, bg="lightyellow", yscrollcommand=scrolly2.set)
                        scrolly2.pack(side=RIGHT, fill=Y)
                        scrolly2.config(command=bill_area.yview)
                        bill_area.pack(fill=BOTH, expand=1)

                        show()

                    def update_content():
                        con = sqlite3.connect(database=r'ims.db')
                        cur = con.cursor()
                        try:
                            cur.execute("select * from product")
                            product = cur.fetchall()
                            lbl_product.config(text=f"Total Product\n[{str(len(product))}]")

                            cur.execute("select * from supplier")
                            supplier = cur.fetchall()
                            lbl_supplier.config(text=f"Total Supplier\n[{str(len(supplier))}]")

                            cur.execute("select * from category")
                            category = cur.fetchall()
                            lbl_category.config(text=f"Total Category\n[{str(len(category))}]")

                            cur.execute("select * from employee")
                            employee = cur.fetchall()
                            lbl_employee.config(text=f"Total Employee\n[{str(len(employee))}]")

                            bill = len(os.listdir('bill'))
                            lbl_sales.config(text=f"Total Sales\n[{str(bill)}]")

                            time_ = time.strftime("%I:%M:%S")
                            date_ = time.strftime("%d/%m/%y")
                            lbl_clock.config(
                                text=f"***Welcome to Management System***\t\t Data: {str(date_)} \t\t Time: {str(time_)}")
                            lbl_clock.after(200, update_content)

                        except Exception as ex:
                            messagebox.showerror("Error", f"Error due to :{str(ex)}", parent=root)

                    def winexit():
                        mess = messagebox.askyesno("Attention", "Do You Want To Exit The Program?")
                        if mess > 0:
                            root.destroy()

                    def prog():
                        messagebox.showinfo("Programming",
                                            f"Programmer : Mahmoud Shaban Allam\nPhone No. 01555790001\n\t  01550530009",
                                            parent=root)

                        # ----- left menu------

                    LeftMenu = Frame(root, bd=2, relief=RIDGE, bg="white")
                    LeftMenu.place(x=0, y=102, width=200, height=580)

                    lbl_menu = Label(LeftMenu, text="Menu", font=("times new roman", 20), bg="#009688").pack(side=TOP,fill=X)
                    bt_employee = Button(LeftMenu, text="Employee", command=employee,font=("times new roman", 20, "bold"), bd=3, cursor="hand2").pack(side=TOP,fill=X)
                    bt_supplier = Button(LeftMenu, text="Supplier", command=supplier,font=("times new roman", 20, "bold"), bd=3, cursor="hand2").pack(side=TOP, fill=X)
                    bt_category = Button(LeftMenu, text="Category", command=category,font=("times new roman", 20, "bold"), bd=3, cursor="hand2").pack(side=TOP,fill=X)
                    bt_product = Button(LeftMenu, text="Product", command=product, font=("times new roman", 20, "bold"),bd=3, cursor="hand2").pack(side=TOP, fill=X)
                    bt_sales = Button(LeftMenu, text="Sales", command=sales, font=("times new roman", 20, "bold"), bd=3,cursor="hand2").pack(side=TOP, fill=X)
                    bt_prog = Button(LeftMenu, text="Programming", command=prog, font=("times new roman", 20, "bold"), bd=3, cursor="hand2").pack(side=TOP, fill=X)
                    bt_exit = Button(LeftMenu, text="Exit", command=winexit, font=("times new roman", 20, "bold"), bd=3,cursor="hand2").pack(side=TOP, fill=X)

                    # ---------contect------------
                    lbl_employee = Label(root, text="Total Employee\n[0]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white",font=("goudy old style", 20, "bold"))
                    lbl_employee.place(x=300, y=120, height=150, width=300)

                    lbl_supplier = Label(root, text="Total Supplier\n[0]", bd=5, relief=RIDGE, bg="#ff5722", fg="white",font=("goudy old style", 20, "bold"))
                    lbl_supplier.place(x=650, y=120, height=150, width=300)

                    lbl_category = Label(root, text="Total Category\n[0]", bd=5, relief=RIDGE, bg="#009688", fg="white",font=("goudy old style", 20, "bold"))
                    lbl_category.place(x=1000, y=120, height=150, width=300)

                    lbl_product = Label(root, text="Total Product\n[0]", bd=5, relief=RIDGE, bg="#607d8b", fg="white",font=("goudy old style", 20, "bold"))
                    lbl_product.place(x=300, y=300, height=150, width=300)

                    lbl_sales = Label(root, text="Total Sales\n[0]", bd=5, relief=RIDGE, bg="#ffc107", fg="white",font=("goudy old style", 20, "bold"))
                    lbl_sales.place(x=650, y=300, height=150, width=300)

                    # -------footer---------------
                    lbl_footer = Label(root, text="**M.SH Management System***", font=("times new roman", 12),
                                       bg="#4d636d", fg="white")
                    lbl_footer.pack(side=BOTTOM, fill=X)

                     #update_content()
                    update_content()

                    root.mainloop()



                else:
                    roots.destroy()
                    #os.system("python billing.py")
                    #==============================================================
                    rot = Tk()
                    rot.geometry("1500x800+0+0")
                    rot.title("Management System *** Developed M.SH ")
                    rot.config(bg="white")
                    cart_list = []


                    # ----------title----------
                    title = Label(rot, text="***** Management System *****", font=("times new roman", 40, "bold"),bg="#010c48", fg="white", anchor="w", padx=20)
                    title.place(x=0, y=0, relwidth=1, height=70)
                    #====================================================================
                    # =========================== Function===========================
                    def ge_input(num):
                        xnum = var_cal_input.get() + str(num)
                        var_cal_input.set(xnum)

                    def clear_cal():
                        var_cal_input.set('')

                    def perform_cal():
                        result = var_cal_input.get()
                        var_cal_input.set(eval(result))

                    def show():
                        con = sqlite3.connect(database=r'ims.db')
                        cur = con.cursor()
                        try:
                            cur.execute("select pid,name,price,qty,status from product where status ='Active'")
                            rows = cur.fetchall()
                            Producttable.delete(*Producttable.get_children())
                            for row in rows:
                                Producttable.insert("", END, values=row)
                        except Exception as ex:
                            messagebox.showerror("Error", f"Error due to : {str(ex)}")

                    def search():
                        con = sqlite3.connect(database=r'ims.db')
                        cur = con.cursor()
                        try:
                            if var_search.get() == "":
                                messagebox.showerror("Error", "Search input should be required", parent=rot)
                            else:
                                cur.execute("select pid,name,price,qty,status from product where name LIKE '%" + str(
                                    var_search.get()) + "%'")
                                rows = cur.fetchall()
                                if len(rows) != 0:
                                    Producttable.delete(*Producttable.get_children())
                                    for row in rows:
                                        Producttable.insert("", END, values=row)
                                else:
                                    messagebox.showerror("Error", "No record found!", parent=rot)
                        except Exception as ex:
                            messagebox.showerror("Error", f"Error due to : {str(ex)}")

                    def get_date(ev):
                        f = Producttable.focus()
                        content = (Producttable.item(f))
                        row = content['values']
                        var_pid.set(row[0])
                        var_pname.set(row[1])
                        var_price.set(row[2])
                        lbl_instock.config(text=f"In Stock [{str(row[3])}]")
                        var_stock.set(row[3])
                        var_qty.set('1')

                    def get_date_cart(ev):
                        f = Carttable.focus()
                        content = (Carttable.item(f))
                        row = content['values']
                        var_pid.set(row[0])
                        var_pname.set(row[1])
                        var_price.set(row[2])
                        var_qty.set(row[3])
                        lbl_instock.config(text=f"In Stock [{str(row[4])}]")
                        var_stock.set(row[4])

                    def add_update_cart():
                        if var_pid.get() == "":
                            messagebox.showerror("Error", "Please Select Product from the list", parent=rot)
                        elif var_qty.get() == "":
                            messagebox.showerror("Error", "Quantity is Required", parent=rot)
                        elif int(var_qty.get()) > int(var_stock.get()):
                            messagebox.showerror("Error", "Invaild Quantity", parent=rot)
                        else:
                            # price_cal=int(int(self.var_qty.get())*float(self.var_price.get()))
                            # price_cal=float(price_cal)
                            price_cal = var_price.get()
                            cart_data = [var_pid.get(), var_pname.get(), price_cal, var_qty.get(),var_stock.get()]
                            # ================update cart===========
                            present = "no"
                            index_ = -1
                            for row in cart_list:
                                if var_pid.get() == row[0]:
                                    present = "yes"
                                    break
                                index_ += 1
                            if present == 'yes':
                                op = messagebox.askyesno("Confirm","Product already present\nDO you want to Update|Remove from the Cart",parent=rot)
                                if op == True:
                                    if var_qty.get() == "0":
                                        cart_list.pop(index_)
                                    else:
                                        # self.cart_list[index_][2]=price_cal
                                        cart_list[index_][3] = var_qty.get()
                            else:
                                cart_list.append(cart_data)
                            show_cart()
                            bill_updates()

                    def bill_updates():
                        bill_amny = 0
                        net_pay = 0
                        discount = 0
                        for row in cart_list:
                            bill_amny = bill_amny + float(row[2]) * int(row[3])

                        discount = (bill_amny * 5) / 100
                        net_pay = bill_amny - discount
                        lbl_amnt.config(text=f"Bill Amount\n{str(bill_amny)}")
                        lbl_net_pay.config(text=f"Net Pay\n{str(net_pay)}")
                        carttitle.config(text=f"Cart\t Total Producr: [{str(len(cart_list))}]")

                    def show_cart():
                        try:
                            Carttable.delete(*Carttable.get_children())
                            for row in cart_list:
                                Carttable.insert("", END, values=row)
                        except Exception as ex:
                            messagebox.showerror("Error", f"Error due to : {str(ex)}")

                    def bill_top():
                        etime = time.strftime("%H:%M:%S")
                        edate = time.strftime("%d/%m/%Y")
                        invoice = int(time.strftime("%H%M%S")) + int(time.strftime("%d%m%y"))
                        bill_top_temp = f"""
\t\tWelcome to the program
\t Phone No. ***********  ,Delhi-125001
{str("=" * 59)}
Customer Name: {var_cname.get()}
Ph No. :{var_contact.get()}
Bill No. {str(invoice)}
Date: {edate}\t\t\t Time: {etime}
{str("=" * 59)}
Product Name\t\t\tQty\t\tPrice
{str("=" * 59)}
            """
                        txt_bill_area.delete('1.0', END)
                        txt_bill_area.insert('1.0', bill_top_temp)

                    def bill_bottom():
                        bill_amny = 0
                        net_pay = 0
                        discount = 0
                        for row in cart_list:
                            bill_amny = bill_amny + float(row[2]) * int(row[3])

                        discount = (bill_amny * 5) / 100
                        net_pay = bill_amny - discount
                        bill_bottom_temp = f""" 
{str("=" * 59)}
Bill Amount\t\t\t\t\t{bill_amny}
Discount\t\t\t\t\t{discount}
Net Pay\t\t\t\t\t{net_pay}
{str("=" * 59)}\n
\t\tThank you for visiting us.
{str("=" * 59)}\n
            """

                        txt_bill_area.insert(END, bill_bottom_temp)

                    def bill_middle():
                        con = sqlite3.connect(database=r'ims.db')
                        cur = con.cursor()
                        try:
                            for row in cart_list:
                                pid = row[0]
                                name = row[1]
                                qty = int(row[4]) - int(row[3])
                                if int(row[3]) == int(row[4]):
                                    status = 'Inactive'
                                if int(row[3]) != int(row[4]):
                                    status = 'Active'

                                price = float(row[2]) * int(row[3])
                                price = str(price)
                                txt_bill_area.insert(END, "\n" + name + "\t\t\t" + row[3] + "\t\t" + price)
                                #   update qty in product table
                                cur.execute("Update product set qty=?,status=? where pid=?", (
                                    qty,
                                    status,
                                    pid

                                ))
                                con.commit()
                            con.close()
                            show()

                        except Exception as ex:
                            messagebox.showerror("Error", f"Error due to :{str(ex)}", parent=rot)



                    def generate_bill():
                        invoice = int(time.strftime("%H%M%S")) + int(time.strftime("%d%m%y"))
                        if var_cname.get() == '' or var_contact.get() == '':
                            messagebox.showerror("Error", f"Customer Details are required", parent=rot)
                        elif len(cart_list) == 0:
                            messagebox.showerror("Error", f"Please Add Product to the Cart!!", parent=rot)
                        else:
                            # ======bill top========
                            bill_top()
                            # ======bill middle========
                            bill_middle()
                            # ======bill bottom========
                            bill_bottom()

                            fb = open(f'bill/{str(invoice)}.txt', 'w',encoding="utf-8")
                            fb.write(txt_bill_area.get('1.0', END))
                            fb.close()
                            messagebox.showinfo("Saved", "Bill has been generated/Save in Backend", parent=rot)
                            chk_print = 1



                    def clear_cart():
                        var_pid.set('')
                        var_pname.set('')
                        var_price.set('')
                        var_qty.set('')
                        lbl_instock.config(text=f"In Stock")
                        var_stock.set('')

                    def clear_all():
                        del cart_list[:]
                        var_cname.set('')
                        var_contact.set('')
                        txt_bill_area.delete('1.0', END)
                        carttitle.config(text=f"Cart\t Total Producr: [0]")
                        var_search.set('')
                        clear_cart()
                        show()
                        show_cart()

                    def update_date_time():
                        time_ = time.strftime("%I:%M:%S")
                        date_ = time.strftime("%d/%m/%y")
                        lbl_clock.config(
                            text=f"***Welcome to Management System***\t\t Data: {str(date_)} \t\t Time: {str(time_)}")
                        lbl_clock.after(200, update_date_time)

                    def print_bill():

                        mess = messagebox.askyesno("Print", "Do you want Printing")
                        if mess > 0:
                            d = txt_bill_area.get("1.0", END)
                            file = tempfile.mktemp(".txt")
                            open(file, "w",encoding="utf-8").write(d)
                            os.startfile(file, "print")

                        """chk_print = 0
                        if chk_print == 1:
                            messagebox.showinfo("Print", "Please wait while Printing", parent=rot)
                            new_file = tempfile.mktemp('.txt')
                            open(new_file, 'w').write(txt_bill_area.get('1.0', END))
                            os.startfile(new_file, 'print')
                        else:
                            messagebox.showerror("Print", "Please generate bill to print the receipt", parent=rot)"""

                    def logout():
                        rot.destroy()
                        os.system("python electronics.py")

                    # --------btn_logout----------
                    btn_logout = Button(rot, text="Logout", command=logout,
                                        font=("times new roman", 15, "bold"), bg="yellow", cursor="hand2")
                    btn_logout.place(x=1250, y=10, height=50, width=150)
                    # -------clock---------------
                    lbl_clock = Label(rot,text="**Welcome to Management System***\t\t Data: DD/MM/YYYY\t\t Time: HH:MM:SS",font=("times new roman", 15), bg="#4d636d", fg="white")
                    lbl_clock.place(x=0, y=70, relwidth=1, height=30)

                    # -----------product_frame--------------

                    var_search = StringVar()

                    productframe1 = Frame(rot, bd=4, relief=RIDGE, bg="white")
                    productframe1.place(x=6, y=110, width=410, height=660)

                    ptitle = Label(productframe1, text="All Products", font=("goudy old style", 20, "bold"),bg="#262626", fg="white")
                    ptitle.pack(side=TOP, fill=X)

                    productframe2 = Frame(productframe1, bd=2, relief=RIDGE, bg="white")
                    productframe2.place(x=2, y=42, width=398, height=90)

                    lbl_search = Label(productframe2, text="Search Product | By Name",font=("times new roman", 15, "bold"), bg="white", fg="green")
                    lbl_search.place(x=2, y=5)
                    lbl_name = Label(productframe2, text="Product Name", font=("times new roman", 15, "bold"),bg="white")
                    lbl_name.place(x=2, y=45)
                    txt_search = Entry(productframe2, textvariable=var_search, font=("times new roman", 15),bg="lightyellow")
                    txt_search.place(x=128, y=47, width=150, height=22)
                    btn_search = Button(productframe2, text="Search", command=search, font=("goudy old style", 15), bg="#2196f3", fg="white", cursor="hand2")
                    btn_search.place(x=285, y=45, width=100, height=25)
                    btn_show_all = Button(productframe2, text="Show All", command=show,font=("goudy old style", 15), bg="#083531", fg="white", cursor="hand2")
                    btn_show_all.place(x=285, y=10, width=100, height=25)

                    # =========billing Details===

                    productframe3 = Frame(productframe1, bd=3, relief=RIDGE)
                    productframe3.place(x=2, y=140, width=398, height=480)

                    scrolly = Scrollbar(productframe3, orient=VERTICAL)
                    scrollx = Scrollbar(productframe3, orient=HORIZONTAL)

                    Producttable = ttk.Treeview(productframe3, columns=("pid", "name", "price", "qty", "status"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
                    scrollx.pack(side=BOTTOM, fill=X)
                    scrolly.pack(side=RIGHT, fill=Y)
                    scrollx.config(command=Producttable.xview)
                    scrolly.config(command=Producttable.yview)

                    Producttable.heading("pid", text="P ID")
                    Producttable.heading("name", text="Name")
                    Producttable.heading("price", text="Price")
                    Producttable.heading("qty", text="QTY")
                    Producttable.heading("status", text="Status")

                    Producttable["show"] = "headings"

                    Producttable.column("pid", width=40)
                    Producttable.column("name", width=100)
                    Producttable.column("price", width=100)
                    Producttable.column("qty", width=40)
                    Producttable.column("status", width=90)
                    Producttable.pack(fill=BOTH, expand=1)
                    Producttable.bind("<ButtonRelease-1>", get_date)

                    lbl_note = Label(productframe1, text="Note:Enter 0 Quantity to remove product from the Cart",font=("gould old style", 12), anchor="w", bg="white", fg="red")
                    lbl_note.pack(side=BOTTOM, fill=X)

                    # ---------customerframe------
                    var_cname = StringVar()
                    var_contact = StringVar()

                    customerframe = Frame(rot, bd=4, relief=RIDGE, bg="white")
                    customerframe.place(x=420, y=110, width=600, height=70)

                    ctitle = Label(customerframe, text="Customer Details", font=("goudy old style", 15), bg="lightgray")
                    ctitle.pack(side=TOP, fill=X)
                    lbl_name = Label(customerframe, text="Name", font=("times new roman", 15), bg="white", fg="green")
                    lbl_name.place(x=5, y=35)
                    txt_name = Entry(customerframe, textvariable=var_cname, font=("times new roman", 15), bg="lightyellow")
                    txt_name.place(x=80, y=35, width=180)
                    lbl_contact = Label(customerframe, text="Contact No.", font=("times new roman", 15), bg="white",fg="green")
                    lbl_contact.place(x=300, y=35)
                    txt_contact = Entry(customerframe, textvariable=var_contact, font=("times new roman", 15),bg="lightyellow")
                    txt_contact.place(x=410, y=35, width=140)

                    # -----------cal cart frame--------------
                    cal_cart_frame = Frame(rot, bd=2, relief=RIDGE, bg="white")
                    cal_cart_frame.place(x=420, y=190, width=600, height=580)
                    # -----------calculator frame--------------
                    var_cal_input = StringVar()

                    cal_frame = Frame(cal_cart_frame, bd=9, relief=RIDGE, bg="white")
                    cal_frame.place(x=5, y=10, width=268, height=440)

                    txt_cal_input = Entry(cal_frame, textvariable=var_cal_input, font=("arial", 15, "bold"), width=21, bd=10, relief=GROOVE, state="readonly", justify=RIGHT)
                    txt_cal_input.grid(row=0, columnspan=4)

                    btn_7 = Button(cal_frame, text='7', font=("arail", 15, "bold"), command=lambda: ge_input(7), bd=5, width=4, pady=23, cursor="hand2")
                    btn_7.grid(row=1, column=0)
                    btn_8 = Button(cal_frame, text='8', font=("arail", 15, "bold"), command=lambda: ge_input(8),bd=5, width=4, pady=23, cursor="hand2")
                    btn_8.grid(row=1, column=1)
                    btn_9 = Button(cal_frame, text='9', font=("arail", 15, "bold"), command=lambda: ge_input(9), bd=5, width=4, pady=23, cursor="hand2")
                    btn_9.grid(row=1, column=2)
                    btn_sum = Button(cal_frame, text='+', font=("arail", 15, "bold"),command=lambda: ge_input('+'), bd=5, width=4, pady=23, cursor="hand2")
                    btn_sum.grid(row=1, column=3)

                    btn_4 = Button(cal_frame, text='4', font=("arail", 15, "bold"), command=lambda: ge_input(4), bd=5, width=4, pady=23, cursor="hand2")
                    btn_4.grid(row=2, column=0)
                    btn_5 = Button(cal_frame, text='5', font=("arail", 15, "bold"), command=lambda: ge_input(5), bd=5, width=4, pady=23, cursor="hand2")
                    btn_5.grid(row=2, column=1)
                    btn_6 = Button(cal_frame, text='6', font=("arail", 15, "bold"), command=lambda: ge_input(6), bd=5, width=4, pady=23, cursor="hand2")
                    btn_6.grid(row=2, column=2)
                    btn_sub = Button(cal_frame, text='-', font=("arail", 15, "bold"),command=lambda: ge_input('-'), bd=5, width=4, pady=23, cursor="hand2")
                    btn_sub.grid(row=2, column=3)

                    btn_1 = Button(cal_frame, text='1', font=("arail", 15, "bold"), command=lambda: ge_input(1), bd=5, width=4, pady=23, cursor="hand2")
                    btn_1.grid(row=3, column=0)
                    btn_2 = Button(cal_frame, text='2', font=("arail", 15, "bold"), command=lambda: ge_input(2), bd=5, width=4, pady=23, cursor="hand2")
                    btn_2.grid(row=3, column=1)
                    btn_3 = Button(cal_frame, text='3', font=("arail", 15, "bold"), command=lambda: ge_input(3), bd=5, width=4, pady=23, cursor="hand2")
                    btn_3.grid(row=3, column=2)
                    btn_mul = Button(cal_frame, text='*', font=("arail", 15, "bold"),command=lambda: ge_input('*'), bd=5, width=4, pady=23, cursor="hand2")
                    btn_mul.grid(row=3, column=3)

                    btn_0 = Button(cal_frame, text='0', font=("arail", 15, "bold"), command=lambda: ge_input(0),bd=5, width=4, pady=26, cursor="hand2")
                    btn_0.grid(row=4, column=0)
                    btn_c = Button(cal_frame, text='c', font=("arail", 15, "bold"), command=clear_cal, bd=5,width=4, pady=26, cursor="hand2")
                    btn_c.grid(row=4, column=1)
                    btn_eq = Button(cal_frame, text='=', font=("arail", 15, "bold"), command=perform_cal, bd=5, width=4, pady=26, cursor="hand2")
                    btn_eq.grid(row=4, column=2)
                    btn_div = Button(cal_frame, text='/', font=("arail", 15, "bold"),command=lambda: ge_input('/'), bd=5, width=4, pady=26, cursor="hand2")
                    btn_div.grid(row=4, column=3)

                    # ----------cart frame-----------
                    cart_frame = Frame(cal_cart_frame, bd=3, relief=RIDGE)
                    cart_frame.place(x=280, y=8, width=310, height=440)
                    carttitle = Label(cart_frame, text="Cart \t Total Products: [0] ",font=("goudy old style", 15), bg="lightgray")
                    carttitle.pack(side=TOP, fill=X)

                    scrolly = Scrollbar(cart_frame, orient=VERTICAL)
                    scrollx = Scrollbar(cart_frame, orient=HORIZONTAL)

                    Carttable = ttk.Treeview(cart_frame, columns=("pid", "name", "price", "qty"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
                    scrollx.pack(side=BOTTOM, fill=X)
                    scrolly.pack(side=RIGHT, fill=Y)
                    scrollx.config(command=Carttable.xview)
                    scrolly.config(command=Carttable.yview)

                    Carttable.heading("pid", text="P ID")
                    Carttable.heading("name", text="Name")
                    Carttable.heading("price", text="Price")
                    Carttable.heading("qty", text="QTY")

                    Carttable["show"] = "headings"

                    Carttable.column("pid", width=40)
                    Carttable.column("name", width=100)
                    Carttable.column("price", width=90)
                    Carttable.column("qty", width=50)
                    Carttable.pack(fill=BOTH, expand=1)
                    Carttable.bind("<ButtonRelease-1>", get_date_cart)

                    # -------------ADD cart buttons--------------
                    var_pid = StringVar()
                    var_pname = StringVar()
                    var_price = StringVar()
                    var_qty = StringVar()
                    var_stock = StringVar()

                    add_cartwidgetsframe = Frame(rot, bd=2, relief=RIDGE, bg="white")
                    add_cartwidgetsframe.place(x=420, y=655, width=600, height=110)

                    lbl_pname = Label(add_cartwidgetsframe, text="Product Name", font=("times new roman", 15), bg="white")
                    lbl_pname.place(x=5, y=5)
                    txt_pname = Entry(add_cartwidgetsframe, textvariable=var_pname, font=("times new roman", 15), bg="lightyellow", state='readonly')
                    txt_pname.place(x=5, y=35, width=190, height=22)

                    lbl_pprice = Label(add_cartwidgetsframe, text="Price Per Qty", font=("times new roman", 15),bg="white")
                    lbl_pprice.place(x=230, y=5)
                    txt_pprice = Entry(add_cartwidgetsframe, textvariable=var_price, font=("times new roman", 15),bg="lightyellow", state='readonly')
                    txt_pprice.place(x=230, y=35, width=160, height=22)

                    lbl_pqty = Label(add_cartwidgetsframe, text="Quantity", font=("times new roman", 15), bg="white")
                    lbl_pqty.place(x=430, y=5)
                    txt_pqty = Entry(add_cartwidgetsframe, textvariable=var_qty, font=("times new roman", 15), bg="lightyellow")
                    txt_pqty.place(x=430, y=35, width=150, height=22)

                    lbl_instock = Label(add_cartwidgetsframe, text="In Stock", font=("times new roman", 15), bg="white")
                    lbl_instock.place(x=5, y=70)

                    btn_clear_cart = Button(add_cartwidgetsframe, text="Clear", command=clear_cart,font=("times new roman", 15, "bold"), bg="lightgray", cursor="hand2")
                    btn_clear_cart.place(x=180, y=70, width=150, height=30)
                    btn_add_cart = Button(add_cartwidgetsframe, text="Add | Update Cart", command=add_update_cart, font=("times new roman", 15, "bold"), bg="orange", cursor="hand2")
                    btn_add_cart.place(x=360, y=70, width=180, height=30)
                    # ====================billing area===============
                    billframe = Frame(rot, bd=2, relief=RIDGE, bg="white")
                    billframe.place(x=1023, y=110, width=500, height=520)

                    Btitle = Label(billframe, text="Customer Bill Area", font=("goudy old style", 20, "bold"),bg="#f44336", fg="white")
                    Btitle.pack(side=TOP, fill=X)
                    scrolly = Scrollbar(billframe, orient=VERTICAL)
                    scrolly.pack(side=RIGHT, fill=Y)
                    txt_bill_area = Text(billframe, yscrollcommand=scrolly.set)
                    txt_bill_area.pack(fill=BOTH, expand=1)
                    scrolly.config(command=txt_bill_area.yview)

                    # =========================billing buttons======
                    billmenuframe = Frame(rot, bd=2, relief=RIDGE, bg="white")
                    billmenuframe.place(x=1023, y=630, width=500, height=140)

                    lbl_amnt = Label(billmenuframe, text='Bill Amount\n[0]', font=("goudy old style", 15, "bold"),bg="#3f51b5", fg="white")
                    lbl_amnt.place(x=2, y=5, width=160, height=70)

                    lbl_discount = Label(billmenuframe, text='Discount \n[5%]',font=("goudy old style", 15, "bold"), bg="#8bc34a", fg="white")
                    lbl_discount.place(x=165, y=5, width=160, height=70)

                    lbl_net_pay = Label(billmenuframe, text='Net Pay\n[0]', font=("goudy old style", 15, "bold"),bg="#607d8b", fg="white")
                    lbl_net_pay.place(x=328, y=5, width=160, height=70)

                    btn_print = Button(billmenuframe, text='Print', command=print_bill,font=("goudy old style", 15, "bold"), bg="lightgreen", fg="white",cursor="hand2")
                    btn_print.place(x=2, y=80, width=160, height=50)

                    btn_clear_all = Button(billmenuframe, text='Clear All', command=clear_all,font=("goudy old style", 15, "bold"), bg="gray", fg="white", cursor="hand2")
                    btn_clear_all.place(x=165, y=80, width=160, height=50)

                    btn_generate = Button(billmenuframe, text='Generate/Save Bill', command=generate_bill,font=("goudy old style", 15, "bold"), bg="#009688", fg="white",cursor="hand2")
                    btn_generate.place(x=328, y=80, width=160, height=50)

                    # ========footer=============
                    footer = Label(rot, text="Management System | Developed By M.SH",font=("times new roman", 11), bg="#4d636d", fg="white")
                    footer.pack(side=BOTTOM, fill=X)

                    show()
                    # self.bill_top()
                    update_date_time()

                    rot.mainloop()



    except Exception as ex:
        messagebox.showerror("Error", f"Error due to :{str(ex)}", parent=roots)

#=====================================================================

title=Label(login_frame,text="Login System",font=("Elephant",30,"bold"),bg="white")
title.place(x=0,y=30,relwidth=1)

lbl_user = Label(login_frame, text="Employee ID", font=("Andalus", 15), bg="white", fg="#767171")
lbl_user.place(x=50, y=150)
txt_employee_id = Entry(login_frame, textvariable=employee_id, font=("times new rowan", 15),bg="lightgray")
txt_employee_id.place(x=50, y=200,width=250)

lbl_password = Label(login_frame, text="Password", font=("Andalus", 15), bg="white", fg="#767171")
lbl_password.place(x=50, y=250)
txt_password = Entry(login_frame, textvariable=password,show='*', font=("times new rowan", 15),bg="lightgray")
txt_password.place(x=50, y=300,width=250)

btn_login=Button(login_frame,text="Log In",command=login,font=("times new roman",13),bg="blue",fg="white",bd=2,relief=GROOVE,cursor="hand2")
btn_login.place(x=50,y=400,width=250)

        #or_=Label(login_frame,text="---------------OR---------------",bg="white",fg="lightgray",font=("times new roman",15,"bold")).place(x=50,y=370)
        #btn_forget=Button(login_frame,text="Forget Password ?",command=self.forget_window,font=("times new roman",13),bg="white",fg="#00759E",bd=0,cursor="hand2").place(x=100,y=410)


roots.mainloop()