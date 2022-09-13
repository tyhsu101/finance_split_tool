from tkinter import Tk                # python 3
from tkinter import font as tkfont  # python 3
from tkinter import *

class fui(Tk):

    def __init__(self):
        super().__init__()
        self.geometry('600x500')
        self.title('Fin split tool')
        self.create_widget()

    def create_widget(self):
        self.members = StringVar()
        self.members_val = {}
        Label(self, text="Input members", borderwidth=3).place(x=10, y=10)
        Entry(self, textvariable=self.members,width = 45).place(x=120, y=13)
        Button(self, text = 'Check member', command = self.create_checkbuttom).place(x=450, y=10)

    def create_checkbuttom(self):
        self.h_pos = 115
        for n in self.members.get().split(','):
            self.members_val[n] = BooleanVar()
            Checkbutton(self, text = n , var = self.members_val[n]).place(x=self.h_pos,y=35)
            self.h_pos += 40
        Button(self, text = 'show', command = self.show_chk_result, width=10).place(x=450,y=35)
    
    def show_chk_result(self):
        add_pos = 0
        for k, v in self.members_val.items():
            if v.get() == 1:
                Label(self, text=k).place(x=120 + add_pos, y = 60)
                add_pos += 25

        

 


if __name__ == "__main__":
    app = fui()
    app.mainloop()