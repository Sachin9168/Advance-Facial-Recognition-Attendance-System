from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("AI Based Face Attendance System")

        title_lbl = Label(self.root, text="TRAIN DATASET", font=("times new roman", 35, "bold"), bg="white",
                          fg="RED")
        title_lbl.place(x=0, y=0, width=1400, height=45)

        img_top = Image.open(r"C:\Users\LENOVO\Desktop\Face recognition system\image22.jpg")
        img_top = img_top.resize((440, 300), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_1b1 = Label(self.root, image=self.photoimg_top)
        f_1b1.place(x=0, y=45, width=440, height=300)

        img_top1 = Image.open(r"C:\Users\LENOVO\Desktop\Face recognition system\image20.jpeg")
        img_top1 = img_top1.resize((480, 300), Image.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_1b1 = Label(self.root, image=self.photoimg_top1)
        f_1b1.place(x=440, y=45, width=480, height=300)

        img_top2 = Image.open(r"C:\Users\LENOVO\Desktop\Face recognition system\image21.webp")
        img_top2 = img_top2.resize((440, 300), Image.LANCZOS)
        self.photoimg_top2 = ImageTk.PhotoImage(img_top2)

        f_1b1 = Label(self.root, image=self.photoimg_top2)
        f_1b1.place(x=920, y=45, width=440, height=300)


         # button frame

        btn_frame = Button(self.root, text="TRAIN DATA",cursor="hand2",command=self.train_classifier, font=("times new romain",30,"bold"),bd=2,bg="red", relief=RIDGE)
        btn_frame.place(x=0, y=343, width=1365, height=60)



        img_bottom = Image.open(r"C:\Users\LENOVO\Desktop\Face recognition system\image11.webp")
        img_bottom = img_bottom.resize((1365, 300), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_1b1 = Label(self.root, image=self.photoimg_bottom)
        f_1b1.place(x=0, y=405, width=1365, height=300)


    def train_classifier(self):
        save_path = r"C:\Users\LENOVO\Desktop\Face recognition system\data"
        data_dir=(save_path)
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # convert grey scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13

        ids = np.array(ids)

        #==================Train the classifier and save=================

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
