from tkinter import *
from PIL import Image, ImageTk

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("AI Based Face Attendance System")

        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"), bg="green",
                          fg="white")
        title_lbl.place(x=0, y=0, width=1400, height=45)

        img_left = Image.open(r"C:\Users\LENOVO\Desktop\Face recognition system\image27.webp")
        img_left = img_left.resize((1400, 660), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_1b1 = Label(self.root, image=self.photoimg_left)
        f_1b1.place(x=0, y=45, width=1400, height=660)

        sachin_lbl = Label(self.root, text="Hello I am Sachin Chouhan, I am Software Developer", font=("times new roman", 20, "bold"), bg="yellow",
                          fg="black")
        sachin_lbl.place(x=0, y=45, width=1400, height=45)





if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
