from tkinter import *
from tkinter.ttk import Combobox, Treeview
from tkinter import messagebox
import pymysql


class RoomClass:
    def __init__(self, home_window):
        self.window = Toplevel(home_window)

        mycolor = '#BC9E82'
        mycolor2 = '#65000B'
        myfont1 = ('Trebuchet MS', 15)

        self.window.title('Hotel Manager/ROOM DETAILS')
        self.window.config(background=mycolor)

        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        w1 = int(w - 260)
        h1 = int(h - 290)

        self.window.geometry(f"{w1}x{h1}+245+215")

        from PIL import Image, ImageTk
        self.b = Image.open("images//hotel room.webp")
        self.bk = ImageTk.PhotoImage(self.b)
        self.blbl = Label(self.window, image=self.bk)
        self.blbl.place(x=0, y=0, width=w, height=h)

        # -------- ROOM DATA --------
        self.room_data = {
            "AC": [{"room": "101", "floor": "1", "status": "Available"}],
            "Non-AC": [{"room": "101", "floor": "1", "status": "Available"}],
            "General": [{"room": "201", "floor": "1", "status": "Available"}],
            "Joint": [{"room": "201", "floor": "1", "status": "Available"}]
        }

        # -------- VARIABLES --------
        self.v1 = StringVar()
        self.v2 = StringVar()
        self.v3 = StringVar()
        self.v4 = StringVar()
        self.v5 = StringVar()

        # -------- LABELS --------
        Label(self.window, text='ROOMS SLOT', bg=mycolor2,
              font=('Georgia', 30, 'bold'), fg='white').place(x=0, y=0, width=w1+260, height=60)

        labels = ['Reg_No', 'Room Type', 'Room No', 'Bed Type', 'Status',
                  'Floor', 'Room Price', 'No of Days', 'Total Bill']

        for i, text in enumerate(labels):
            Label(self.window, text=text, bg=mycolor, font=myfont1).place(x=20, y=80 + i * 40)

        # -------- INPUTS --------
        self.c1 = Combobox(self.window, values=[str(i) for i in range(1, 21)],
                           textvariable=self.v1, state='readonly')
        self.c2 = Combobox(self.window, values=list(self.room_data.keys()),
                           textvariable=self.v2, state='readonly')
        self.c3 = Combobox(self.window, textvariable=self.v3, state='readonly')
        self.c4 = Combobox(self.window, values=('Single Bed', 'Double Bed'),
                           textvariable=self.v4, state='readonly')
        self.c5 = Combobox(self.window, values=('Available', 'Non-Available'),
                           textvariable=self.v5, state='readonly')

        self.c1.set('Select Reg no')
        self.c2.set('Choose Room Type')
        self.c3.set('Select Room No')
        self.c4.set('Choose Bed Type')
        self.c5.set('Status')

        self.t6 = Entry(self.window)
        self.t7 = Entry(self.window)
        self.t8 = Entry(self.window)
        self.t9 = Entry(self.window, state='readonly')

        widgets = [self.c1, self.c2, self.c3, self.c4, self.c5,
                   self.t6, self.t7, self.t8, self.t9]

        for i, wdg in enumerate(widgets):
            wdg.place(x=200, y=80 + i * 40)

        # -------- BUTTONS --------
        Button(self.window, text='Save', bg=mycolor2, fg='white',
               command=self.saveData).place(x=20, y=450, width=100,height=30)

        Button(self.window, text='Update', bg=mycolor2, fg='white',
               command=self.updateData).place(x=130, y=450, width=100,height=30)

        Button(self.window, text='Delete', bg=mycolor2, fg='white',
               command=self.deleteData).place(x=240, y=450, width=100,height=30)

        Button(self.window, text='Search', bg=mycolor2, fg='white',
               command=self.clearPage).place(x=380, y=80, width=100,height=30)

        Button(self.window, text='Fetch', bg=mycolor2, fg='white',
               command=self.fetchData).place(x=380, y=115, width=100,height=30)

        Button(self.window, text='Reset', bg=mycolor2, fg='white',
               command=self.clearPage).place(x=380, y=150, width=100,height=30)

        # -------- TABLE --------
        self.mytable = Treeview(self.window,
                                columns=('c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9'),
                                show='headings')

        cols = ['Reg_No', 'Type', 'Room', 'Bed', 'Status',
                'Floor', 'Price', 'Days', 'Total']

        for i, col in enumerate(cols):
            self.mytable.heading(f'c{i+1}', text=col)
            self.mytable.column(f'#{i+1}',width=60)

        self.mytable.place(x=500, y=80, width= 750,height=400)

        # -------- EVENTS --------
        self.c2.bind("<<ComboboxSelected>>", self.filter_rooms)
        self.c3.bind("<<ComboboxSelected>>", self.fill_room_details)

        self.t7.bind("<KeyRelease>", lambda e: self.calculate_total())
        self.t8.bind("<KeyRelease>", lambda e: self.calculate_total())

        # -------- DB --------
        self.databaseConnection()
        self.getAllData()

    # -------- LOGIC --------
    def filter_rooms(self, event=None):
        rooms = [r["room"] for r in self.room_data.get(self.v2.get(), [])]
        self.c3['values'] = rooms

    def fill_room_details(self, event=None):
        for r in self.room_data.get(self.v2.get(), []):
            if r["room"] == self.v3.get():
                self.v5.set(r["status"])
                self.t6.delete(0, END)
                self.t6.insert(0, r["floor"])

    def calculate_total(self):
        try:
            total = int(self.t7.get()) * int(self.t8.get())
            self.t9.config(state='normal')
            self.t9.delete(0, END)
            self.t9.insert(0, total)
            self.t9.config(state='readonly')
        except:
            pass

    # -------- DATABASE --------
    def databaseConnection(self):
        try:
            self.conn = pymysql.connect(
                host='localhost',
                user='root',
                password='',  # keep empty for XAMPP
                database='hotel_manager_db'
            )
            self.curr = self.conn.cursor()
        except Exception as e:
            self.conn = None
            self.curr = None
            messagebox.showerror("DB Error", str(e))

    def saveData(self):
        if not self.curr:
            messagebox.showerror("Error", "Database not connected")
            return
        try:
            self.curr.execute(
                "INSERT INTO roominfo_table VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (self.v1.get(), self.v2.get(), self.v3.get(), self.v4.get(),
                 self.v5.get(), self.t6.get(), self.t7.get(), self.t8.get(), self.t9.get())
            )
            self.conn.commit()
            messagebox.showinfo(" Saved Successfully", "Saved")
            self.getAllData()
            self.clearPage()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def updateData(self):
        if not self.curr:
            messagebox.showerror("Error", "Database not connected")
            return

        if self.v1.get() == "" or self.v1.get() == "Select Reg no":
            messagebox.showerror("Error", "Select record to update")
            return

        try:
            self.curr.execute("""
                              UPDATE roominfo_table SET Type=%s,Room=%s,Bed=%s,Status=%s,Floor=%s,Price=%s,Days=%s,Total=%s WHERE Reg_No = %s
                              """, (
                                  self.v2.get(), self.v3.get(), self.v4.get(), self.v5.get(),
                                  self.t6.get(), self.t7.get(), self.t8.get(), self.t9.get(),
                                  self.v1.get()
                              ))

            self.conn.commit()

            if self.curr.rowcount == 0:
                messagebox.showwarning("Warning", "No record updated (check Reg_No)")
            else:
                messagebox.showinfo("Success", "Updated Successfully")

            self.getAllData()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def deleteData(self):
        if not self.curr:
            messagebox.showerror("Error", "Database not connected")
            return

        selected = self.mytable.focus()
        data = self.mytable.item(selected)

        if not data['values']:
            messagebox.showwarning("Warning", "Select a row first")
            return

        reg_no = data['values'][0]

        confirm = messagebox.askyesno("Confirm", "Delete this record?")
        if not confirm:
            return

        try:
            self.curr.execute("DELETE FROM roominfo_table WHERE Reg_No=%s", (reg_no,))
            self.conn.commit()

            self.mytable.delete(selected)

            messagebox.showinfo("Success", "Deleted Successfully")
            self.clearPage()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def fetchData(self):
        selected = self.mytable.focus()
        data = self.mytable.item(selected)

        if not data['values']:
            messagebox.showwarning("Warning", "Select a row first")
            return

        row = data['values']
        self.v1.set(row[0])
        self.v2.set(row[1])
        self.v3.set(row[2])
        self.v4.set(row[3])
        self.v5.set(row[4])
        self.t6.delete(0, END)
        self.t6.insert(0, row[5])
        self.t7.delete(0, END)
        self.t7.insert(0, row[6])
        self.t8.delete(0, END)
        self.t8.insert(0, row[7])
        self.t9.config(state='normal')
        self.t9.delete(0, END)
        self.t9.insert(0, row[8])
        self.t9.config(state='readonly')

    def getAllData(self):
        if not self.curr:
            return
        try:
            self.curr.execute("SELECT * FROM roominfo_table")
            rows = self.curr.fetchall()
            self.mytable.delete(*self.mytable.get_children())
            for row in rows:
                self.mytable.insert('', END, values=row)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clearPage(self):
        self.v1.set("Select Reg no")
        self.v2.set("Choose Room Type")
        self.v3.set("Select Room No")
        self.v4.set("Choose Bed Type")
        self.v5.set("Status")
        self.t6.delete(0, END)
        self.t7.delete(0, END)
        self.t8.delete(0, END)
        self.t9.config(state='normal')
        self.t9.delete(0, END)
        self.t9.config(state='readonly')


if __name__ == '__main__':
    root = Tk()
    RoomClass(root)
    root.mainloop()

