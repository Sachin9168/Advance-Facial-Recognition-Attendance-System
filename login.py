from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from registration import Register
import mysql.connector
from main import Face_Recognition_System

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("AI Based Face Attendance System")

        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_security_Q = StringVar()
        self.var_security_A = StringVar()
        self.var_newpass = StringVar()

        # First image
        img = Image.open(r"C:\Users\LENOVO\Desktop\Face recognition system\image33.jpg")
        img = img.resize((1370, 760), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_1b1 = Label(self.root, image=self.photoimg)
        f_1b1.place(x=0, y=0, width=1370, height=760)

        frame = Frame(self.root, bg="black")
        frame.place(x=490, y=140, width=390, height=510)

        img_logo = Image.open(r"C:\Users\LENOVO\Desktop\Face recognition system\image35.png")
        img_logo = img_logo.resize((100, 100), Image.LANCZOS)
        self.photoimg_logo = ImageTk.PhotoImage(img_logo)

        f_1b2 = Label(self.root, image=self.photoimg_logo)
        f_1b2.place(x=630, y=150, width=100, height=100)

        title_lbl = Label(self.root, text="AI BASED FACE ATTENDANCE SYSTEM", font=("times new roman", 15, "bold"),
                          bg="black", fg="white")
        title_lbl.place(x=490, y=260, width=390, height=30)

        # Username
        img_user = Image.open(r"C:\Users\LENOVO\Desktop\Face recognition system\image35.png")
        img_user = img_user.resize((40, 40), Image.LANCZOS)
        self.photoimg_user = ImageTk.PhotoImage(img_user)

        f_1b2 = Label(self.root, image=self.photoimg_user)
        f_1b2.place(x=530, y=320, width=30, height=30)

        user_lbl = Label(self.root, text="Username", font=("times new roman", 23, "bold"), bg="black", fg="white")
        user_lbl.place(x=560, y=320, width=150, height=30)

        self.txtuser = ttk.Entry(frame, font=("times new romain", 15, "bold"))
        self.txtuser.place(x=40, y=220, width=300, height=30)

        img_pass = Image.open(r"C:\Users\LENOVO\Desktop\Face recognition system\image37.png")
        img_pass = img_pass.resize((40, 40), Image.LANCZOS)
        self.photoimg_pass = ImageTk.PhotoImage(img_pass)

        f_1b2 = Label(self.root, image=self.photoimg_pass)
        f_1b2.place(x=530, y=410, width=30, height=30)

        pass_lbl = Label(self.root, text="Password", font=("times new roman", 23, "bold"), bg="black", fg="white")
        pass_lbl.place(x=560, y=410, width=150, height=30)

        self.txtpass = ttk.Entry(frame, font=("times new romain", 15, "bold"))
        self.txtpass.place(x=40, y=310, width=300, height=30)

        # Login button
        login_btn = Button(frame, text="Login", command=self.login, font=("times new roman", 23, "bold"), bg="red",
                           fg="white", activeforeground="white", activebackground="red")
        login_btn.place(x=110, y=355, width=150, height=40)

        registration_btn = Button(frame, text="New User Registration", command=self.register_window,
                                  font=("times new roman", 15, "bold"), bg="black", fg="white",
                                  activeforeground="white", activebackground="black")
        registration_btn.place(x=10, y=425, width=200, height=30)

        forgetpass_btn = Button(frame, text="Forget Password", command=self.check_email_before_reset,
                                font=("times new roman", 15, "bold"), bg="black", fg="white",
                                activeforeground="white", activebackground="black")
        forgetpass_btn.place(x=10, y=460, width=150, height=30)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")

        elif self.txtuser.get() == "sachin" and self.txtpass.get() == "123456":
            messagebox.showinfo("success", "Login Successfully")

        else:
            conn = mysql.connector.connect(host="localhost", port=3306, user="newuser", password="Sachin@9165",
                                           database="face_recognizer", auth_plugin="mysql_native_password")

            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and pass=%s", (
                self.txtuser.get(),
                self.txtpass.get()
            ))

            row = my_cursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid user name and password")
            else:
                open_main = messagebox.askyesno("YesNo", "Access Only Admin")
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = Face_Recognition_System(self.new_window)

    def check_email_before_reset(self):
        email = self.txtuser.get()
        if email == "":
            messagebox.showerror("Error", "Please enter your email first")
            return

        if not self.email_exists_in_db(email):
            messagebox.showerror("Error", "Email not found")
            return

        #  email exists, open the reset password window
        self.reset_password_window()

    def email_exists_in_db(self, email):
        conn = mysql.connector.connect(host="localhost", port=3306, user="newuser", password="Sachin@9165",
                                       database="face_recognizer", auth_plugin="mysql_native_password")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM register WHERE email=%s", (email,))
        row = my_cursor.fetchone()
        conn.close()
        return row is not None

    def reset_password_window(self):
        self.root2 = Toplevel(self.root)
        self.root2.title("Reset Password")
        self.root2.geometry("400x400")

        security_Q_lbl = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"))
        security_Q_lbl.pack(pady=10)
        self.combo_securiy_Q = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_securiy_Q["values"] = ("Select" "Favourite Food", "Favourite Subject", "Favourite Sports", "Favourite Location")
        self.combo_securiy_Q.current(0)
        self.combo_securiy_Q.pack(pady=10)

        security_A_lbl = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"))
        security_A_lbl.pack(pady=10)
        self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
        self.txt_security.pack(pady=10)

        new_pass_lbl = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"))
        new_pass_lbl.pack(pady=10)
        self.txt_newpass = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
        self.txt_newpass.pack(pady=10)

        reset_btn = Button(self.root2, text="Reset Password", command=self.reset_pass, font=("times new roman", 15, "bold"), bg="green", fg="white")
        reset_btn.pack(pady=20)

    def reset_pass(self):
        if self.combo_securiy_Q.get() == "Select ":
            messagebox.showerror("Error", "Select a security question", parent=self.root2)
        elif self.txt_security.get() == "":
            messagebox.showerror("Error", "Please enter the answer", parent=self.root2)
        elif self.txt_newpass.get() == "":
            messagebox.showerror("Error", "Please enter the new password", parent=self.root2)
        else:
            email = self.txtuser.get()
            conn = mysql.connector.connect(host="localhost", port=3306, user="newuser", password="Sachin@9165",
                                           database="face_recognizer", auth_plugin="mysql_native_password")

            my_cursor = conn.cursor()
            query = "SELECT * FROM register WHERE email=%s AND SecurityQ=%s AND SecurityA=%s"
            value = (email, self.combo_securiy_Q.get(), self.txt_security.get())
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row is None:
                messagebox.showerror("Error", "Please enter the correct answer", parent=self.root2)
            else:
                query = "UPDATE register SET password=%s WHERE email=%s"
                value = (self.txt_newpass.get(), email)
                my_cursor.execute(query, value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Info", "Your password has been reset. Please log in with the new password.",
                                    parent=self.root2)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()

