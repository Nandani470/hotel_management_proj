from tkinter import*
from tkinter import messagebox
from recieption import BookingClass
from roomreport import Report1Class
from rooms import RoomClass
from recieptionreport import Report2Class
from ManageUser import UserClass
from ChangePassword import ChangePasswordClass
from PIL import Image,ImageTk
class HotelManagementSystem:
    def __init__(self,uname,utype):
        self.utype=utype
        self.uname=uname
        self.root= Tk()
        self.root.title("Hotel Management System")

        self.w = self.root.winfo_screenwidth()
        self.h = self.root.winfo_screenheight()
        self.root.minsize(self.w,self.h)
        self.root.state('zoomed')

        img_h1 = 140
        imgw1 = 250

        self.b1 = Image.open("images/images1/hotel9.jpeg")
        self.b1 = ImageTk.PhotoImage(self.b1)
        self.blbl1 = Label(self.root,bd=5,relief=RIDGE,background='pink', image=self.b1)
        self.blbl1.place(x=imgw1, y=0, width=self.w-imgw1, height=img_h1)


       #============logo============================================
        self.b2 = Image.open("images/images1/logo4.webp")
        self.b2 = ImageTk.PhotoImage(self.b2)
        self.blbl = Label(self.root, image=self.b2, bd=5, relief=RIDGE)
        self.blbl.place(x=0, y=0, width=imgw1, height=img_h1)


        self.hdlbl = Label(self.root, text='HOTEL MANAGEMENT SYSTEM', background='black', font=('Georgia', 35, 'bold'),
                           relief='groove', borderwidth='4', foreground='white')
        self.hdlbl.place(x=0, y=img_h1, width=self.w, height=50)
        #========================menu=====================



        #========================button frame========================
        btn_font1 = ('Georgia', 14, 'bold')
        frame_height=self.h-(img_h1+50)
        frame_width=300
        btn_width=250
        btn_height=50
        all_btns_h = btn_height*7+40
        #====================mainframe==================
        bg1 = 'black'
        fg1 = 'white'
        bw1=5
        self_frame =Frame(self.root,bd=1,relief='groove',background='white')
        self_frame.place(x=0, y=190, width=frame_width, height=frame_height)

        lbl_menu = Label(self_frame, text='MENU', background='#181111', font=('Georgia', 20, 'bold'),
                         relief='groove', borderwidth=1, foreground='white')
        lbl_menu.place(x=0, y=0, width=btn_width,height=40)


        btn_frame = Frame(self_frame, bd=0, relief='groove',background='blue')
        btn_frame.place(x=0, y=40, width=btn_width, height=all_btns_h)


        y1=0

        rece_btn = Button (btn_frame, text='RECEPTION',background=bg1, font=btn_font1,command=lambda : BookingClass(self.root),
                         relief='groove', borderwidth=bw1, foreground=fg1,cursor='hand1')
        rece_btn.place(x=0,y=y1,width=btn_width,height=btn_height)
        y1+=btn_height

        bookrep_btn =Button(btn_frame, text='RECIEPTION REPORT ', background=bg1, font=btn_font1,
                         relief='groove', borderwidth=bw1, foreground=fg1,cursor='hand1',command=lambda : Report2Class(self.root))
        bookrep_btn.place(x=0,y=y1,width=btn_width,height=btn_height)
        y1+=btn_height

        room_btn = Button(btn_frame, text='ROOMS SLOT', background=bg1, font=btn_font1,
                            relief='groove', borderwidth=bw1, foreground=fg1, cursor='hand1',command=lambda : RoomClass(self.root))
        room_btn.place(x=0,y=y1,width=btn_width,height=btn_height)
        y1+=btn_height

        roomrep_btn =Button (btn_frame, text='ROOMS REPORT', background=bg1, font=btn_font1,
                            relief='groove', borderwidth=bw1, foreground=fg1,  cursor='hand1',command=lambda : Report1Class(self.root))
        roomrep_btn.place(x=0,y=y1,width=btn_width,height=btn_height)
        y1+=btn_height

        chngepass_btn =Button (btn_frame, text='CHANGE PASSWORD', background=bg1, font=btn_font1,
                            relief='groove', borderwidth=bw1, foreground=fg1,cursor='hand1',command=lambda : ChangePasswordClass(self.root,self.uname))
        chngepass_btn.place(x=0,y=y1,width=btn_width,height=btn_height)
        y1+=btn_height

        user_btn =Button(btn_frame, text='USER', background=bg1, font=btn_font1,
                            relief='groove', borderwidth=bw1, foreground=fg1, cursor='hand1',command=lambda : UserClass(self.root))
        user_btn.place(x=0,y=y1,width=btn_width,height=btn_height)
        y1+=btn_height

        exit_btn = Button(btn_frame, text='EXIT', background=bg1, font=btn_font1,
                            relief='groove', borderwidth=bw1, foreground=fg1, cursor='hand1',command=self.quitter)
        exit_btn.place(x=0,y=y1,width=btn_width,height=btn_height)
        y1+=btn_height

        self.bk = Image.open("images/images1/hotel12.jpeg")
        self.bk = ImageTk.PhotoImage(self.bk)
        self.blbl4 = Label(self.root, image=self.bk ,bd=1, relief=RIDGE,background='green')
        self.blbl4.place(x=imgw1, y=img_h1+50, width=self.w-imgw1,height=self.h-(img_h1+50))

        self.b5 = Image.open("images/images1/hotel6.jpeg")
        self.b5 = ImageTk.PhotoImage(self.b5)
        self.blbl5 = Label(self_frame, image=self.b5, bd=2, relief=RIDGE)
        self.blbl5.place(x=0, y=all_btns_h, width=btn_width, height=frame_height-all_btns_h)
        self.root.mainloop()

    def quitter(self):
        ans = messagebox.askquestion("Confirmation", "Are you to Exit?", parent=self.root)
        if ans == 'yes':
            self.root.destroy()
            from Loginpage import LoginClass
            LoginClass()

        #class rece_btn(self):
        #def reception_py(self, home_window):
           # self.window = Toplevel(self,home_window)
#           self.window=BookingClass(self.window)
            #    self.window.title=rece_btn(self.window )
            #    self.window.geometry("1295x550+0+0")
if __name__ =='__main__':
    HotelManagementSystem("riya",456)




