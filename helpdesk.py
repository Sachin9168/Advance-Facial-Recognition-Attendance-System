from tkinter import *
from PIL import Image, ImageTk

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("AI Based Face Attendance System")

        title_lbl = Label(self.root, text="HELP DESK", font=("times new roman", 35, "bold"), bg="blue",
                          fg="white")
        title_lbl.place(x=0, y=0, width=1400, height=45)

        img_left = Image.open(r"C:\Users\LENOVO\Desktop\Face recognition system\image25.jpg")
        img_left = img_left.resize((1400, 660), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_1b1 = Label(self.root, image=self.photoimg_left)
        f_1b1.place(x=-50, y=45, width=1400, height=660)

        sachin_lbl = Label(self.root, text="Email: Sachinchouhanrajput9165@gmail.com", font=("times new roman", 16, "bold"), bg="red",
                          fg="white")
        sachin_lbl.place(x=433, y=205, width=430, height=45)


if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
