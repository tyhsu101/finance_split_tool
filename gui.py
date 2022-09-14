from tkinter import Tk                # python 3
from tkinter import font as tkfont  # python 3
from tkinter import *
#Adam,Bob,Cate
class fui(Tk):

    def __init__(self):
        super().__init__()
        self.geometry('600x500')
        self.title('Fin split tool')
        self.show_list_post = 150
        
        self.members = StringVar()
        self.members_val = {}
        
        
        Label(self, text="Input members", borderwidth=3).place(x=10, y=10)
        self.member_entry = Entry(self, textvariable=self.members,width = 45)
        self.member_entry.place(x=120, y=13)
        Button(self, text = 'Check member', command = self.create_checkbuttom).place(x=450, y=10)

    def create_checkbuttom(self):
        self.member_entry.config(state = 'disabled')
        self.member_list = self.members.get().split(',')
        self.giver_list = Listbox(self,width = 10,selectmode='single')
        self.giver_list.place(x = 115,y = 40)
        for i,n in enumerate(self.mamber_list):
            self.giver_list.insert(1,n)

        self.v_pos = 30
        for n in self.mamber_list:
            self.members_val[n] = BooleanVar()
            self.members_val[n].set(1)
            Checkbutton(self, text = n , var = self.members_val[n] ).place(x=300,y=self.v_pos)
            self.v_pos += 20
        Button(self, text = 'show_reciver', command = self.show_chk_result, width=10).place(x=450,y=35)
        Button(self, text = 'show_giver', command = self.show_list, width=10).place(x=500,y=35)
    
    def show_chk_result(self):
        add_pos = 0
        for k, v in self.members_val.items():
            if v.get():
                Label(self, text=k).place(x=115 + add_pos, y = self.v_pos)
                add_pos += 30

    def show_list(self):
        
        Label(self,text = self.giver_list.get(self.giver_list.curselection())).place(x=self.show_list_post, y = 200)
        self.show_list_post+=20


        

 


if __name__ == "__main__":
    app = fui()
    app.mainloop()