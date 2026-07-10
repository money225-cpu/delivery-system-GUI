from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class resultClass:
    def __init__(self, root):
        self.root = root
        self.root.title("ລະບົບຈັດການຜົນການສົ່ງຂອງສິນຄ້າ (Delivery Management System)")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # === Title ====
        title = Label(self.root, text="ເພີ່ມຂໍ້ມູນຜົນການສົ່ງຂອງພັດສະດຸ", font=("Phetsarath OT", 20, "bold"), bg="orange", fg="#262626").place(x=10, y=15, width=1180, height=50)

        # ======= Variables ======
        self.var_tracking_id = StringVar() # เปลี่ยนจาก roll เป็น tracking_id
        self.var_name = StringVar()
        self.var_type = StringVar()        # เปลี่ยนจาก type เป็น type (ประเภท)
        self.var_weight = StringVar()      # เปลี่ยนจาก marks เป็น weight
        self.var_status = StringVar()  # เปลี่ยนจาก full_marks เป็น status
        
        self.tracking_list = []

        # ======= Labels =======
        lbl_select = Label(self.root, text="ເລືອກເລກພັດສະດຸ", font=("Phetsarath OT", 20, 'bold'), bg='white').place(x=50, y=100)
        lbl_name = Label(self.root, text="ຊື່ລູກຄ້າ", font=("Phetsarath OT", 20, 'bold'), bg='white').place(x=50, y=160)
        lbl_type = Label(self.root, text="ປະເພດສິນຄ້າ", font=("Phetsarath OT", 20, 'bold'), bg='white').place(x=50, y=220)
        lbl_weight = Label(self.root, text="ນໍ້າຫນັກສິນຄ້າ (kg)", font=("Phetsarath OT", 20, 'bold'), bg='white').place(x=50, y=280)
        lbl_st = Label(self.root, text="ສະຖານະພັດສະດຸ", font=("Phetsarath OT", 20, 'bold'), bg='white').place(x=50, y=340)

        # ======= Entry Fields =======
        self.txt_tracking = ttk.Combobox(self.root, textvariable=self.var_tracking_id, values=self.tracking_list, font=("Phetsarath OT", 15, 'bold'), state='readonly', justify=CENTER)
        self.txt_tracking.place(x=280, y=100, width=200)
        self.txt_tracking.set("ເລືອກ")
        
        self.fetch_tracking_ids()
        
        btn_search = Button(self.root, text='ຄົ້ນຫາ', font=("Phetsarath OT", 15, "bold"), bg="#03a9f4", fg="white", cursor="hand2", command=self.search).place(x=500, y=100, width=100, height=28)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("Phetsarath OT", 20, 'bold'), bg='lightyellow', state='readonly').place(x=280, y=160, width=320)
        txt_type = Entry(self.root, textvariable=self.var_type, font=("Phetsarath OT", 20, 'bold'), bg='lightyellow', state='readonly').place(x=280, y=220, width=320)
        txt_weight = Entry(self.root, textvariable=self.var_weight, font=("Phetsarath OT", 20, 'bold'), bg='lightyellow').place(x=280, y=280, width=320)
        txt_st = Entry(self.root, textvariable=self.var_status, font=("Phetsarath OT", 20, 'bold'), bg='lightyellow').place(x=280, y=340, width=320)

        # ==== Buttons ====
        btn_add = Button(self.root, text='ສົ່ງ', font=("Phetsarath OT", 15, "bold"), bg="lightgreen", activebackground="lightgreen", cursor="hand2", command=self.add).place(x=300, y=420, width=120, height=35)
        btn_clear = Button(self.root, text='ລ້າງ', font=("Phetsarath OT", 15, "bold"), bg="lightgray", activebackground="lightgray", cursor="hand2", command=self.clear).place(x=430, y=420, width=120, height=35)

        # ==== Image ====
        
        try:
            self.bg_img = Image.open("image/Mad.jpg") 
            self.bg_img = self.bg_img.resize((500, 300), Image.LANCZOS)
            self.bg_img = ImageTk.PhotoImage(self.bg_img)
            self.lbg_bg = Label(self.root, image=self.bg_img).place(x=650, y=100)
        except Exception as e:
            print("Image not found, skipping image load.")

    
    def fetch_tracking_ids(self):
        


        con = sqlite3.connect(database=r'rms.db')
        cur = con.cursor()
        try:
            cur.execute("select tracking_id from parcel") 
            row = cur.fetchall()
            self.tracking_list.clear() 
            if len(row) > 0:
                for r in row:
                    self.tracking_list.append(r[0])
            self.txt_tracking.config(values=self.tracking_list) 
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    def search(self):
        con = sqlite3.connect(database=r'rms.db')
        cur = con.cursor()
        try:
            cur.execute("select name,type from parcel where tracking_id=? ", (self.var_tracking_id.get(),))
            row = cur.fetchone()
            if row != None:
                self.var_name.set(row[0])
                self.var_type.set(row[1])
            else:
                messagebox.showerror("Error", "ບໍ່ພົບລະຫັດພັດສະດຸ!!!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()


    def add(self):
        con = sqlite3.connect(database=r'rms.db')
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "ໂປດເລືອກລະຫັດພັດສະດຸກ່ອນ", parent=self.root)
            else:
                
                cur.execute("select * from result where tracking_id=?", (self.var_tracking_id.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "ຂໍ້ມູນນີ້ມີຢຸ່ແລ້ວ", parent=self.root)
                else:  
                    fake_per = "0" 
                    
                    cur.execute("INSERT INTO result (tracking_id,name,type,weight,status,per) VALUES (?,?,?,?,?,?)", (
                        self.var_tracking_id.get(),
                        self.var_name.get(),
                        self.var_type.get(),
                        self.var_weight.get(),      
                        self.var_status.get(),  
                        fake_per
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "ຂໍ້ມູນສົ່ງສິນຄ້າຖືກບັນທຶກສຳເລັດແລ້ວ", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()

    def clear(self):
        self.var_tracking_id.set("ເລືອກ") 
        self.var_name.set("")
        self.var_type.set("")
        self.var_weight.set("")
        self.var_status.set("")

if __name__ == "__main__":
    root = Tk()
    obj = resultClass(root)
    root.mainloop()