from tkinter import *
from PIL import Image, ImageTk, ImageFilter
from customer import Cust_Win
from room import Roombooking
from details import DetailsRoom


class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")
        self.root.state("zoomed")
     
        # ====================TITLE====================
        lbl_title = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=("Dutch801 XBd BT",30,"bold"), bg="white", fg="black")
        lbl_title.place(x=0, y=0, width=1550, height=35)

        # ====================LOGO====================
        img2 = Image.open("C:/Users/SIDDHARTH/Documents/project/Hotel Management System/logo.png")
        img2 = img2.resize((1536, 150), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2)
        lblimg.place(x=0, y=35, width=1536, height=150)
       
        # ====================MAIN FRAME====================
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=185, width=1536, height=609)

        #====================MAIN FRAME IMAGE====================
        img1 = Image.open("C:/Users/SIDDHARTH/Documents/project/Hotel Management System/hotel_img.png")
        img1 = img1.resize((1529, 602), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg_main = Label(main_frame, image=self.photoimg1)
        lblimg_main.place(x=0, y=0, width=1529, height=602)

        # ====================MENU====================
        lbl_menu = Label(main_frame, text="MENU", font=("TIMES NEW ROMAN",25,"bold"), bg="black", fg="gold")
        lbl_menu.place(x=1, y=1, width=235)

        # ====================BUTTON FRAME====================
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=38, width=237, height=173)

        cust_btn = Button(btn_frame, text="CUSTOMER", command=self.cust_details, width=22, font=("TIMES NEW ROMAN",13,"bold"), bg="black", fg="white", cursor="hand2")
        cust_btn.grid(row=0, column=0)

        room_btn = Button(btn_frame, text="ROOM",command=self.roombooking, width=22, font=("TIMES NEW ROMAN",13,"bold"), bg="black", fg="white", cursor="hand2")
        room_btn.grid(row=1, column=0)

        details_btn = Button(btn_frame, text="DETAILS",command=self.details_room, width=22, font=("TIMES NEW ROMAN",13,"bold"), bg="black", fg="white", cursor="hand2")
        details_btn.grid(row=2, column=0)

        report_btn = Button(btn_frame, text="REPORT", width=22, font=("TIMES NEW ROMAN",13,"bold"), bg="black", fg="white", cursor="hand2")
        report_btn.grid(row=3, column=0)

        logout_btn = Button(btn_frame, text="LOGOUT",command=self.logout, width=22, font=("TIMES NEW ROMAN",13,"bold"), bg="black", fg="white", cursor="hand2")
        logout_btn.grid(row=4, column=0)

    
    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)

    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)

    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)

    def logout(self):
        self.root.destroy()





if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
