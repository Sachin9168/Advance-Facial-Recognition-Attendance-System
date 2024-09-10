from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os
import csv
from tkinter import  filedialog

mydata=[]
class Attendence:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("AI Based Face Attendance System")


        # _____________________________variable_________
        self.var_ID = StringVar()
        self.var_RollNo = StringVar()
        self.var_NAme = StringVar()
        self.var_Department = StringVar()
        self.var_Date = StringVar()
        self.var_Time = StringVar()
        self.var_AttendanceStatus = StringVar()


        # first image
        img = Image.open(r"C:\Users\LENOVO\Desktop\Face recognition system\image31.jpg")
        img = img.resize((432, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_1b1 = Label(self.root, image=self.photoimg)
        f_1b1.place(x=0, y=0, width=432, height=130)

        # second image
        img1 = Image.open(r"C:\Users\LENOVO\Desktop\Face recognition system\image29.jpg")
        img1 = img1.resize((432, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_1b1 = Label(self.root, image=self.photoimg1)
        f_1b1.place(x=432, y=0, width=432, height=130)

        # third image

        img2 = Image.open(r"C:\Users\LENOVO\Desktop\Face recognition system\image30.jpg")
        img2 = img2.resize((550, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_1b1 = Label(self.root, image=self.photoimg2)
        f_1b1.place(x=864, y=0, width=550, height=130)

        # baground image
        img3 = Image.open(r"C:\Users\LENOVO\Desktop\Face recognition system\image5.jpg")
        img3 = img3.resize((1400, 590), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1400, height=590)

        title_lbl = Label(bg_img, text="ATTENDENCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white",
                          fg="GREEN")
        title_lbl.place(x=0, y=0, width=1400, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=25, y=55, width=1300, height=510)

        # left label frame

        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details",
                                font=("times new romain", 12, "bold"))
        Left_frame.place(x=10, y=10, width=630, height=495)

        img_left = Image.open(r"C:\Users\LENOVO\Desktop\Face recognition system\image19.jpg")
        img_left = img_left.resize((620, 200), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_1b1 = Label(Left_frame, image=self.photoimg_left)
        f_1b1.place(x=0, y=0, width=630, height=200)


        # student attendance details
        student_attendance_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE,
                                         font=("times new romain", 12, "bold"))
        student_attendance_frame.place(x=5, y=200, width=615, height=270)

        # Attendance ID
        AttendanceID_label1 = Label(student_attendance_frame, text="Attendance ID:", font=("times new romain", 13, "bold"),
                                 bg="white")
        AttendanceID_label1.grid(row=0, column=0, padx=5, pady=10, sticky=W)

        AttendanceID_entry = ttk.Entry(student_attendance_frame,textvariable=self.var_ID, width=14,
                                    font=("times new romain", 13, "bold"))
        AttendanceID_entry.grid(row=0, column=2, padx=5, pady=10, sticky=W)

        # rollno
        rollno_label1 = Label(student_attendance_frame, text="Roll No:", font=("times new romain", 13, "bold"),
                                   bg="white")
        rollno_label1.grid(row=0, column=3, padx=5, pady=10, sticky=W)

        rollno_entry = ttk.Entry(student_attendance_frame, textvariable=self.var_RollNo, width=17,
                                      font=("times new romain", 13, "bold"))
        rollno_entry.grid(row=0, column=4, padx=5, pady=10, sticky=W)

        # Name
        Name_label1 = Label(student_attendance_frame, text="Name:", font=("times new romain", 13, "bold"),
                                    bg="white")
        Name_label1.grid(row=1, column=0, padx=5, pady=10, sticky=W)

        Name_entry = ttk.Entry(student_attendance_frame, textvariable=self.var_NAme,width=14, font=("times new romain", 13, "bold"))
        Name_entry.grid(row=1, column=2, padx=5, pady=10, sticky=W)


        # Department
        Department_label1 = Label(student_attendance_frame, text="Department:", font=("times new romain", 13, "bold"),
                              bg="white")
        Department_label1.grid(row=1, column=3, padx=5, pady=10, sticky=W)

        Department_entry = ttk.Entry(student_attendance_frame,textvariable=self.var_Department,  width=17,
                                 font=("times new romain", 13, "bold"))
        Department_entry.grid(row=1, column=4, padx=5, pady=10, sticky=W)

        # Time
        Time_label1 = Label(student_attendance_frame, text="Time:", font=("times new romain", 13, "bold"),
                               bg="white")
        Time_label1.grid(row=2, column=0, padx=5, pady=10, sticky=W)

        Time_entry = ttk.Entry(student_attendance_frame,textvariable=self.var_Time, width=14,
                                  font=("times new romain", 13, "bold"))
        Time_entry.grid(row=2, column=2, padx=5, pady=10, sticky=W)


        # Date
        Date_label1 = Label(student_attendance_frame, text="Date:", font=("times new romain", 13, "bold"),
                           bg="white")
        Date_label1.grid(row=2, column=3, padx=5, pady=10, sticky=W)

        Date_entry = ttk.Entry(student_attendance_frame,textvariable=self.var_Date,  width=17,
                              font=("times new romain", 13, "bold"))
        Date_entry.grid(row=2, column=4, padx=5, pady=10, sticky=W)

        # Attendance status
        attendance_status_label1 = Label(student_attendance_frame, text="Attendence Status:", font=("times new romain", 13, "bold"),
                             bg="white")
        attendance_status_label1.grid(row=3, column=0, padx=5, pady=15, sticky=W)

        attendance_status_entry = ttk.Entry(student_attendance_frame, textvariable=self.var_AttendanceStatus, width=14,
                               font=("times new romain", 13, "bold"))
        attendance_status_entry.grid(row=3, column=2, padx=5, pady=15, sticky=W)

        # buttons frame

        btn_frame = Frame(student_attendance_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=190, width=610, height=40)

        # Import CSV button
        importCSV_btn = Button(btn_frame,text="Import CSV",command=self.importCsv, width=16, height=1,
                          font=("times new roman", 15, "bold"), bg="blue",
                          fg="white")
        importCSV_btn.grid(row=0, column=0)

        # Export CSV button
        exportCSV_btn = Button(btn_frame,text="Export CSV", command=self.exportCsv,width=16, height=1,
                            font=("times new roman", 15, "bold"), bg="blue",
                            fg="white")
        exportCSV_btn.grid(row=0, column=1)

        # reset button
        reset_btn = Button(btn_frame, text="Reset",width=16, height=1,command=self.reset_data,                           font=("times new roman", 15, "bold"), bg="blue",
                           fg="white")
        reset_btn.grid(row=0, column=3)

        #Button1

        btn1_frame = Frame(student_attendance_frame, bd=2, relief=RIDGE)
        btn1_frame.place(x=0, y=230, width=610, height=40)

        # save button
        save_btn = Button(btn1_frame, text="Save", command=self.add_data, width=25, height=1,
                          font=("times new roman", 15, "bold"), bg="blue",
                          fg="white")
        save_btn.grid(row=1, column=0)

        # delete button
        delete_btn = Button(btn1_frame, text="Delete",command=self.delete_data,  width=25, height=1,
                            font=("times new roman", 15, "bold"), bg="blue",
                            fg="white")
        delete_btn.grid(row=1, column=1)



        # Right label frame

        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text=" Attendance Details",
                                 font=("times new romain", 12, "bold"))
        Right_frame.place(x=650, y=10, width=630, height=510)


        # table frame
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=0, width=615, height=475)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, columns=("ID", "RollNo", "Name", "Department", "Time", "Date",
                                                                "AttendanceStatus"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("ID", text="AttendanceID")
        self.AttendanceReportTable.heading("RollNo", text="RollNo")
        self.AttendanceReportTable.heading("Name", text="Name")
        self.AttendanceReportTable.heading("Department", text="Department")
        self.AttendanceReportTable.heading("Date", text="Date")
        self.AttendanceReportTable.heading("Time", text="time")
        self.AttendanceReportTable.heading("AttendanceStatus", text="AttandenceStatus")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("ID", width=100)
        self.AttendanceReportTable.column("RollNo", width=100)
        self.AttendanceReportTable.column("Name", width=100)
        self.AttendanceReportTable.column("Department", width=100)
        self.AttendanceReportTable.column("Date", width=100)
        self.AttendanceReportTable.column("Time", width=100)
        self.AttendanceReportTable.column("AttendanceStatus", width=100)


        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #=============== fetch data =========================

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    #  import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fin=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV Fie","*.csv"),("All File","*.*")),parent=self.root)
        with open(fin) as myfile:
            csvread= csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
                self.fetchData(mydata)


    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found To Export",parent= self.root)
                return  False
            fin = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV",
                                         filetypes=(("CSV Fie", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fin,mode="w",newline="") as myfile:
               exp_write=csv.writer(myfile,delimiter=",")
               for i in mydata:
                  exp_write.writerow(i)
               messagebox.showinfo("Data Export","Your Data Exported to " + os.path.basename(fin)+"Successfully")

        except Exception as es:
            messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        row=content['values']
        self.var_ID.set(row[0])
        self.var_RollNo.set(row[1])
        self.var_NAme.set(row[2])
        self.var_Department.set(row[3])
        self.var_Time.set(row[4])
        self.var_Date.set(row[5])
        self.var_AttendanceStatus.set(row[6])

    def add_data(self):
        # Check if any field is empty or "Select Department" is selected
        if (self.var_Department.get() == "" or self.var_NAme.get() == "" or
                self.var_RollNo.get() == ""):
            messagebox.showerror("Error", "All Fields are required",parent=self.root)
        else:
            try:
                 conn = mysql.connector.connect(host="localhost",port=3306,user="newuser",password="Sachin@9165",database="face_recognizer",auth_plugin="mysql_native_password" )

                 my_cursor=conn.cursor()
                 my_cursor.execute("insert into attendance values(%s,%s,%s,%s,%s,%s,%s)",(
                     self.var_ID.get(),
                     self.var_RollNo.get(),
                     self.var_NAme.get(),
                     self.var_Department.get(),
                     self.var_Time.get(),
                     self.var_Date.get(),
                     self.var_AttendanceStatus.get()
                 ))
                 conn.commit()
                 self.fetch_data()
                 conn.close()
                 messagebox.showinfo("Success","Student Attendance has been added successfully",
                                     parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    def delete_data(self):
        if self.var_ID.get()=="":
            messagebox.showerror( "Error" , "Student id must be required", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student attendance?", parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",port=3306,user="newuser",password="Sachin@9165",database="face_recognizer",auth_plugin="mysql_native_password")
                    my_cursor = conn.cursor()
                    sql="delete from attendance where AttendanceID=%s"
                    val= (self.var_ID.get(),)
                    my_cursor.execute(sql,val)

                else:
                     if not delete:
                         return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student attendance", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)




    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",port=3306,user="newuser",password="Sachin@9165",database="face_recognizer",auth_plugin="mysql_native_password" )

        my_cursor = conn.cursor()
        my_cursor.execute("select * from attendance")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
            for i in data:
                self.AttendanceReportTable.insert("",END,values=i)
            conn.commit()
        conn.close()


    def reset_data(self):
        self.var_ID.set("")
        self.var_RollNo.set("")
        self.var_NAme.set("")
        self.var_Department.set("")
        self.var_Time.set("")
        self.var_Date.set("")
        self.var_AttendanceStatus.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Attendence(root)
    root.mainloop()
