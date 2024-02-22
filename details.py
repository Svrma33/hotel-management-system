from tkinter import*
from PIL import Image, ImageTk, ImageFilter
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class DetailsRoom:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1280x550+238+218")

         # ====================TITLE====================
        lbl_title = Label(self.root, text="ROOM BOOKING DETAILS", font=("Dutch801 XBd BT",30,"bold"), bg="black", fg="gold")
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # ====================LABEL FRAME===================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("times new roman",15,"bold"),padx=2)
        labelframeleft.place(x=10,y=50,width=540,height=350)

        # ====================LABEL AND ENTRIES===================
        #Floor
        lbl_floor=Label(labelframeleft,text="Floor:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W,padx=20)

        self.var_floor=StringVar()
        entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,font=("arial",12,"bold"),width=20)
        entry_floor.grid(row=0,column=1,sticky=W)

        #Room No
        lbl_RoomNo=Label(labelframeleft,text="Room Number:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W,padx=20)

        self.var_RoomNo=StringVar()
        entry_RoomNo=ttk.Entry(labelframeleft,textvariable=self.var_RoomNo,font=("arial",12,"bold"),width=20)
        entry_RoomNo.grid(row=1,column=1,sticky=W)

        #Room Type
        lbl_RoomType=Label(labelframeleft,text="Room Type:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W,padx=20)

        self.var_RoomType=StringVar()        
        self.entry_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_RoomType,font=("arial",12,"bold"),state="readonly")
        self.entry_RoomType["values"]=("Select","Single","Double","Luxury")
        self.entry_RoomType.place(x=166,y=76,width=185)
        self.entry_RoomType.current(0)

        # ====================BUTTONS====================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=55,y=250,width=412,height=36)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnAdd=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=1,padx=1)

        btnAdd=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=2,padx=1)

        btnAdd=Button(btn_frame,text="Reset",command=self.reset_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=3,padx=1)

        # ====================TABLE FRAME====================
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Details",font=("times new roman",15,"bold"),padx=2)
        Table_Frame.place(x=600,y=50,width=600,height=350)

        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)

        self.room_table=ttk.Treeview(Table_Frame,column=("floor","roomno","roomtype"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomno",text="Room No")
        self.room_table.heading("roomtype",text="Room Type")

        self.room_table["show"]="headings"
        
        self.room_table.column("floor",width=100)
        self.room_table.column("roomno",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.pack(fill=BOTH,expand=1)

        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    #add data
    def add_data(self):
        if self.var_floor.get()=="" or self.var_RoomType.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="127.0.0.1",user="root",password="124421",database="hotel")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                                    self.var_floor.get(),
                                                                                    self.var_RoomNo.get(),
                                                                                    self.var_RoomType.get()
                                                                                    
                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","New room has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="127.0.0.1",user="root",password="124421",database="hotel")
        my_cursor=conn.cursor()
        my_cursor.execute("select *from details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #get cursor
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_floor.set(row[0])
        self.var_RoomNo.set(row[1])
        self.var_RoomType.set(row[2])
        
    #update function
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please enter Floor number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="127.0.0.1",user="root",password="124421",database="hotel")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set Floor=%s,RoomType=%s where RoomNo=%s",(
                                                                                    self.var_floor.get(),
                                                                                    self.var_RoomType.get(),
                                                                                    self.var_RoomNo.get()
                                                                                ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","New Room details has been updated successfully",parent=self.root)
        
    #delete function
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this room detail",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="127.0.0.1",user="root",password="124421",database="hotel")
            my_cursor=conn.cursor()
            query="delete from details where RoomNo=%s"
            value=(self.var_RoomNo.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset_data(self):
        self.var_floor.set(""),
        self.var_RoomNo.set(""),
        self.var_RoomType.set("")





if __name__ =="__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()