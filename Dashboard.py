from tkinter import*
from PIL import Image,ImageTk     #pip install pilow
from manage import manageClass
from information import informationClass
from result import resultClass
from check import checkClass
from tkinter import messagebox
import os

class RMS:
    def __init__(self,root):
        self.root = root
        self.root.title("ລະບົບຈັດການຜົນການສົ່ງຂອງສິນຄ້າ (Delivery Management System)")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #===icons===
        self.logo_dash = None
        try:
            logo = Image.open("image/deli.webp") 
            logo = logo.resize((50, 50), Image.LANCZOS)
            self.logo_dash = ImageTk.PhotoImage(logo)
        except FileNotFoundError:
            pass
        #===title===
        title=Label(self.root,text="ລະບົບຈັດການຜົນການສົ່ງຂອງພັດສະດຸ",padx=10,compound=LEFT,image=self.logo_dash,font=("Phetsarath OT",20,"bold"),bg="#96B609",fg="white").place(x=0,y=0,relwidth=1,height=50)
        #===ໃສ່ເມນູ===
        M_Frame=LabelFrame(self.root,text="Menus",font=("time new roman",15),bg="white")
        M_Frame.place(x=10, y=70, width=1340, height=90)

        btn_type=Button(M_Frame, text="ຈັດການບໍລິການ", font=("phetsarath OT",15,"bold"),bg="#96B609",fg="white",cursor="hand2",command=self.add_course).place(x=50, y=5, width=200, height=40)
        btn_student=Button(M_Frame, text="ຂໍ້ມູນພັດສະດຸ", font=("phetsarath OT",15,"bold"),bg="#96B609",fg="white",cursor="hand2",command=self.add_student).place(x=320, y=5, width=200, height=40)
        btn_result=Button(M_Frame, text="ບັນທຶກຜົົນການສົ່ງ", font=("phetsarath OT",15,"bold"),bg="#96B609",fg="white",cursor="hand2",command=self.add_result).place(x=600, y=5, width=200, height=40)
        btn_view=Button(M_Frame, text="ກວດສອບຂໍ້ມູນ", font=("phetsarath OT",15,"bold"),bg="#96B609",fg="white",cursor="hand2",command=self.add_view).place(x=870, y=5, width=200, height=40)
        btn_exist=Button(M_Frame, text="ອອກຈາກລະບົບ", font=("phetsarath OT",15,"bold"),bg="#96B609",fg="white",cursor="hand2",command=self.exist).place(x=1120, y=5, width=200, height=40)
 
        #===content_window===
        self.bg_img = None
        try:
            bg = Image.open("image/d.webp")
            bg = bg.resize((920,350),Image.LANCZOS)
            self.bg_img = ImageTk.PhotoImage(bg)
            self.lbg_bg = Label(self.root,image=self.bg_img)
            self.lbg_bg.place(x=200,y=180,width=920,height=370)
            self.lbg_bg.image = self.bg_img
        except FileNotFoundError:
            self.lbg_bg = Label(self.root,bg="white")
            self.lbg_bg.place(x=200,y=180,width=920,height=370)

        #===update_details===
        self.lbl_type=Label(self.root,text="ເສັ້ນທາງທັງໝົດ\n[ 0 ]",font=("Phetsarath OT",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_type.place(x=200,y=560,width=300,height=80)
        
        self.lbl_student=Label(self.root,text="ພັດສະດຸທັງໝົດ\n[ 0 ]",font=("Phetsarath OT",20),bd=10,relief=RIDGE,bg="#0faece",fg="white")
        self.lbl_student.place(x=510,y=560,width=300,height=80)

        self.lbl_result=Label(self.root,text="ຜົນການສົ່ງທັງໝົດ\n[ 0 ]",font=("Phetsarath OT",20),bd=10,relief=RIDGE,bg="#de0eed",fg="white")
        self.lbl_result.place(x=820,y=560,width=300,height=80)
        
       
        #===footer===
        footer=Label(self.root,text="Delivery Result Management System\nContact us for any Technical Issue: 55418943",font=("goudy old style",12,),bg="#262626",fg="white").pack(side=BOTTOM, fill=X)
 
    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=manageClass(self.new_win)

    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=informationClass(self.new_win)

    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)

    def add_view(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=checkClass(self.new_win)
 
    def exist(self):
        op=messagebox.askyesno("Confirm","ທ່ານຕ້ອງການອອກຈາກຫນ້າຕ່າງນີ້ແທ້ບໍ",parent=self.root)
        if op==True:
            self.root.destroy()


if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()