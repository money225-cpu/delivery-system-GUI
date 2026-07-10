from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class informationClass:
    def __init__(self,root):
        self.root = root
        self.root.title("ລະບົບຈັດການຂໍ້ມູນພັດສະດຸ (Delivery Management system)")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        
        #===title====
        title=Label(self.root,text="ຈັດການລາຍລະອຽດຂໍ້ມູນຂອງພັດສະດຸ",font=("Phetsarath OT",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,width=1180,height=35)
        
        #====Variables (ปรับชื่อให้สื่อความหมาย)===
        self.var_tracking_id=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_contact=StringVar()
        self.var_type=StringVar() # ไว้เก็บประเภทสินค้า (banana, shoe, fan)
        self.var_a_date=StringVar()
        self.var_state=StringVar()
        self.var_city=StringVar()
        self.var_pin=StringVar()
        self.var_address=StringVar()

        #====widgets======
        #=====column 1=======
        lbl_tracking_id=Label(self.root,text="ເລກພັດສະດຸ",font=("Phetsarath OT",15,'bold'),bg='white').place(x=10,y=60)
        lbl_Name=Label(self.root,text="ຊື່ລູກຄ້າ",font=("Phetsarath OT",15,'bold'),bg='white').place(x=10,y=100)
        lbl_Email=Label(self.root,text="ອີເມວ",font=("Phetsarath OT",15,'bold'),bg='white').place(x=10,y=140)
        lbl_gender=Label(self.root,text="ເພດ",font=("Phetsarath OT",15,'bold'),bg='white').place(x=10,y=180)
        lbl_state=Label(self.root,text="ແຂວງ",font=("Phetsarath OT",15,'bold'),bg='white').place(x=10,y=220)
        txt_state=Entry(self.root,textvariable=self.var_state,font=("Phetsarath OT",15,'bold'),bg='lightyellow').place(x=150,y=220,width=150)
        lbl_city=Label(self.root,text="ເມືອງ",font=("Phetsarath OT",15,'bold'),bg='white').place(x=310,y=220)
        txt_city=Entry(self.root,textvariable=self.var_city,font=("Phetsarath OT",15,'bold'),bg='lightyellow').place(x=380,y=220,width=100)
        lbl_pin=Label(self.root,text= "ບ້ານ",font=("Phetsarath OT",15,'bold'),bg='white').place(x=490,y=220)
        txt_pin=Entry(self.root,textvariable=self.var_pin,font=("Phetsarath OT",15,'bold'),bg='lightyellow').place(x=620,y=220,width=120)

        #=====Entry Fields=======
        self.txt_tracking_id=Entry(self.root,textvariable=self.var_tracking_id,font=("Phetsarath OT",15,'bold'),bg='lightyellow')
        self.txt_tracking_id.place(x=150,y=60,width=200)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("Phetsarath OT",15,'bold'),bg='lightyellow').place(x=150,y=100,width=200)
        txt_email=Entry(self.root,textvariable=self.var_email,font=("Phetsarath OT",15,'bold'),bg='lightyellow').place(x=150,y=140,width=200)
        self.txt_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("ຊາຍ","ຍິງ","ອື່ນໆ"),font=("Phetsarath OT",15,'bold'),state='readonly',justify=CENTER)
        self.txt_gender.place(x=150,y=180,width=200)
        self.txt_gender.set("ເລືອກເພດ")

        #=====column 2=======
        lbl_dob=Label(self.root,text="ວັນທີ່ີຮັບເຂົ້າລະບົບ",font=("Phetsarath OT",15,'bold'),bg='white').place(x=360,y=60)
        lbl_contact=Label(self.root,text="ເບີໂທຕິດຕໍ່",font=("Phetsarath OT",15,'bold'),bg='white').place(x=360,y=100)
        lbl_admission=Label(self.root,text="ວັນທີຝາກ",font=("Phetsarath OT",15,'bold'),bg='white').place(x=360,y=140)
        lbl_course=Label(self.root,text="ປະເພດສິນຄ້າ",font=("Phetsarath OT",15,'bold'),bg='white').place(x=360,y=180)

        self.course_list=[]
        self.fetch_type() # ดึงข้อมูล banana, shoe, fan มาใส่ตรงนี้
        
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("Phetsarath OT",15,'bold'),bg='lightyellow').place(x=540,y=60,width=200)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("Phetsarath OT",15,'bold'),bg='lightyellow').place(x=540,y=100,width=200)
        txt_admission=Entry(self.root,textvariable=self.var_a_date,font=("Phetsarath OT",15,'bold'),bg='lightyellow').place(x=540,y=140,width=200)
        self.txt_course=ttk.Combobox(self.root,textvariable=self.var_type,values=self.course_list,font=("Phetsarath OT",15,'bold'),state='readonly',justify=CENTER)
        self.txt_course.place(x=540,y=180,width=200)
        self.txt_course.set("ເລືອກປະເພດ")

        #=====Address=======
        lbl_address=Label(self.root,text="ທີ່ຢູ່ໄປສະນີ",font=("Phetsarath OT",15,'bold'),bg='white').place(x=10,y=260)
        self.txt_address=Text(self.root,font=("Phetsarath OT",15,'bold'),bg='lightyellow')
        self.txt_address.place(x=150,y=260,width=590,height=100)

        #====Buttons====
        self.btn_add=Button(self.root,text='ບັນທຶກ',font=("Phetsarath OT",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=150,y=400,width=110,height=40)
        self.btn_update=Button(self.root,text='ແກ້ໄຂ',font=("Phetsarath OT",15,"bold"),bg="#4caf50",fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=270,y=400,width=110,height=40)
        self.btn_delete=Button(self.root,text='ລຶບ',font=("Phetsarath OT",15,"bold"),bg="#f44336",fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390,y=400,width=110,height=40)
        self.btn_clear=Button(self.root,text='ລ້າງຂໍ້ມູນ',font=("Phetsarath OT",15,"bold"),bg="#607d8b",fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510,y=400,width=110,height=40)

        #====Search Panel====
        self.var_search=StringVar()
        lbl_search_tracking_id=Label(self.root,text="ເລກພັດສະດຸ",font=("Phetsarath OT",15,'bold'),bg='white').place(x=770,y=60)
        txt_search_tracking_id=Entry(self.root,textvariable=self.var_search,font=("Phetsarath OT",15,'bold'),bg='lightyellow').place(x=900,y=60,width=180)
        btn_search=Button(self.root,text='ຄົ້ນຫາ',font=("Phetsarath OT",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search).place(x=1090,y=60,width=100,height=30)

        #====Content View (Treeview)====
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=770,y=100,width=420,height=340)

        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        
        # แก้ไข Column ให้ตรงกับ DB
        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("tracking_id","name","email","gender","dob","contact","admission","type","state","city","pin","address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)

        self.CourseTable.heading("tracking_id",text="ID")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("email",text="Email")
        self.CourseTable.heading("gender",text="Gender")
        self.CourseTable.heading("dob",text="DOB")
        self.CourseTable.heading("contact",text="Contact")
        self.CourseTable.heading("admission",text="Date")
        self.CourseTable.heading("type",text="Type")
        self.CourseTable.heading("state",text="State")
        self.CourseTable.heading("city",text="City")
        self.CourseTable.heading("pin",text="Pin")
        self.CourseTable.heading("address",text="Address")
        self.CourseTable["show"]='headings'
        self.CourseTable.column("tracking_id",width=100)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("type",width=100)
        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

    #================Functions================

    def fetch_type(self):
        con=sqlite3.connect(database=r'rms.db')
        cur=con.cursor()
        try:
            cur.execute("select name from type")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        finally:
            con.close()

    def add(self):
        con=sqlite3.connect(database=r'rms.db')
        cur=con.cursor()
        try:
            if self.var_tracking_id.get()=="":
                messagebox.showerror("Error","ກະລຸນາປ້ອນເລກພັດສະດຸ",parent=self.root)
            else:
                cur.execute("select * from parcel where tracking_id=?",(self.var_tracking_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","ເລກພັດສະດຸນີ້ມີໃນລະບົບແລ້ວ",parent=self.root)
                else:
                    
                    cur.execute("insert into parcel (tracking_id,name,email,gender,dob,contact,admission,type,state,city,pin,address) values(?,?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_tracking_id.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_type.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0",END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","ບັນທຶກຂໍ້ມູນພັດສະດຸສຳເລັດ",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        finally:
            con.close()

    def update(self):
        con=sqlite3.connect(database=r'rms.db')
        cur=con.cursor()
        try:
            if self.var_tracking_id.get()=="":
                messagebox.showerror("Error","ກະລຸນາເລືອກຂໍ້ມູນທີ່ຕ້ອງການແກ້ໄຂ",parent=self.root)
            else:
                cur.execute("select * from parcel where tracking_id=?",(self.var_tracking_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","ບໍ່ພົບຂໍ້ມູນ",parent=self.root)
                else:
                    cur.execute("update parcel set name=?,email=?,gender=?,dob=?,contact=?,admission=?,type=?,state=?,city=?,pin=?,address=? where tracking_id=?",(
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_type.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0",END),
                        self.var_tracking_id.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","ແກ້ໄຂຂໍ້ມູນສຳເລັດ",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        finally:
            con.close()

    def show(self):
        con=sqlite3.connect(database=r'rms.db')
        cur=con.cursor()
        try:
            cur.execute("select * from parcel")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        finally:
            con.close()

    def get_data(self,ev):
        f=self.CourseTable.focus()
        content=(self.CourseTable.item(f))
        row=content['values']
        if row:
            self.var_tracking_id.set(row[0])
            self.var_name.set(row[1])
            self.var_email.set(row[2])
            self.var_gender.set(row[3])
            self.var_dob.set(row[4])
            self.var_contact.set(row[5])
            self.var_a_date.set(row[6])
            self.var_type.set(row[7])
            self.var_state.set(row[8])
            self.var_city.set(row[9])
            self.var_pin.set(row[10])
            self.txt_address.delete("1.0",END)
            self.txt_address.insert(END,row[11])

    def delete(self):
        con=sqlite3.connect(database=r'rms.db')
        cur=con.cursor()
        try:
            if self.var_tracking_id.get()=="":
                messagebox.showerror("Error","ກະລຸນາປ້ອນເລກພັດສະດຸ",parent=self.root)
            else:
                cur.execute("select * from parcel where tracking_id=?",(self.var_tracking_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","ບໍ່ພົບຂໍ້ມູນ",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","ທ່ານຕ້ອງການລຶບຂໍ້ມູນແທ້ບໍ?",parent=self.root)
                    if op==True:
                        cur.execute("delete from parcel where tracking_id=?",(self.var_tracking_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","ລຶບຂໍ້ມູນສຳເລັດ",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        finally:
            con.close()

    def clear(self):
        self.show()
        self.var_tracking_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("ເລືອກເພດ")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_a_date.set("")
        self.var_type.set("ເລືອກປະເພດ")
        self.var_state.set("")
        self.var_city.set("")
        self.var_pin.set("")
        self.txt_address.delete("1.0",END)
        self.var_search.set("")

    def search(self):
        con=sqlite3.connect(database=r'rms.db')
        cur=con.cursor()
        try:
            cur.execute(f"select * from parcel where tracking_id LIKE '%{self.var_search.get()}%'")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
           
            for row in rows:
                 self.CourseTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        

if __name__ == "__main__":
    root = Tk()
    obj = informationClass(root)
    root.mainloop()