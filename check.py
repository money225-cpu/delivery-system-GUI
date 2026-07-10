from tkinter import*
from PIL import Image,ImageTk     #pip install pilow
from tkinter import ttk,messagebox
import sqlite3
class checkClass:
    def __init__(self,root):
        self.root = root
        self.root.title("ລະບົບຈັດການຜົນການສົ່ງຂອງສິນຄ້າ")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        #===title====
        title=Label(self.root,text="ລະບົບຈັດການຜົນການສົ່ງຂອງສິນຄ້າ",font=("Phetsarath OT",20,"bold"),bg="orange",fg="#262626").place(x=10,y=15,width=1180,height=50)

        #=====search======
        self.var_search=StringVar()
        self.var_id=""

        lbl_search=Label(self.root,text="ຄົ້ນຫາໂດຍເລກພັດສະດຸ",font=("Phetsarath OT",20,"bold"),bg='white').place(x=280,y=100)
        txt_search=Entry(self.root,textvariable=self.var_search,font=("Phetsarath OT",20),bg='lightyellow').place(x=570,y=100,width=190)
        btn_search=Button(self.root,text='ຄົ້ນຫາ',font=("Phetsarath OT",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search).place(x=780,y=100,width=100,height=35)
        btn_clear=Button(self.root,text='ລ້າງ',font=("Phetsarath OT",15,"bold"),bg="gray",fg="white",cursor="hand2",command=self.clear).place(x=900,y=100,width=100,height=35)
       
        #====result labels====
        lbl_tracking_id=Label(self.root,text="ເລກພັດສະດຸ",font=("Phetsarath OT",15,'bold'),bg='white',bd=2,relief=GROOVE).place(x=150,y=230,width=150,height=50)
        lbl_name=Label(self.root,text="ຊື່",font=("Phetsarath OT",15,'bold'),bg='white',bd=2,relief=GROOVE).place(x=300,y=230,width=150,height=50)
        lbl_type=Label(self.root,text="ປະເພດສິນຄ້າ",font=("Phetsarath OT",15,'bold'),bg='white',bd=2,relief=GROOVE).place(x=450,y=230,width=150,height=50)
        lbl_weight=Label(self.root,text="ນໍ້າໜັກສິນຄ້າ",font=("Phetsarath OT",14,'bold'),bg='white',bd=2,relief=GROOVE).place(x=600,y=230,width=160,height=50)
        lbl_status=Label(self.root,text="ສະຖານະພັດສະດຸ",font=("Phetsarath OT",15,'bold'),bg='white',bd=2,relief=GROOVE).place(x=760,y=230,width=170,height=50)

        self.tracking_id=Label(self.root,font=("Phetsarath OT",15,'bold'),bg='white',bd=2,relief=GROOVE)
        self.tracking_id.place(x=150,y=280,width=150,height=50)
        self.name=Label(self.root,font=("Phetsarath OT",15,'bold'),bg='white',bd=2,relief=GROOVE)
        self.name.place(x=300,y=280,width=150,height=50)
        self.type=Label(self.root,font=("Phetsarath OT",15,'bold'),bg='white',bd=2,relief=GROOVE)
        self.type.place(x=450,y=280,width=150,height=50)
        self.weight=Label(self.root,font=("Phetsarath OT",14,'bold'),bg='white',bd=2,relief=GROOVE)
        self.weight.place(x=600,y=280,width=160,height=50)
        self.status=Label(self.root,font=("Phetsarath OT",15,'bold'),bg='white',bd=2,relief=GROOVE)
        self.status.place(x=760,y=280,width=170,height=50)
        

        #=========button delete=====
        btn_delete=Button(self.root,text='ລົບ',font=("Phetsarath OT",15,"bold"),bg="red",fg="white",cursor="hand2",command=self.delete).place(x=500,y=350,width=180,height=35)


#===========================================================================

    def search(self):
        con=sqlite3.connect(database=r'rms.db')
        cur=con.cursor()
        try:       
            if self.var_search.get()=="":  # Check if search field is empty
                    messagebox.showerror("Error", "ກະລຸນາປ້ອນລະຫັດພັດສະດຸທີ່ຕ້ອງການຄົ້ນຫາ", parent=self.root)
            else:
                cur.execute("select * from result where tracking_id=? ",(self.var_search.get(),))
                row=cur.fetchone()
                if row!=None:
                  self.var_id=row[0]
                  self.tracking_id.config(text=row[1])
                  self.name.config(text=row[2])
                  self.type.config(text=row[3])
                  self.weight.config(text=row[4])
                  self.status.config(text=row[5])
                else:
                    messagebox.showerror("Error","ບໍ່ພົບລະຫັດພັດສະດຸນີ້!!!",parent=self.root)            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    
    def clear(self):
        self.var_id=""
        self.tracking_id.config(text="")
        self.name.config(text="")
        self.type.config(text="")
        self.weight.config(text="")
        self.status.config(text="")
        self.var_search.set("")
    
    def delete(self):
        con=sqlite3.connect(database=r'rms.db')
        cur=con.cursor()
        try:
            if self.var_id=="":
                messagebox.showerror("Error","ໂປດປ້ອນລະຫັດຂອງຂໍ້ມູນທີ່ຕ້ອງການລຶບ",parent=self.root)
            else:
                cur.execute("select * from result where rid=?",(self.var_id,))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","ຂໍ້ມູນນີ້ບໍ່ມີໃນຖານຂໍ້ມູນ",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","ທ່ານຕ້ອງການຢາກລຶບຂໍ້ມູນນີ້ແທ້ບໍ",parent=self.root)
                    if op==True:
                        cur.execute("delete from result where rid=?",(self.var_id,))
                        con.commit()
                        messagebox.showinfo("Delete","ຂໍ້ມູນຖືກລຶບສຳເລັດແລ້ວ",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        finally:
            con.close()

if __name__=="__main__":
    root=Tk()
    obj=checkClass(root)
    root.mainloop()