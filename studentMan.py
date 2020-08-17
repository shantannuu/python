import tkinter,random,pymysql
from tkinter import ttk
from tkinter import messagebox

class Student_management:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1450x800+0+0")
        self.root.title("Student Management")
        
        # title
        title = tkinter.Label(self.root,text="STUDENTS ENROLLMENT",font=("times new roman",30,"bold"),fg="red",bg="yellow",pady=15)
        title.pack(fill= "x",side="top")

        # all Variables
        self.Roll_var=tkinter.StringVar()
        self.Name_var=tkinter.StringVar()
        self.Standard_var=tkinter.StringVar()
        self.Stream_var=tkinter.StringVar()
        self.Subjects_var=tkinter.StringVar()
        self.Fee_var=tkinter.StringVar()
        self.paid=tkinter.IntVar()
        self.unpaid=tkinter.IntVar()
        self.search_by = tkinter.StringVar()
        self.search_txt = tkinter.StringVar()
        self.total=tkinter.IntVar()


        # Manage details
        f1 = tkinter.LabelFrame(self.root,text="MANAGE STUDENTS",font=("times new roman",15,"bold"),bd=3)
        f1.place(x=20,y=90,width=470,height=560)

        stu_roll = tkinter.Label(f1,text="Student Roll No :",font=("times new roman",15,"bold"))
        stu_roll.grid(row=0,column=0,padx=20,pady=10,sticky="w")

        stu_roll_txt = tkinter.Entry(f1,font=("times new roman",15),width=25,textvariable=self.Roll_var).grid(row=0,column=1,padx=20,pady=10,sticky="w")

        stu_name = tkinter.Label(f1,text="Student Name :",font=("times new roman",15,"bold"))
        stu_name.grid(row=1,column=0,padx=20,pady=10,sticky="w")

        stu_name_txt = tkinter.Entry(f1,font=("times new roman",15),width=25,textvariable=self.Name_var).grid(row=1,column=1,padx=20,pady=10,sticky="w")

        stu_std = tkinter.Label(f1,text="Student Standard :",font=("times new roman",15,"bold"))
        stu_std.grid(row=2,column=0,padx=20,pady=10,sticky="w")

        stu_std_txt = ttk.Combobox(f1,textvariable=self.Standard_var,font=("times new roman",15,"bold"),state="readonly")
        stu_std_txt['values']=("5th","6th","7th","8th","9th","10th")
        stu_std_txt.grid(row=2,column=1,padx=20,pady=10,sticky="w")

        stu_stream = tkinter.Label(f1,text="Student Stream :",font=("times new roman",15,"bold"))
        stu_stream.grid(row=3,column=0,padx=20,pady=10,sticky="w")

        stu_stream_txt = ttk.Combobox(f1,textvariable=self.Stream_var,font=("times new roman",15,"bold"),state="readonly")
        stu_stream_txt['values']=("CBSC","SSC")
        stu_stream_txt.grid(row=3,column=1,padx=20,pady=10,sticky="w")

        stu_subject = tkinter.Label(f1,text="Student Subject :",font=("times new roman",15,"bold"))
        stu_subject.grid(row=4,column=0,padx=20,pady=10,sticky="w")

        stu_subject_txt = ttk.Combobox(f1,textvariable=self.Subjects_var,font=("times new roman",15,"bold"),state="readonly")
        stu_subject_txt['values']=("Marathi","Hindi","Sanskrit","Marathi-Sanskrit","Hindi-Sanskrit","Hindi-Marathi")
        stu_subject_txt.grid(row=4,column=1,padx=20,pady=10,sticky="w")

        fee_type = tkinter.Label(f1,text="Fee Type :",font=("times new roman",15,"bold"))
        fee_type.grid(row=5,column=0,padx=20,pady=10,sticky="w")

        fee_type_txt = ttk.Combobox(f1,textvariable=self.Fee_var,font=("times new roman",15,"bold"),state="readonly")
        fee_type_txt['values']=("Monthly","Quaterly","Half-Yearly","Yearly")
        fee_type_txt.grid(row=5,column=1,padx=20,pady=10,sticky="w")

        stu_paid = tkinter.Label(f1,text="Paid :",font=("times new roman",15,"bold"))
        stu_paid.grid(row=6,column=0,padx=20,pady=10,sticky="w")

        stu_paid_txt = tkinter.Entry(f1,textvariable=self.paid,font=("times new roman",15),width=25).grid(row=6,column=1,padx=20,pady=10,sticky="w")


        # buttons
        f2 = tkinter.Frame(f1,bd=1,relief="solid")
        f2.place(x=5,y=380,width=450,height=100)

        Add_stu=tkinter.Button(f2,command=self.add_student,text="ADD",pady=10,width=12,font=("times new roman",15,"bold"),bd=5).grid(row=0,column=0,padx=5,pady=10)

        update_stu=tkinter.Button(f2,command=self.update,text="Update",pady=10,width=12,font=("times new roman",15,"bold"),bd=5).grid(row=0,column=1,padx=5,pady=10)
        
        Delete_stu=tkinter.Button(f2,command=self.delete_data,text="Delete",pady=10,width=12,font=("times new roman",15,"bold"),bd=5).grid(row=0,column=2,padx=5,pady=10)
        
        clear=tkinter.Button(f2,command=self.clear,text="Clear",pady=10,width=12,font=("times new roman",15,
        "bold"),bd=5).grid(row=0,column=3,padx=5,pady=10)

        # students details
        f3 = tkinter.LabelFrame(self.root,text="STUDENTS DETAILS",font=("times new roman",15,"bold"),bd=3)
        f3.place(x=500,y=90,width=900,height=560)

        search_by = tkinter.Label(f3,text="Search By :",font=("times new roman",15,"bold"))
        search_by.grid(row=0,column=0,padx=20,pady=10,sticky="w")

        search_by_txt = ttk.Combobox(f3,textvariable=self.search_by,font=("times new roman",15,"bold"),state="readonly")
        search_by_txt['values']=("roll_no","name","standard","stream","fee")
        search_by_txt.grid(row=0,column=1,padx=20,pady=10,sticky="w")

        search_txt = tkinter.Entry(f3,textvariable=self.search_txt,font=("times new roman",15),width=25).grid(row=0,column=2,padx=10,pady=5)

        btn = tkinter.Button(f3,command=self.search_data,text="Search",width=15,bd=7,font=("times new roman",15,"bold"),pady=3,activeforeground = "red").grid(row=0,column=3,padx=10,pady=5)

        Show_btn = tkinter.Button(f3,command=self.fetch_data,text="showAll",width=15,bd=7,font=("times new roman",15,"bold"),pady=3,activeforeground = "red").grid(row=0,column=4,padx=10,pady=5)


        # student database
        f4 = tkinter.Frame(f3,bd=1,relief="solid")
        f4.place(x=10,y=60,width=870,height=470)

        scroll_x=tkinter.Scrollbar(f4,orient="horizontal")
        scroll_y=tkinter.Scrollbar(f4,orient="vertical")

        self.student_table=ttk.Treeview(f4,columns=("Roll","Name","Standard","Stream","Subjects","Fee","Paid","Date","Unpaid"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side="bottom",fill="x")
        scroll_y.pack(side="right",fill="y")
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Roll",text="Roll No.")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Standard",text="Standard")
        self.student_table.heading("Stream",text="Stream")
        self.student_table.heading("Subjects",text="Subjects")
        self.student_table.heading("Fee",text="Fee")
        self.student_table.heading("Paid",text="Paid")
        self.student_table.heading("Date",text="Date")
        self.student_table.heading("Unpaid",text="Unpaid")
        self.student_table['show']='headings'
        self.student_table.column("Roll",width=100)
        self.student_table.column("Name",width=150)
        self.student_table.column("Standard",width=150)
        self.student_table.column("Stream",width=150)
        self.student_table.column("Subjects",width=150)
        self.student_table.column("Fee",width=150)
        self.student_table.column("Paid",width=150)
        self.student_table.column("Date",width=170)
        self.student_table.column("Unpaid",width=150)
        self.student_table.pack(fill="both",expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    #     f5 = tkinter.Frame(self.root,bd=1,relief="solid")
    #     f5.place(x=520,y=670,width=870,height=100)

    #     total = tkinter.Label(f5,text="Total Money :",font=("times new roman",15,"bold"))
    #     total.grid(row=0,column=0,padx=20,pady=10,sticky="w")

    #     total_txt = tkinter.Entry(f5,font=("times new roman",15),width=25,textvariable=self.total).grid(row=0,column=1,padx=20,pady=10,sticky="w")

    # def total(self):
    #     self.money = 

    def add_student(self):
        if self.Roll_var.get()=="" or self.Name_var.get()=="" or self.Standard_var.get()=="" or self.Stream_var.get()=="" or self.Subjects_var.get()=="" or self.Fee_var.get()=="":
            messagebox.showerror("Error","All Fields are Required")
        else:
            # "Monthly","Quaterly","Half-Yearly","Yearly"
            con=pymysql.connect(host="localhost",user="root",password="",database="stm")
            cur=con.cursor()
            if self.Standard_var.get()=="8th" and self.Subjects_var.get()=="Sanskrit" and self.Stream_var.get()=="SSC":
                cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Roll_var.get(),self.Name_var.get(),self.Standard_var.get(),self.Stream_var.get(),self.Subjects_var.get(),self.Fee_var.get(),self.paid.get(),current_timestamp(),(6000-self.paid.get())))
            elif self.Standard_var.get()=="9th" and self.Subjects_var.get()=="Sanskrit" and self.Stream_var.get()=="SSC":
                cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Roll_var.get(),self.Name_var.get(),self.Standard_var.get(),self.Stream_var.get(),self.Subjects_var.get(),self.Fee_var.get(),self.paid.get(),current_timestamp(),(7000-self.paid.get())))
            elif self.Standard_var.get()=="10th" and self.Subjects_var.get()=="Sanskrit" and self.Stream_var.get()=="SSC":
                cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Roll_var.get(),self.Name_var.get(),self.Standard_var.get(),self.Stream_var.get(),self.Subjects_var.get(),self.Fee_var.get(),self.paid.get(),current_timestamp(),(8000-self.paid.get())))
            elif self.Standard_var.get()=="8th" and self.Subjects_var.get()=="Hindi" and self.Stream_var.get()=="SSC":
                cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Roll_var.get(),self.Name_var.get(),self.Standard_var.get(),self.Stream_var.get(),self.Subjects_var.get(),self.Fee_var.get(),self.paid.get(),current_timestamp(),(4000-self.paid.get())))
            elif self.Standard_var.get()=="9th" and self.Subjects_var.get()=="Hindi" and self.Stream_var.get()=="SSC":
                cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Roll_var.get(),self.Name_var.get(),self.Standard_var.get(),self.Stream_var.get(),self.Subjects_var.get(),self.Fee_var.get(),self.paid.get(),current_timestamp(),(5000-self.paid.get())))
            elif self.Standard_var.get()=="10th" and self.Subjects_var.get()=="Hindi" and self.Stream_var.get()=="SSC":
                cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Roll_var.get(),self.Name_var.get(),self.Standard_var.get(),self.Stream_var.get(),self.Subjects_var.get(),self.Fee_var.get(),self.paid.get(),current_timestamp(),(6000-self.paid.get())))
            elif self.Standard_var.get()=="8th" and self.Subjects_var.get()=="Marathi" and self.Stream_var.get()=="SSC":
                cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Roll_var.get(),self.Name_var.get(),self.Standard_var.get(),self.Stream_var.get(),self.Subjects_var.get(),self.Fee_var.get(),self.paid.get(),current_timestamp(),(4000-self.paid.get())))
            elif self.Standard_var.get()=="9th" and self.Subjects_var.get()=="Marathi" and self.Stream_var.get()=="SSC":
                cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Roll_var.get(),self.Name_var.get(),self.Standard_var.get(),self.Stream_var.get(),self.Subjects_var.get(),self.Fee_var.get(),self.paid.get(),current_timestamp(),(5000-self.paid.get())))
            elif self.Standard_var.get()=="10th" and self.Subjects_var.get()=="Marathi" and self.Stream_var.get()=="SSC":
                cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Roll_var.get(),self.Name_var.get(),self.Standard_var.get(),self.Stream_var.get(),self.Subjects_var.get(),self.Fee_var.get(),self.paid.get(),current_timestamp(),(6000-self.paid.get())))
            elif self.Standard_var.get()=="5th" and self.Subjects_var.get()=="Marathi" and self.Stream_var.get()=="SSC":
                cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Roll_var.get(),self.Name_var.get(),self.Standard_var.get(),self.Stream_var.get(),self.Subjects_var.get(),self.Fee_var.get(),self.paid.get(),current_timestamp(),(2500-self.paid.get())))
            elif self.Standard_var.get()=="5th" and self.Subjects_var.get()=="Hindi" and self.Stream_var.get()=="SSC":
                cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Roll_var.get(),self.Name_var.get(),self.Standard_var.get(),self.Stream_var.get(),self.Subjects_var.get(),self.Fee_var.get(),self.paid.get(),current_timestamp(),(2500-self.paid.get())))
            elif self.Standard_var.get()=="6th" and self.Subjects_var.get()=="Marathi" and self.Stream_var.get()=="SSC":
                cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Roll_var.get(),self.Name_var.get(),self.Standard_var.get(),self.Stream_var.get(),self.Subjects_var.get(),self.Fee_var.get(),self.paid.get(),current_timestamp(),(3000-self.paid.get())))
            elif self.Standard_var.get()=="6th" and self.Subjects_var.get()=="Hindi" and self.Stream_var.get()=="SSC":
                cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Roll_var.get(),self.Name_var.get(),self.Standard_var.get(),self.Stream_var.get(),self.Subjects_var.get(),self.Fee_var.get(),self.paid.get(),current_timestamp(),(3000-self.paid.get())))
            elif self.Standard_var.get()=="7th" and self.Subjects_var.get()=="Marathi" and self.Stream_var.get()=="SSC":
                cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Roll_var.get(),self.Name_var.get(),self.Standard_var.get(),self.Stream_var.get(),self.Subjects_var.get(),self.Fee_var.get(),self.paid.get(),current_timestamp(),(3500-self.paid.get())))
            elif self.Standard_var.get()=="7th" and self.Subjects_var.get()=="Hindi" and self.Stream_var.get()=="SSC":
                cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Roll_var.get(),self.Name_var.get(),self.Standard_var.get(),self.Stream_var.get(),self.Subjects_var.get(),self.Fee_var.get(),self.paid.get(),current_timestamp(),(3500-self.paid.get())))
            elif self.Standard_var.get()=="9th" and self.Subjects_var.get()=="Marathi-Sanskrit" and self.Stream_var.get()=="SSC":
                cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Roll_var.get(),self.Name_var.get(),self.Standard_var.get(),self.Stream_var.get(),self.Subjects_var.get(),self.Fee_var.get(),self.paid.get(),current_timestamp(),(12000-self.paid.get())))
            elif self.Standard_var.get()=="8th" and self.Subjects_var.get()=="Hindi-Sanskrit" and self.Stream_var.get()=="CBSC":
                cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Roll_var.get(),self.Name_var.get(),self.Standard_var.get(),self.Stream_var.get(),self.Subjects_var.get(),self.Fee_var.get(),self.paid.get(),current_timestamp(),(15000-self.paid.get())))
            elif self.Standard_var.get()=="10th" and self.Subjects_var.get()=="Sanskrit" and self.Stream_var.get()=="SSC":
                cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Roll_var.get(),self.Name_var.get(),self.Standard_var.get(),self.Stream_var.get(),self.Subjects_var.get(),self.Fee_var.get(),self.paid.get(),current_timestamp(),(8000-self.paid.get())))
            elif self.Standard_var.get()=="8th" and self.Subjects_var.get()=="Hindi-Marathi" and self.Stream_var.get()=="SSC":
                cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Roll_var.get(),self.Name_var.get(),self.Standard_var.get(),self.Stream_var.get(),self.Subjects_var.get(),self.Fee_var.get(),self.paid.get(),current_timestamp(),(8000-self.paid.get())))
            else:
                messagebox.showerror("Error","Please put rights records")
                # "Sanskrit","Marathi-Sanskrit","Hindi-Sanskrit","Hindi-Marathi"
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Succes","record has been inserted")

    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',tkinter.END,values=row)
            con.commit()
        con.close()
    
    def clear(self):
        self.Roll_var.set("")
        self.Name_var.set("")
        self.Standard_var.set("")
        self.Stream_var.set("")
        self.Subjects_var.set("")
        self.Fee_var.set("")
        self.paid.set("")

    def get_cursor(self,ev):
        cursor_row=self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row=contents['values']
        self.Roll_var.set(row[0])
        self.Name_var.set(row[1])
        self.Standard_var.set(row[2])
        self.Stream_var.set(row[3])
        self.Subjects_var.set(row[4])
        self.Fee_var.set(row[5])
        self.paid.set(row[6])

    def update(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("update students set name=%s,standard=%s,stream=%s,subjects=%s,fee=%s where roll_no=%s",(self.Name_var.get(),self.Standard_var.get(),self.Stream_var.get(),self.Subjects_var.get(),self.Fee_var.get(),self.Roll_var.get()))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("delete from students where roll_no=%s",self.Roll_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
    
    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',tkinter.END,values=row)
            con.commit()
        con.close()

root = tkinter.Tk()
obj = Student_management(root)

root.mainloop()
