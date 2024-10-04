from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("ADVANCE FACIAL RECOGNITION ATTENDANCE SYSTEM")

        #_____________________________variable_________
        self.var_Department = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_section = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_DOB = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_TG = StringVar()
        self.var_radio1 = StringVar()


        # first image
        img = Image.open(r"C:\Users\LENOVO\Desktop\Face recognition system\image15.jpeg")
        img = img.resize((432,130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_1b1 = Label(self.root, image=self.photoimg)
        f_1b1.place(x=0, y=0, width=432, height=130)

        #second image
        img1 = Image.open(r"C:\Users\LENOVO\Desktop\Face recognition system\image16.jpeg")
        img1 = img1.resize((432, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_1b1 = Label(self.root, image=self.photoimg1)
        f_1b1.place(x=432, y=0, width=432, height=130)

        #third image

        img2 = Image.open(r"C:\Users\LENOVO\Desktop\Face recognition system\image17.jpeg")
        img2 = img2.resize((550, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_1b1 = Label(self.root, image=self.photoimg2)
        f_1b1.place(x=864, y=0, width=550, height=130)

        #baground image
        img3 = Image.open(r"C:\Users\LENOVO\Desktop\Face recognition system\image5.jpg")
        img3 = img3.resize((1400, 590), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1400, height=590)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM", font=("times new roman",35,"bold"),bg="white",fg="GREEN")
        title_lbl.place(x=0,y=0,width=1400,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=25,y=55,width=1300,height=510)

        #left label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new romain",12,"bold"))
        Left_frame.place(x=10,y=10,width=630,height=495)

        img_left = Image.open(r"C:\Users\LENOVO\Desktop\Face recognition system\image18.webp")
        img_left = img_left.resize((620, 70), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_1b1 = Label(Left_frame, image=self.photoimg_left)
        f_1b1.place(x=0, y=0, width=630, height=70)


        #current course information
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information",
                                font=("times new romain", 12, "bold"))
        current_course_frame.place(x=5, y=70, width=615, height=115)


         #department
        dep_label1=Label(current_course_frame,text="Departmental",font=("times new romain",12,"bold"),bg="white")
        dep_label1.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Department,font=("times new romain", 12 ,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","Computer Science","IT","AIML","DS","Electronics","Mechnical","Civil")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        #course
        course_label1 = Label(current_course_frame, font=("times new romain", 13, "bold"),bg="white" )
        course_label1.grid(row=0, column=2, padx=10)

        course_combo = ttk.Combobox(current_course_frame, text="Course",textvariable=self.var_course, font=("times new romain", 13, "bold"), width=17,
                                 state="readonly")
        course_combo["values"] = ("Select Course", "Btech")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10,sticky=W)


        # year
        year_label1 = Label(current_course_frame, font=("times new romain", 13, "bold"),bg="white" )
        year_label1.grid(row=1, column=0, padx=10)

        year_combo = ttk.Combobox(current_course_frame,text="Year",textvariable=self.var_year,  font=("times new romain", 13, "bold"), width=17,
                                    state="readonly")
        year_combo["values"] = ("Select Year", "2020-21", "2021-22","2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)


        #Semester
        semester_label1 = Label(current_course_frame,  font=("times new romain", 13, "bold"), bg="white")
        semester_label1.grid(row=1, column=2, padx=10)

        semester_combo = ttk.Combobox(current_course_frame, text="Semester",textvariable=self.var_semester, font=("times new romain", 13, "bold"), width=17,
                                  state="readonly")
        semester_combo["values"] = ("Select Semester", "1", "2", "3", "4","5","6","7","8")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)


         #class student information
        class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information",
                                          font=("times new romain", 12, "bold"))
        class_student_frame.place(x=5, y=185, width=615, height=285)


        #student ID
        studentID_label1 = Label(class_student_frame, text="Student ID:", font=("times new romain", 13, "bold"),
                                bg="white")
        studentID_label1.grid(row=0, column=0, padx=10,pady=5,sticky=W)

        studentID_entry = ttk.Entry(class_student_frame,textvariable=self.var_id,width=14,font=("times new romain", 13 , "bold"))
        studentID_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)


        # student name
        studentName_label1 = Label(class_student_frame, text="Student Name:", font=("times new romain", 13, "bold"),
                                 bg="white")
        studentName_label1.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_student_frame, textvariable=self.var_name,width=17, font=("times new romain", 13, "bold"))
        studentName_entry.grid(row=0, column=4, padx=10, pady=5, sticky=W)


        # class section
        classSection_label1 = Label(class_student_frame, text="Class Section:", font=("times new romain", 13, "bold"),
                                   bg="white")
        classSection_label1.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        #classSection_entry = ttk.Entry(class_student_frame,textvariable=self.var_section, width=14, font=("times new romain", 13, "bold"))
        #classSection_entry.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        classSection_combo = ttk.Combobox(class_student_frame, text="Year", textvariable=self.var_section,
                                  font=("times new romain", 12, "bold"), width=12,
                                  state="readonly")
        classSection_combo["values"] = ("Select Section", "A", "B", "C", "D")
        classSection_combo.current(0)
        classSection_combo.grid(row=1, column=2, padx=10, pady=0, sticky=W)


        # roll no
        rollNo_label1 = Label(class_student_frame, text="Roll No:", font=("times new romain", 13, "bold"),
                                     bg="white")
        rollNo_label1.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        rollNo_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll, width=17, font=("times new romain", 13, "bold"))
        rollNo_entry.grid(row=1, column=4, padx=10, pady=5, sticky=W)


        # gender
        gender_label1 = Label(class_student_frame, text="Gender:", font=("times new romain", 13, "bold"),
                              bg="white")
        gender_label1.grid(row=2, column=0, padx=10, pady=5, sticky=W)


        gender_combo = ttk.Combobox(class_student_frame, text="Year", textvariable=self.var_gender,
                                  font=("times new romain", 12, "bold"), width=12,
                                  state="readonly")
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=2, padx=10, pady=0, sticky=W)


        # DOB
        DOB_label1 = Label(class_student_frame, text="DOB:", font=("times new romain", 13, "bold"),
                              bg="white")
        DOB_label1.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        DOB_entry = ttk.Entry(class_student_frame,textvariable=self.var_DOB, width=17, font=("times new romain", 13, "bold"))
        DOB_entry.grid(row=2, column=4, padx=10, pady=5, sticky=W)


        # Email
        Email_label1 = Label(class_student_frame, text="Email:", font=("times new romain", 13, "bold"),
                              bg="white")
        Email_label1.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        Email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email,width=14, font=("times new romain", 13, "bold"))
        Email_entry.grid(row=3, column=2, padx=10, pady=5, sticky=W)


        # Phone No
        phoneNo_label1 = Label(class_student_frame, text="Phone No:", font=("times new romain", 13, "bold"),
                           bg="white")
        phoneNo_label1.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        phoneNo_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone, width=17, font=("times new romain", 13, "bold"))
        phoneNo_entry.grid(row=3, column=4, padx=10, pady=5, sticky=W)


        # Address
        address_label1 = Label(class_student_frame, text="Address:", font=("times new romain", 13, "bold"),
                             bg="white")
        address_label1.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(class_student_frame,textvariable=self.var_address, width=14, font=("times new romain", 13, "bold"))
        address_entry.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        # TG name
        TG_label1 = Label(class_student_frame, text="TG:", font=("times new romain", 13, "bold"),
                               bg="white")
        TG_label1.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        TG_entry = ttk.Entry(class_student_frame, width=17,textvariable=self.var_TG, font=("times new romain", 13, "bold"))
        TG_entry.grid(row=4, column=4, padx=10, pady=5, sticky=W)


        # radio button

        radiobtn1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1,text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=5,column=0)


        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="no")
        radiobtn2.grid(row=5,column=3)


        #buttons frame

        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=192, width=610, height=40)

        #save button
        save_btn = Button(btn_frame, width=12,height=1, text="Save",command=self.add_data, font=("times new roman", 15, "bold"), bg="blue",
                          fg="white")
        save_btn.grid(row=0, column=0)

        # delete button
        delete_btn = Button(btn_frame, width=12, height=1,text="Delete",command=self.delete_data, font=("times new roman", 15, "bold"), bg="blue",
                            fg="white")
        delete_btn.grid(row=0, column=1)

        # update button
        update_btn = Button(btn_frame, width=12,height=1, text="Update", command=self.update_data,font=("times new roman", 15, "bold"), bg="blue",
                            fg="white")
        update_btn.grid(row=0, column=2)

        # reset button
        reset_btn = Button(btn_frame, width=12,height=1, text="Reset", command=self.reset_data, font=("times new roman", 15, "bold"), bg="blue",
                           fg="white")
        reset_btn.grid(row=0, column=3)


        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE)
        btn_frame1.place(x=0, y=232, width=610, height=40)

        # take photo button
        take_photo_btn = Button(btn_frame1, width=25, height=1, text="Take Photo Sample",command=self.generate_dataset, font=("times new roman", 15, "bold"), bg="blue",
                          fg="white")
        take_photo_btn.grid(row=0, column=0)

        # update photo button
        update_photo_btn = Button(btn_frame1, width=25, height=1, text="Update Photo Sample",command=self.update_dataset, font=("times new roman", 15, "bold"),
                            bg="blue",
                            fg="white")
        update_photo_btn.grid(row=0, column=1)


        #Right label frame

        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Data",
                                font=("times new romain", 12, "bold"))
        Right_frame.place(x=650, y=10, width=630, height=510)


        img_right = Image.open(r"C:\Users\LENOVO\Desktop\Face recognition system\image19.jpg")
        img_right = img_right.resize((620, 150), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_1b1 = Label(Right_frame, image=self.photoimg_right)
        f_1b1.place(x=0, y=0, width=630, height=150)


        #search system
        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Stored Student Information",
                                          font=("times new romain", 12, "bold"))
        search_frame.place(x=5, y=150, width=615, height=70)


        #table frame
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=175, width=615, height=295)

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("Department","course","year","sem","id","name",
                                                           "section","roll","gender","DOB",'email',
                                                           "phone","address","TG","photo"),
                                        xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Department",text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("section", text="Section")
        self.student_table.heading("roll", text="RollNo")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("TG", text="TG")
        self.student_table.heading("photo", text="Photo")

        self.student_table["show"] = "headings"

        self.student_table.column("Department",width=120)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=130)
        self.student_table.column("section", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("email", width=215)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("TG", width=130)
        self.student_table.column("photo", width=100)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    #**********************Function Declaration**********************************

    def add_data(self):
        # Check if any field is empty or "Select Department" is selected
        if (self.var_Department.get() == "Select Department" or self.var_name.get() == "" or
                self.var_id.get() == ""):
            messagebox.showerror("Error", "All Fields are required",parent=self.root)
        else:
            try:
                 conn = mysql.connector.connect(host="localhost",port=3306,user="newuser",password="Sachin@9165",database="face_recognizer",auth_plugin="mysql_native_password" )

                 my_cursor=conn.cursor()
                 my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                       self.var_Department.get(),
                                                                                       self.var_course.get(),
                                                                                       self.var_year.get(),
                                                                                       self.var_semester.get(),
                                                                                       self.var_id.get(),
                                                                                       self.var_name.get(),
                                                                                       self.var_section.get(),
                                                                                       self.var_roll.get(),
                                                                                       self.var_gender.get(),
                                                                                       self.var_DOB.get(),
                                                                                       self.var_email.get(),
                                                                                       self.var_phone.get(),
                                                                                       self.var_address.get(),
                                                                                       self.var_TG.get(),
                                                                                       self.var_radio1.get()
                  ))
                 conn.commit()
                 self.fetch_data()
                 conn.close()
                 messagebox.showinfo("Success","Student details has been added successfully",
                                     parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    #######################fetch data###########################################
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",port=3306,user="newuser",password="Sachin@9165",database="face_recognizer",auth_plugin="mysql_native_password" )

        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    ################get cursor####################

    def get_cursor(self,event=""):
        cursor_focus= self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_Department.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_section.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_DOB.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_TG.set(data[13]),
        self.var_radio1.set(data[14])


   ############ update function ################

    def update_data(self):
        if (self.var_Department.get() == "Select Department" or self.var_name.get() == "" or
            self.var_id.get() == ""):
              messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
             try:
                 Update = messagebox.askyesno("Update", "Do You Want To Update This Student's Details?", parent=self.root)
                 if Update > 0:
                      conn = mysql.connector.connect(host="localhost",port=3306,user="newuser",password="Sachin@9165",database="face_recognizer",auth_plugin="mysql_native_password")

                      my_cursor = conn.cursor()
                      my_cursor.execute(
                                    "UPDATE student SET Department=%s, course=%s, year=%s, semester=%s, name=%s, section=%s, rollno=%s, gender=%s, DOB=%s, email=%s, phone=%s, address=%s, TG=%s, photosample=%s WHERE StudentID=%s",
                                     (
                                     self.var_Department.get(),
                                     self.var_course.get(),
                                     self.var_year.get(),
                                     self.var_semester.get(),
                                     self.var_name.get(),
                                     self.var_section.get(),
                                     self.var_roll.get(),
                                     self.var_gender.get(),
                                     self.var_DOB.get(),
                                     self.var_email.get(),
                                     self.var_phone.get(),
                                     self.var_address.get(),
                                     self.var_TG.get(),
                                     self.var_radio1.get(),
                                     self.var_id.get()
                                        )
                                        )
                 else:
                      if not Update:
                             return
                 messagebox.showinfo("Success", "Student Details Successfully Updated", parent=self.root)
                 conn.commit()
                 self.fetch_data()
                 conn.close()

             except Exception as es:
                   messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    ############## delete function#################################
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror( "Error" , "Student id must be required", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student details?", parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",port=3306,user="newuser",password="Sachin@9165",database="face_recognizer",auth_plugin="mysql_native_password")
                    my_cursor = conn.cursor()
                    sql="delete from student where StudentID=%s"
                    val= (self.var_id.get(),)
                    my_cursor.execute(sql,val)

                else:
                     if not delete:
                         return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)


########################## reset button#########################8
    def reset_data(self):
        self.var_Department.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_section.set("Select Section")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_DOB.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_TG.set("")
        self.var_radio1.set("")


        ##############  generate dataset or take photo  sample   ##################

    def generate_dataset(self):
        if (self.var_Department.get() == "Select Department" or self.var_name.get() == "" or
                self.var_id.get() == ""):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",port=3306,user="newuser",password="Sachin@9165", database="face_recognizer",auth_plugin="mysql_native_password" )
                my_cursor = conn.cursor()

                # Check if the student ID exists
                my_cursor.execute("SELECT COUNT(*) FROM student WHERE StudentID=%s", (self.var_id.get(),))
                count = my_cursor.fetchone()[0]

                if count == 0:
                    messagebox.showerror("Error", "Student ID does not exist in the database", parent=self.root)
                    conn.close()
                    return

                # Ensure the directory exists
                save_path = r"C:\Users\LENOVO\Desktop\Face recognition system\data"
                if not os.path.exists(save_path):
                    os.makedirs(save_path)

                # Load predefined data on face frontals from OpenCV
                face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    if len(faces) == 0:
                        return None
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if not ret:
                        break

                    face = face_cropped(my_frame)
                    if face is not None:
                        img_id += 1
                        face = cv2.resize(face, (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = os.path.join(save_path, f"user.{self.var_id.get()}.{img_id}.jpg")
                        cv2.imwrite(file_name_path, face)

                        # Put text on the face image at a fixed position (e.g., top-left corner)
                        position = (50, 50)  # X, Y coordinates of where to put the text
                        cv2.putText(face, str(img_id), position, cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)

                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or img_id == 100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating dataset completed")
                conn.close()

            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror("Error", "Student ID is required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student?",
                                             parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost",port=3306,user="newuser",password="Sachin@9165",database="face_recognizer",auth_plugin="mysql_native_password")
                    my_cursor = conn.cursor()

                    # Delete student record from database
                    sql = "DELETE FROM student WHERE StudentID=%s"
                    val = (self.var_id.get(),)
                    my_cursor.execute(sql, val)

                    # Commit the deletion
                    conn.commit()

                    # Delete associated images
                    save_path = r"C:\Users\LENOVO\Desktop\Face recognition system\data"
                    if os.path.exists(save_path):
                        for file_name in os.listdir(save_path):
                            if file_name.startswith(f"user.{self.var_id.get()}."):
                                file_path = os.path.join(save_path, file_name)
                                os.remove(file_path)

                    conn.close()

                    self.fetch_data()  # Refresh data
                    self.reset_data()  # Reset form
                    messagebox.showinfo("Delete", "Student details and images successfully deleted", parent=self.root)

                else:
                    if not delete:
                        return

            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)



    ############update dataset or update photo sample####################

    def update_dataset(self):
        if (self.var_Department.get() == "Select Department" or self.var_name.get() == "" or
                self.var_id.get() == ""):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update Photo Sample",
                                             "Do you want to update the photo sample for this student?",
                                             parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(host="localhost", port=3306,user="newuser",password="Sachin@9165",database="face_recognizer",auth_plugin="mysql_native_password")
                    my_cursor = conn.cursor()

                    # Update student record in database
                    my_cursor.execute(
                        """UPDATE student 
                        SET Department=%s, course=%s, year=%s, semester=%s, name=%s, section=%s, rollno=%s, gender=%s, 
                            DOB=%s, email=%s, phone=%s, address=%s, TG=%s 
                        WHERE StudentID=%s""",
                        (
                            self.var_Department.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_name.get(),
                            self.var_section.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_DOB.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_TG.get(),
                            self.var_id.get()
                        )
                    )
                    conn.commit()

                    # Delete existing photo samples
                    save_path = r"C:\Users\LENOVO\Desktop\Face recognition system\data"
                    if os.path.exists(save_path):
                        for file_name in os.listdir(save_path):
                            if file_name.startswith(f"user.{self.var_id.get()}."):
                                file_path = os.path.join(save_path, file_name)
                                os.remove(file_path)

                    conn.close()

                    # Capture new photo samples
                    self.capture_photo_samples()

                    messagebox.showinfo("Success", "Photo samples updated successfully", parent=self.root)

                else:
                    if not update:
                        return

            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    def capture_photo_samples(self):
        save_path = r"C:\Users\LENOVO\Desktop\Face recognition system\data"
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        # Load predefined data on face frontals from OpenCV
        face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

        def face_cropped(img):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray, 1.3, 5)
            if len(faces) == 0:
                return None
            for (x, y, w, h) in faces:
                face_cropped = img[y:y + h, x:x + w]
                return face_cropped

        cap = cv2.VideoCapture(0)
        img_id = 0
        while True:
            ret, my_frame = cap.read()
            if not ret:
                break

            face = face_cropped(my_frame)
            if face is not None:
                img_id += 1
                face = cv2.resize(face, (450, 450))
                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                file_name_path = os.path.join(save_path, f"user.{self.var_id.get()}.{img_id}.jpg")
                cv2.imwrite(file_name_path, face)

                # Put text on the face image at a fixed position (e.g., top-left corner)
                position = (50, 50)  # X, Y coordinates of where to put the text
                cv2.putText(face, str(img_id), position, cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)

                cv2.imshow("Cropped Face", face)

            if cv2.waitKey(1) == 13 or img_id == 100:
                break

        cap.release()
        cv2.destroyAllWindows()


    def open_img(self):
        os.startfile("save_path")


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()

