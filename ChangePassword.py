from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
import pymysql
class ChangePasswordClass:
    def __init__(self,home_window,uname):
        self.uname=uname
        self.window = Toplevel(home_window)
        # -------------settings ----------------------------
        # -----setting-----------
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        w1 = int(w - 260)
        h1 = int(h - 290)

        self.window.minsize(w1, h1)
        self.window.geometry("%dx%d+%d+%d" % (w1, h1, 245, 215))
        self.window.title("Hotel Manager/Change Password")
        # --------------------- widgets -----------------------------------------------

        mycolor = '#BC9E82'
        mycolor2 = '#65000B'
        myfont1 = ('Trebuchet MS', 15)

        self.window.config(background=mycolor)

        self.hdlbl = Label(self.window,text="Change Password",background=mycolor2,
                           font=("Georgia",30,'bold'),relief='groove',borderwidth=10,foreground='white')
        self.L1 = Label(self.window,text="Current Password",background=mycolor,font=myfont1)
        self.L2 = Label(self.window,text="New Password",background=mycolor,font=myfont1)
        self.L3 = Label(self.window,text="Confirm Password",background=mycolor,font=myfont1)

        self.t1 = Entry(self.window,font=myfont1,show='*')
        self.t2 = Entry(self.window,font=myfont1,show='*')
        self.t3 = Entry(self.window,font=myfont1,show='*')


        #-------------- buttons -----------------------------------------------

        self.b1 = Button(self.window,text="Change",background=mycolor2,foreground='white',
                         font=myfont1,command=self.updateData)

        #-------------- placements -----------------------------------------------

        x1 = 20
        y1 = 80

        x_diff = 170
        y_diff = 40
        self.hdlbl.place(x=0, y=0, width=w1 + 100, height=60)

        self.L1.place(x=x1,y=y1)
        self.t1.place(x=x1+x_diff,y=y1)

        y1+=y_diff
        self.L2.place(x=x1,y=y1)
        self.t2.place(x=x1+x_diff,y=y1)
        y1+=y_diff
        self.L3.place(x=x1,y=y1)
        self.t3.place(x=x1+x_diff,y=y1)
        y1+=y_diff
        self.b1.place(x=x1,y=y1,width=100,height=40)

        self.databaseConnection()
        self.clearPage()
        self.window.mainloop()

    def databaseConnection(self):
        try:
            self.conn = pymysql.connect(host="localhost",db="hotel_manager_db",user="root",password="")
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showinfo("Database Error","Database Connection Error : \n"+str(e),parent=self.window)

    def updateData(self):
        if self.validate_check()==False:
            return
        if(self.t2.get()==self.t3.get()):
            try:
                qry = "update usertable set password=%s  where username=%s and password=%s "
                rowcount = self.curr.execute(qry,(self.t2.get(), self.uname,self.t1.get()))
                self.conn.commit()
                if rowcount==1:
                    messagebox.showinfo("Success","Password changed successfully :)",parent=self.window)
                    self.clearPage()
                else:
                    messagebox.showwarning("Failure","Wrong current password",parent=self.window)
            except Exception as e:
                messagebox.showerror("Query Error", "Query Error : \n" + str(e), parent=self.window)
        else:
             messagebox.showwarning("Error", "Confirm password carefully", parent=self.window)

    def clearPage(self):
        self.t1.delete(0,END)
        self.t2.delete(0,END)
        self.t3.delete(0,END)

    def validate_check(self):
        if len(self.t1.get())<1:
            messagebox.showwarning("Validation Check", "Enter Current Password", parent=self.window)
            return False
        elif len(self.t2.get())<1:
            messagebox.showwarning("Validation Check", "Enter New Password", parent=self.window)
            return False
        elif len(self.t3.get())<1:
            messagebox.showwarning("Validation Check", "Enter Confirm Password", parent=self.window)
            return False
        return True


if __name__ == '__main__':
    dummy_homepage = Tk()
    ChangePasswordClass(dummy_homepage)
    dummy_homepage.mainloop()