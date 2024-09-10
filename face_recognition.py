from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
from datetime import datetime
import cv2

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("AI Based Face Attendance System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white",
                          fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1400, height=45)

        img_left = Image.open(r"C:\Users\LENOVO\Desktop\Face recognition system\image23.jpg")
        img_left = img_left.resize((680, 660), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_1b1 = Label(self.root, image=self.photoimg_left)
        f_1b1.place(x=0, y=45, width=680, height=660)

        img_right = Image.open(r"C:\Users\LENOVO\Desktop\Face recognition system\image24.jpg")
        img_right = img_right.resize((680, 660), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_1b1 = Label(self.root, image=self.photoimg_right)
        f_1b1.place(x=680, y=45, width=680, height=660)

        # button frame
        btn_frame = Button(self.root, text="Face Recognition", cursor="hand2", command=self.face_recog,
                           font=("times new roman", 30, "bold"), bd=2, bg="darkgreen", fg="white", relief=RIDGE)
        btn_frame.place(x=830, y=610, width=380, height=60)

    def mark_attendance(self, i, d, r, n):
        with open("attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []

            for line in myDataList:
                entry = line.split(",")
                name_list.append(entry[0])

            # Check if the student ID is already in the list, if not, add it
            if i not in name_list:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    # =============== face recognition ====================
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbours, color, txt, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbours)

            coord = []
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int(100 * (1 - predict / 300))

                conn = mysql.connector.connect(host="localhost", port=3306, user="newuser", password="Sachin@9165",
                                               database="face_recognizer", auth_plugin="mysql_native_password")
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT name FROM student WHERE StudentID=" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n) if n else "Unknown"

                my_cursor.execute("SELECT rollno FROM student WHERE StudentID=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r) if r else "Unknown"

                my_cursor.execute("SELECT Department FROM student WHERE StudentID=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d) if d else "Unknown"

                my_cursor.execute("SELECT StudentID FROM student WHERE StudentID=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i) if i else "Unknown"

                if confidence > 77:
                    cv2.putText(img, f"Department: {d}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"ID: {i}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll No: {r}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {n}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i, d, r, n)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)  # Red rectangle for unknown face
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "face", clf)
            return img

        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press Enter to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
