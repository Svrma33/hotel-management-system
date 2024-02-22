from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk, ImageFilter
from tkinter import messagebox
import mysql.connector
from customer import Cust_Win
from room import Roombooking
from details import DetailsRoom

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN")
        self.root.geometry("1230x750+130+18")
        self.root.resizable(False,False)

        img1 = Image.open("C:/Users/SIDDHARTH/Documents/project/Hotel Management System/hotel_img.png")
        img1 = img1.resize((1230,750), Image.LANCZOS)
        img1_blur = img1.filter(ImageFilter.GaussianBlur)
        self.photoimg1 = ImageTk.PhotoImage(img1_blur)

        lbl_bg= Label(self.root, image=self.photoimg1)
        lbl_bg.place(x=0, y=0, width=1230, height=750)

        frame=Frame(self.root,bg="black")
        frame.place(x=450,y=155,width=340,height=450)

        img2=Image.open("C:/Users/SIDDHARTH\Documents/project/Hotel Management System/Login.png")
        img2=img2.resize((70,70),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black")
        lblimg2.place(x=570,y=160,width=100,height=100)

        login_str=Label(frame,text="LOGIN",font=("Dutch801 XBd BT",25,"bold"),fg="white",bg="black")
        login_str.place(x=109,y=95)

        #label
        Email=Label(frame,text="Email",font=("Times New Roman",15,"bold"),fg="white",bg="black")
        Email.place(x=67,y=153)

        self.txtemail=ttk.Entry(frame,font=("Times New Roman",15))
        self.txtemail.place(x=40,y=185,width=270)

        Password=Label(frame,text="Password",font=("Times New Roman",15,"bold"),fg="white",bg="black")
        Password.place(x=67,y=225)

        self.txtpass=ttk.Entry(frame,font=("Times New Roman",15))
        self.txtpass.place(x=40,y=255,width=270)

        #icon images
        img3=Image.open("C:/Users/SIDDHARTH\Documents/project/Hotel Management System/Email.png")
        img3=img3.resize((30,30),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black")
        lblimg3.place(x=485,y=305,width=30,height=30)

        img4=Image.open("C:/Users/SIDDHARTH\Documents/project/Hotel Management System/Password.png")
        img4=img4.resize((35,25),Image.LANCZOS)
        self.photoimage4=ImageTk.PhotoImage(img4)
        lblimg4=Label(image=self.photoimage4,bg="black")
        lblimg4.place(x=485,y=380,width=35,height=25)

        #LoginButton
        loginbtn=Button(frame,text="Login",command=self.login,font=("Times New Roman",14,"bold"),cursor="hand2",bd=3,relief=RIDGE,fg="black",bg="white",activeforeground="black",activebackground="white")
        loginbtn.place(x=110,y=300,width=110,height=35)

        #RegisterButton
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("Times New Roman",11),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=10,y=360,width=160)

        #ForgetpassButton
        loginbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("Times New Roman",11),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        loginbtn.place(x=2,y=395,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtemail.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields required")
        elif self.txtemail.get()=="siddharth" and self.txtpass.get()=="verma":
            messagebox.showinfo("Success","Welcome")
        else:
            conn=mysql.connector.connect(host="127.0.0.1",user="root",password="124421",database="login")
            my_cursor=conn.cursor()
            my_cursor.execute("select *from registernow where email=%s and password=%s",(
                self.txtemail.get(),
                self.txtpass.get()
            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Email & Password")
            else:
                open_main=messagebox.askyesno("Access","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    #====================================reset password====================================
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="127.0.0.1",user="root",password="124421",database="login")
            my_cursor=conn.cursor()
            query=("select *from registernow where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtemail.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct answer",parent=self.root2)
            else:
                query=("update registernow set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtemail.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset",parent=self.root2)
                self.root2.destroy()



    #====================================forget password window====================================        
    
    def forgot_password_window(self):
        if self.txtemail.get()=="":
            messagebox.showerror("Error","Please enter Email Address to reset password")
        else:
            conn=mysql.connector.connect(host="127.0.0.1",user="root",password="124421",database="login")
            my_cursor=conn.cursor()
            query=("select *from registernow where email=%s")
            value=(self.txtemail.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("My Error","Please enter the valid email")
            else:                
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+580+190")
                self.root2.resizable(False,False)

                l=Label(self.root2,text="Forget Password",font=("Times New Roman",20,"bold"),fg="Red")
                l.place(x=0,y=10,width=340)

                security_Q=Label(self.root2,text="Select Security Questions",font=("Times new roman",15,"bold"))
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",12),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Nick Name","Your Pet's Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)
                
                security_A=Label(self.root2,text="Security Answer",font=("Times new roman",15,"bold"))
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("Times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("Times new roman",15,"bold"))
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("Times new roman",15))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("Times new roman",15,"bold"),cursor="hand2",fg="white",bg="black",activeforeground="white",activebackground="black")
                btn.place(x=132,y=290)


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1230x750+130+18")
        self.root.resizable(False,False)

        # ==================variables====================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=IntVar()
        

        #====================background image====================
        img1 = Image.open("C:/Users/SIDDHARTH/Documents/project/Hotel Management System/hotel_img.png")
        img1 = img1.resize((1230,750), Image.LANCZOS)
        img1_blur = img1.filter(ImageFilter.GaussianBlur)
        self.photoimg1 = ImageTk.PhotoImage(img1_blur)

        lbl_bg= Label(self.root, image=self.photoimg1)
        lbl_bg.place(x=0, y=0, width=1230, height=750)

        #====================main frame====================
        frame=Frame(self.root,bg="white")
        frame.place(x=215,y=102,width=800,height=550)

        register_lbl=Label(frame,text="New User Register",font=("Times new roman",20,"bold"),fg="Red",bg="white")
        register_lbl.place(x=285,y=20)

        #====================label and entry====================
        #row-1
        fname=Label(frame,text="First Name",font=("Times new roman",15,"bold"),bg="white")
        fname.place(x=100,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("Times new roman",15))
        fname_entry.place(x=100,y=130,width=250)
        
        lname=Label(frame,text="Last Name",font=("Times new roman",15,"bold"),bg="white")
        lname.place(x=450,y=100)

        lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("Times new roman",15))
        lname_entry.place(x=450,y=130,width=250)

        #row-2
        contact=Label(frame,text="Contact Number",font=("Times new roman",15,"bold"),bg="white")
        contact.place(x=100,y=170)

        contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("Times new roman",12))
        contact_entry.place(x=100,y=200,width=250)
        
        email=Label(frame,text="Email",font=("Times new roman",15,"bold"),bg="white")
        email.place(x=450,y=170)

        email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("Times new roman",12))
        email_entry.place(x=450,y=200,width=250)

        #row-3
        security_Q=Label(frame,text="Select Security Questions",font=("Times new roman",15,"bold"),bg="white")
        security_Q.place(x=100,y=250)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",12),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Nick Name","Your Pet's Name")
        self.combo_security_Q.place(x=100,y=280,width=250)
        self.combo_security_Q.current(0)
        
        security_A=Label(frame,text="Security Answer",font=("Times new roman",15,"bold"),bg="white")
        security_A.place(x=450,y=250)

        security_A_entry=ttk.Entry(frame,textvariable=self.var_securityA,font=("Times new roman",15))
        security_A_entry.place(x=450,y=280,width=250)

        #row-4
        pswd=Label(frame,text="Password",font=("Times new roman",15,"bold"),bg="white")
        pswd.place(x=100,y=320)

        pswd_entry=ttk.Entry(frame,textvariable=self.var_pass,font=("Times new roman",15))
        pswd_entry.place(x=100,y=350,width=250)
        
        cpswd=Label(frame,text="Confirm Password",font=("Times new roman",15,"bold"),bg="white")
        cpswd.place(x=450,y=320)

        cpswd_entry=ttk.Entry(frame,textvariable=self.var_confpass,font=("Times new roman",15))
        cpswd_entry.place(x=450,y=350,width=250)

        # ==================checkbutton====================
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("Times new roman",12),onvalue=1,offvalue=0)
        checkbtn.place(x=100,y=390)

        # ==================button====================
        img=Image.open("C:/Users/SIDDHARTH/Documents/project/Hotel Management System/register now.png")
        img=img.resize((150,50),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=150,y=440,width=150)

        img0=Image.open("C:/Users/SIDDHARTH/Documents/project/Hotel Management System/login now.png")
        img0=img0.resize((150,50),Image.LANCZOS)
        self.photoimage0=ImageTk.PhotoImage(img0)
        b1=Button(frame,image=self.photoimage0,command=self.return_login,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=480,y=440,width=150)

        # ==================Function declaration====================
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms & condition")
        else:
            conn=mysql.connector.connect(host="127.0.0.1",user="root",password="124421",database="login")
            my_cursor=conn.cursor()
            query=("select *from registernow where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User aleady exist,please try another email")
            else:
                my_cursor.execute("insert into registernow values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                    self.var_fname.get(),
                                                                    self.var_lname.get(),
                                                                    self.var_contact.get(),
                                                                    self.var_email.get(),
                                                                    self.var_securityQ.get(),
                                                                    self.var_securityA.get(),
                                                                    self.var_pass.get()
                                                                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")

    def return_login(self):
        self.root.destroy()

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

if __name__ =="__main__":
    main()