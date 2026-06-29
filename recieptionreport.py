import os
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
import pymysql

from printpage import my_cust_PDF

class Report2Class:
    def __init__(self,home_window):
        self.window = Toplevel(home_window)
        # -------------settings ----------------------------
        # -----setting-----------
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        w1 = int(w - 260)
        h1 = int(h - 290)

        self.window.minsize(w1, h1)
        self.window.geometry("%dx%d+%d+%d" % (w1, h1, 245, 215))
        self.window.title("Hotel Manager/ Booking Report")

        from PIL import Image, ImageTk
        self.b = Image.open("images//hotelview.jpg")
        self.bk = ImageTk.PhotoImage(self.b)
        self.blbl = Label(self.window, image=self.bk)
        self.blbl.place(x=0, y=0, width=w, height=h)

        # --------------------- widgets -----------------------------------------------

        mycolor = '#BC9E82'
        mycolor2 = '#65000B'
        myfont1 = ('Trebuchet MS', 15)
        self.window.config(background=mycolor)

        self.hdlbl = Label(self.window,text="BOOKING",background=mycolor2,
                           font=("Georgia",30,'bold'),relief='groove',borderwidth=10,foreground='white')

        #---------------- table -------------

        self.mytable = Treeview(self.window, columns=['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7','c8','c9'], height=19)
        self.mytable.heading('c1', text='Reg_No')
        self.mytable.heading('c2', text='Name')
        self.mytable.heading('c3', text='Phone')
        self.mytable.heading('c4', text='UID')
        self.mytable.heading('c5', text='Check_In')
        self.mytable.heading('c6', text='Check_Out')
        self.mytable.heading('c7', text='Total_guests')
        self.mytable.heading('c8', text='Status')
        self.mytable.heading('c9', text='Mode')
        self.mytable['show'] = 'headings'

        self.mytable.column("#1", width=110, anchor='center')
        self.mytable.column("#2", width=210, anchor='center')
        self.mytable.column("#3", width=110, anchor='center')
        self.mytable.column("#4", width=110, anchor='center')
        self.mytable.column("#5", width=210, anchor='center')
        self.mytable.column("#6", width=210, anchor='center')
        self.mytable.column("#7", width=110, anchor='center')
        self.mytable.column("#8", width=110, anchor='center')
        self.mytable.column("#9", width=110, anchor='center')



        #-------------- buttons -----------------------------------------------

        self.b1 = Button(self.window,text="Print",background=mycolor2,foreground='white',font=myfont1,command=self.get_Printout)

        #-------------- placements -----------------------------------------------
        x1 = 20
        y1 = 80

        x_diff = 170
        y_diff = 40
        self.hdlbl.place(x=0, y=0, width=w1 + 260, height=60)

        self.mytable.place(x=x1,y=y1)
        self.b1.place(x=x1+500,y=y1+500,width=200)

        self.databaseConnection()
        self.getAllData()
        self.window.mainloop()


    def get_Printout(self):
        pdf = my_cust_PDF()
        headings = ['Reg_No', 'Name', 'Phone No ', 'Check_In', 'Check_Out', 'Guest(s)','Status','Mode']
        pdf.print_chapter(self.printData, headings)
        pdf.output('pdf_file1.pdf')
        os.system('explorer.exe "pdf_file1.pdf"')


    def databaseConnection(self):
        try:
            self.conn = pymysql.connect(host="localhost",db="hotel_manager_db",user="root",password="")
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showinfo("Database Error","Database Connection Error : \n"+str(e),parent=self.window)


    def getAllData(self):

        try:
            qry = "select * from booking_table "
            rowcount = self.curr.execute(qry)
            data = self.curr.fetchall()
            # print("data = \n",data)
            self.printData=[]

            if data:
                for myrow in data:
                    self.printData.append([myrow[0],myrow[1],myrow[2],myrow[4],myrow[5],myrow[6],myrow[7],myrow[8]])
                    self.mytable.insert("",END,values=myrow)

            else:
                messagebox.showwarning("Empty", "No Record Found", parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error", "Query Error : \n" + str(e), parent=self.window)

if __name__ == '__main__':
    dummy_homepage = Tk()
    Report2Class(dummy_homepage)
    dummy_homepage.mainloop()
