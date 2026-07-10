from tkinter import*
from PIL import Image,ImageTk     #pip install pilow
from tkinter import ttk,messagebox
import sqlite3
class manageClass:
    def __init__(self,root):
        self.root = root
        self.root.title("ຈັດການລາຍລະອຽດການຂົນສົ່ງ")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        #===title====
        title=Label(self.root,text="ຈັດການລາຍລະອຽດການຂົນສົ່ງ",font=("Phetsarath OT",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,width=1180,height=35)
        #====Variables===
        self.var_type=StringVar()
        self.var_duration=StringVar()
        self.var_charges=StringVar()

        #====widgets======
        lbl_typeName=Label(self.root,text="ປະເພດສິນຄ້າ",font=("Phetsarath OT",15,'bold'),bg='white').place(x=10,y=60)
        lbl_duration=Label(self.root,text="ໄລຍະເວລາການຈັດສົ່ງ",font=("Phetsarath OT",15,'bold'),bg='white').place(x=10,y=100)
        lbl_charges=Label(self.root,text="ຄ່າທຳນຽມການສົ່ງ",font=("Phetsarath OT",15,'bold'),bg='white').place(x=10,y=140)
        lbl_description=Label(self.root,text="ລາຍລະອຽດເພີ່ມເຕີມ",font=("Phetsarath OT",15,'bold'),bg='white').place(x=10,y=180)

        #====Enttry Fields=====
        self.txt_typeName=Entry(self.root,textvariable=self.var_type,font=("Phetsarath OT",15,'bold'),bg='lightyellow')
        self.txt_typeName.place(x=200,y=60,width=200)
        txt_duration=Entry(self.root,textvariable=self.var_duration,font=("Phetsarath OT",15,'bold'),bg='lightyellow').place(x=200,y=100,width=200)
        txt_charges=Entry(self.root,textvariable=self.var_charges,font=("Phetsarath OT",15,'bold'),bg='lightyellow').place(x=200,y=140,width=200)
        self.txt_description=Text(self.root,font=("Phetsarath OT",15,'bold'),bg='lightyellow')
        self.txt_description.place(x=200,y=180,width=480,height=130)


        #===Buttons====)
        self.btn_add=Button(self.root,text='ບັນທຶກ',font=("Phetsarath OT",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=150,y=400,width=110,height=40)
        self.btn_update=Button(self.root,text='ແກ້ໄຂ',font=("Phetsarath OT",15,"bold"),bg="#03c04a",fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=270,y=400,width=110,height=40)
        self.btn_delete=Button(self.root,text='ລົບ',font=("Phetsarath OT",15,"bold"),bg="#f44336",fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390,y=400,width=110,height=40)
        self.btn_clear=Button(self.root,text='ລ້າງ',font=("Phetsarath OT",15,"bold"),bg="#607d8b",fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510,y=400,width=110,height=40)
        #===Seach panel===
        self.var_search=StringVar()
        lbl_search_typeName=Label(self.root,text="ປະເພດສິນຄ້າ",font=("Phetsarath OT",15,'bold'),bg='white').place(x=720,y=60)
        txt_search_typeName=Entry(self.root,textvariable=self.var_search,font=("Phetsarath OT",15,'bold'),bg='lightyellow').place(x=870,y=60,width=180)
        btn_search=Button(self.root,text='ຄົ້ນຫາ',font=("Phetsarath OT",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.search).place(x=1070,y=60,width=120,height=28)
        #====Content Table===
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=100,width=470,height=340)

        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("name","duration","charges","description"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
       
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)

        
        self.CourseTable.heading("name",text="ປເພດສິນຄ້າ")
        self.CourseTable.heading("duration",text="ໄລຍະເວລາ")
        self.CourseTable.heading("charges",text="ຄ່າທຳນຽມການສົ່ງ")
        self.CourseTable.heading("description",text="ລາຍລະອຽດເພີ່ມເຕີມ")
        self.CourseTable["show"]="headings"
        
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("duration",width=100)
        self.CourseTable.column("charges",width=100)
        self.CourseTable.column("description",width=150)
        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#=====================================================================
    def clear(self):
        self.show()
        self.var_type.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.txt_description.delete('1.0',END)
        self.txt_typeName.config(state=NORMAL)  #ປິດສະຖານະ

    def delete(self):
        con=sqlite3.connect(database=r'rms.db')
        cur=con.cursor()
        try:
            if self.var_type.get()=="":
                messagebox.showerror("ຂໍ້ຜິດພາດ","ກະລຸນາເລືອກປະເພດສິນຄ້າ",parent=self.root)
            else:
                cur.execute("SELECT * FROM type WHERE name=?",(self.var_type.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("ຂໍ້ຜິດພາດ","ກະລຸນາເລືອກປະເພດສິນຄ້າໃນລາຍຊື່ກ່ອນ",parent=self.root)
                else:
                    op=messagebox.askyesno("ຢືນຢັນການລຶບຂໍ້ມູນ","ທ່ານຕ້ອງການລຶບຂໍ້ມູນນີ້ອີ່ຫລີບໍ?",parent=self.root)
                    if op==True:
                        cur.execute("DELETE FROM type WHERE name=?",(self.var_type.get(),))
                        con.commit()
                        messagebox.showinfo("ລົບຂໍ້ມູນ","ຂໍ້ມູນຖືກລົບສຳເລັດ",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
   
    def get_data(self, ev=None):
        self.txt_typeName.config(state='readonly')  #ເປີດສະຖານະ
        self.txt_typeName
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content['values']
        #print(row)
        self.var_type.set(row[0])
        self.var_duration.set(row[1])
        self.var_charges.set(row[2])
        #=====self.var_course.set(row[4]) =====text ບໍ່ໄດ້ໃຊ້ StringVar ໄດ້ຕ້ອງໃຊ້ Text ແທນ
        self.txt_description.delete('1.0',END)
        self.txt_description.insert(END,row[3])
  
    def add(self):
        con=sqlite3.connect(database=r'rms.db')
        cur=con.cursor()
        try:
            if self.var_type.get()=="":
                messagebox.showerror("Error","ກະລຸນາປ້ອນຊື່ປະເພດສິນຄ້າ",parent=self.root)
            else:
                cur.execute("SELECT * FROM type WHERE name=?",(self.var_type.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","ສິນຄ້ານີ້ມີຢູ່ໃນລະບົບແລ້ວ",parent=self.root)
                else:
                    cur.execute("INSERT INTO type (name,duration,charges,description) VALUES (?,?,?,?)",(
                        self.var_type.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get('1.0',END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","ຂໍ້ມູນຖືກບັນທຶກສຳເລັດ",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def update(self):
        con=sqlite3.connect(database=r'rms.db')
        cur=con.cursor()
        try:
            if self.var_type.get()=="":
                messagebox.showerror("Error","Type Name must be required",parent=self.root)
            else:
                cur.execute("SELECT * FROM type WHERE name=?",(self.var_type.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select Type from list",parent=self.root)
                else:
                    cur.execute(" UPDATE type SET duration=?,charges=?,description=? WHERE name=?",(         
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get('1.0',END),
                        self.var_type.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","ຂໍ້ມູນອັບເດດສຳເລັດແລ້ວ",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def show(self):
        con=sqlite3.connect(database=r'rms.db')
        cur=con.cursor()
        try:                                                                      
                cur.execute("SELECT name,duration,charges,description FROM type")
                row=cur.fetchall()
                self.CourseTable.delete(*self.CourseTable.get_children())
                for row in row:
                    self.CourseTable.insert('',END,values=row)               
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def search(self):
        con=sqlite3.connect(database=r'rms.db')
        cur=con.cursor()
        try:                                                                                                                             
                cur.execute(f"SELECT name,duration,charges,description FROM type where name LIKE '%{self.var_search.get()}%'")
                row=cur.fetchall()
                self.CourseTable.delete(*self.CourseTable.get_children())
                for row in row:
                    self.CourseTable.insert('',END,values=row)               
        except Exception as ex:
            messagebox.showerror("ຂໍ້ຜິດພາດ",f"ຂໍ້ຜິດພາດໃນການຄົ້ນຫາຂໍ້ມູນເນື່ອງຈາກ: {str(ex)}")





if __name__=="__main__":
    root=Tk()
    obj=manageClass(root)
    root.mainloop()