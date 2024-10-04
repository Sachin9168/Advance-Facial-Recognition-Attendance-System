import tkinter.messagebox
from tkinter import *
from PIL import Image, ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
import os
from time import strftime
import tkinter
from helpdesk import Help
from developer import Developer
from attendence import  Attendence

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Advance Facial Recognition Attendance System")

        # first image
        img = Image.open(r"C:\Users\LENOVO\Desktop\Face recognition system\image2.jpeg")
        img = img.resize((432,130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_1b1 = Label(self.root, image=self.photoimg)
        f_1b1.place(x=0, y=0, width=432, height=130)

        #second image
        img1 = Image.open(r"C:\Users\LENOVO\Desktop\Face recognition system\image3.webp")
        img1 = img1.resize((432, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_1b1 = Label(self.root, image=self.photoimg1)
        f_1b1.place(x=432, y=0, width=432, height=130)

        #third image

        img2 = Image.open(r"C:\Users\LENOVO\Desktop\Face recognition system\image4.jpg")
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


        title_lbl=Label(bg_img,text="ADVANCE FACIAL RECOGNITION ATTENDANCE SYSTEM", font=("times new roman",28,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1185,height=45)


        #=================== time====================

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        # Time display label
        lbl = Label(bg_img, font=("times new roman", 20, "bold"), bg="white", fg="brown")
        lbl.place(x=1185, y=0, width=185, height=45)  # Adjust the position and size as needed
        time()
      

        #student button
        img4 = Image.open(r"C:\Users\LENOVO\Desktop\Face recognition system\image6.jpeg")
        img4 = img4.resize((180, 180), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1= Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=90,width=180,height=180)

        b1_1= Button(bg_img, text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",20,"bold"),bg="blue",fg="white")
        b1_1.place(x=100,y=260,width=180,height=40)


        #detect face button
        img5 = Image.open(r"C:\Users\LENOVO\Desktop\Face recognition system\image7.jpeg")
        img5 = img5.resize((180, 180), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1= Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=400,y=90,width=180,height=180)

        b1_1= Button(bg_img, text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",20,"bold"),bg="blue",fg="white")
        b1_1.place(x=400,y=260,width=180,height=40)


        # Attendance face button
        img6 = Image.open(r"C:\Users\LENOVO\Desktop\Face recognition system\image8.jpg")
        img6 = img6.resize((180, 180), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2",command=self.students_attendance)
        b1.place(x=730, y=90, width=180, height=180)

        b1_1 = Button(bg_img, text="Attendance", cursor="hand2", command=self.students_attendance,font=("times new roman", 20, "bold"), bg="blue",
                      fg="white")
        b1_1.place(x=730, y=260, width=180, height=40)


        # help button
        img7 = Image.open(r"C:\Users\LENOVO\Desktop\Face recognition system\image9.jpg")
        img7 = img7.resize((180, 180), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2",command=self.help_desk)
        b1.place(x=1060, y=90, width=180, height=180)

        b1_1 = Button(bg_img, text="Help Desk", cursor="hand2",command=self.help_desk, font=("times new roman", 20, "bold"), bg="blue",
                      fg="white")
        b1_1.place(x=1060, y=260, width=180, height=40)


        # train face button
        img8 = Image.open(r"C:\Users\LENOVO\Desktop\Face recognition system\image10.jpeg")
        img8 = img8.resize((180, 180), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.train_data)
        b1.place(x=100, y=340, width=180, height=180)

        b1_1 = Button(bg_img, text="Train Data", cursor="hand2",command=self.train_data, font=("times new roman", 20, "bold"), bg="blue",
                      fg="white")
        b1_1.place(x=100, y=510, width=180, height=40)


        # photos button
        img9 = Image.open(r"C:\Users\LENOVO\Desktop\Face recognition system\image11.webp")
        img9 = img9.resize((180, 180), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9,command=self.open_img ,cursor="hand2")
        b1.place(x=400, y=340, width=180, height=180)

        b1_1 = Button(bg_img, text="Photos",command=self.open_img, cursor="hand2", font=("times new roman", 20, "bold"), bg="blue",
                      fg="white")
        b1_1.place(x=400, y=510, width=180, height=40)

        # developer button
        img10 = Image.open(r"C:\Users\LENOVO\Desktop\Face recognition system\image14.jpeg")
        img10 = img10.resize((180, 180), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10, cursor="hand2",command=self.sachin)
        b1.place(x=730, y=340, width=180, height=180)

        b1_1 = Button(bg_img, text="Developer", cursor="hand2",command=self.sachin, font=("times new roman", 20, "bold"), bg="blue",
                      fg="white")
        b1_1.place(x=730, y=510, width=180, height=40)

         # Exit button
        img11 = Image.open(r"C:\Users\LENOVO\Desktop\Face recognition system\image13.jpeg")
        img11 = img11.resize((180, 180), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11, cursor="hand2",command=self.iExit)
        b1.place(x=1060, y=340, width=180, height=180)

        b1_1 = Button(bg_img, text="Exit", cursor="hand2", command=self.iExit,font=("times new roman", 20, "bold"), bg="blue",
                      fg="white")
        b1_1.place(x=1060, y=510, width=180, height=40)


        #-------------------Function button-------------------------------------------

    def student_details(self):
            self.new_window=Toplevel(self.root)
            self.app=Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def open_img(self):
        save_path = r"C:\Users\LENOVO\Desktop\Face recognition system\data"
        os.startfile(save_path)

    def help_desk(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)

    def sachin(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def students_attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendence(self.new_window)

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit AI Based Face Attendence System?",parent=self.root)

        if self.iExit>0:
            self.root.destroy()
        else:
            return


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()



