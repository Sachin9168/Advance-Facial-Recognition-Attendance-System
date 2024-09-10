from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox

class Register:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("AI Based Face Attendance System")

        #============================= variable=================================
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_cNo = StringVar()
        self.var_email = StringVar()
        self.var_SecurityQ = StringVar()
        self.var_SecurityA = StringVar()
        self.var_pass = StringVar()
        self.var_Cpass = StringVar()

        # first image
        img = Image.open(r"C:\Users\LENOVO\Desktop\Face recognition system\image38.jpeg")
        img = img.resize((1370, 760), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_1b1 = Label(self.root, image=self.photoimg)
        f_1b1.place(x=0, y=0, width=1370, height=760)

        frame = Frame(self.root, bg="white")
        frame.place(x=350, y=120, width=700, height=540)

        title_lbl = Label(self.root, text="AI BASED FACE ATTENDANCE SYSTEM", font=("times new roman", 25, "bold"),
                          bg="blue", fg="white")
        title_lbl.place(x=350, y=60, width=700, height=60)

        title_lbl = Label(self.root, text="NEW USER REGISTRATION", font=("times new roman", 35, "bold"),
                          bg="white", fg="black")
        title_lbl.place(x=375, y=120, width=650, height=60)

        firstName_lbl = Label(self.root, text="First Name:", font=("times new roman", 28, "bold"),
                              bg="white", fg="black")
        firstName_lbl.place(x=390, y=220, width=210, height=30)

        self.txtFirstName = ttk.Entry(frame, textvariable=self.var_fname, font=("times new romain", 15, "bold"))
        self.txtFirstName.place(x=50, y=140, width=250, height=30)

        lastName_lbl = Label(self.root, text="Last Name:", font=("times new roman", 28, "bold"),
                             bg="white", fg="black")
        lastName_lbl.place(x=730, y=220, width=210, height=30)

        self.txtLastName = ttk.Entry(frame, textvariable=self.var_lname, font=("times new romain", 15, "bold"))
        self.txtLastName.place(x=400, y=140, width=250, height=30)

        contactNo_lbl = Label(self.root, text="Contact No:", font=("times new roman", 28, "bold"),
                              bg="white", fg="black")
        contactNo_lbl.place(x=390, y=310, width=210, height=30)

        self.txtContactNo = ttk.Entry(frame, textvariable=self.var_cNo, font=("times new romain", 15, "bold"))
        self.txtContactNo.place(x=50, y=230, width=250, height=30)

        Email_lbl = Label(self.root, text="Email:", font=("times new roman", 28, "bold"),
                          bg="white", fg="black")
        Email_lbl.place(x=700, y=310, width=210, height=30)

        self.txtEmail = ttk.Entry(frame, textvariable=self.var_email, font=("times new romain", 15, "bold"))
        self.txtEmail.place(x=400, y=230, width=250, height=30)

        SecurityQ_lbl = Label(self.root, text="Security Question:", font=("times new roman", 25, "bold"),
                              bg="white", fg="black")
        SecurityQ_lbl.place(x=400, y=400, width=260, height=30)

        self.SecurityQ_combo = ttk.Combobox(frame, textvariable=self.var_SecurityQ,
                                            font=("times new romain", 15, "bold"), width=250, state="readonly")
        self.SecurityQ_combo["values"] = (
            "Select Favourite Things ", "Favourite Food", "Favourite Subject", "Favourite Sports", "Favourite Location")
        self.SecurityQ_combo.current(0)
        self.SecurityQ_combo.place(x=50, y=320, width=250, height=30)

        SecurityA_lbl = Label(self.root, text="Security Answer:", font=("times new roman", 25, "bold"),
                              bg="white", fg="black")
        SecurityA_lbl.place(x=740, y=400, width=260, height=30)

        self.txtSecurityA = ttk.Entry(frame, textvariable=self.var_SecurityA, font=("times new romain", 15, "bold"))
        self.txtSecurityA.place(x=400, y=320, width=250, height=30)

        Pass_lbl = Label(self.root, text="Password:", font=("times new roman", 25, "bold"),
                         bg="white", fg="black")
        Pass_lbl.place(x=400, y=490, width=150, height=30)

        self.txtPass = ttk.Entry(frame, textvariable=self.var_pass, font=("times new romain", 15, "bold"), show="*")
        self.txtPass.place(x=50, y=410, width=250, height=30)

        Cpass_lbl = Label(self.root, text="Confirm Password:", font=("times new roman", 25, "bold"),
                          bg="white", fg="black")
        Cpass_lbl.place(x=740, y=490, width=270, height=30)

        self.txtCpass = ttk.Entry(frame, textvariable=self.var_Cpass, font=("times new romain", 15, "bold"), show="*")
        self.txtCpass.place(x=400, y=410, width=250, height=30)

        checkbtn = Checkbutton(frame, text="I Agree The Terms And Conditions", font=("times new romain", 15, "bold"),
                               onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=450)

        # Register button
        register_btn = Button(frame, text="Register", command=self.register, font=("times new roman", 20, "bold"),
                              bg="red", fg="white", activeforeground="white", activebackground="red")
        register_btn.place(x=250, y=490, width=200, height=40)

    def register(self):
        # Check if any field is empty
        if (self.var_fname.get() == "" or self.var_lname.get() == "" or
                self.var_cNo.get() == "" or self.var_email.get() == "" or
                self.var_SecurityQ.get() == "Select Favourite Things " or self.var_SecurityA.get() == "" or
                self.var_pass.get() == "" or self.var_Cpass.get() == ""):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)

        # Check if password and confirm password are not the same
        elif self.var_pass.get() != self.var_Cpass.get():
            messagebox.showerror("Error", "Password and Confirm Password must be the same", parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(host="localhost", port=3306, user="newuser", password="Sachin@9165",
                                               database="face_recognizer", auth_plugin="mysql_native_password")

                my_cursor = conn.cursor()

                query = ("select * from register where email=%s")
                value = (self.var_email.get(),)  # This should be a tuple
                my_cursor.execute(query, value)

                row = my_cursor.fetchone()

                if row is not None:
                    messagebox.showerror("Error", "User already exists, please try another email", parent=self.root)
                else:
                    my_cursor.execute("insert into register (fname, lname, cNo, email, SecurityQ, SecurityA, pass) values (%s, %s, %s, %s, %s, %s, %s)", (
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_cNo.get(),
                        self.var_email.get(),
                        self.var_SecurityQ.get(),
                        self.var_SecurityA.get(),
                        self.var_pass.get()
                    ))

                    conn.commit()
                    conn.close()

                    messagebox.showinfo("Success", "Registered Successfully", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()
