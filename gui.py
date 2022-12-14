from tkinter import Tk                # python 3
from tkinter import font as tkfont  # python 3
from tkinter import *
from tkinter import messagebox
from splitwise import split_wise
#Adam,Bob,Cate,Dylan
class fui(Tk):

    def __init__(self):
        super().__init__()
        ## calculator
        ## main outline set
        self.geometry('600x500')
        self.title('Fin split tool')
        
        ## position var
        self.show_list_post = 150
        self.show_amt_h = 120
        ## var object
        self.members = StringVar()
        self.members_val = {}

        ## starter input: set members
        Label(self, text="Input members", borderwidth=3).place(x=10, y=10)
        self.member_entry = Entry(self, textvariable=self.members,width = 45)
        self.member_entry.place(x=120, y=13)
        Button(self, text = 'Set up members', command = self.set_up).place(x=450, y=10)

    def set_up(self):
        ### disable set buttom
        self.member_entry.config(state = 'disabled')
        ### set up members as list
        self.member_list = self.members.get().split(',')
        self.calculator = split_wise(self.member_list)
        self.calculator.open_account()
        ### start input
        ## amount
        Label(self,text = 'Expense\nAmount:').place(x=20, y=40)
        self.expense_amt = StringVar()
        self.amount = Entry(self,textvariable = self.expense_amt,width = 10)
        self.amount.place(x = 80,y = 50)
        ## giver
        Label(self,text = 'Select\nGiver:').place(x=160, y=40)
        self.giver_list = Listbox(self,width = 10, selectmode='single',height = len(self.member_list)*1)
        self.giver_list.place(x = 210,y = 40)
        for i,n in enumerate(self.member_list):
            self.giver_list.insert(1,n)
        ## recivers
        Label(self,text = 'Select\nReciver:').place(x=290, y=40)
        self.v_pos = 40
        for n in self.member_list:
            self.members_val[n] = BooleanVar()
            self.members_val[n].set(1)
            Checkbutton(self, text = n , var = self.members_val[n] ).place(x=350,y=self.v_pos)
            self.v_pos += 20
        #Button(self, text = 'show_reciver', command = self.show_chk_result, width=10).place(x=120,y=200)
        #Button(self, text = 'show_giver', command = self.show_list, width=10).place(x=200,y=200)
        Button(self,text = 'add expense',command=self.add_expense, width=10).place(x=450,y=40)
        Button(self,text = 'show balance',command=self.show_curr_balance, width=10).place(x=450,y=60)
        Button(self,text = 'show detail',command=self.show_detail, width=10).place(x=450,y=80)
        Button(self,text = 'Closing',command=self.closing_account, width=10).place(x=450,y=100)

    def add_expense(self):
        #show_text = self.giver_list.get(self.giver_list.curselection()) + ' give ' + self.expense_amt.get() + ' to ' +','.join([k[0] for k in self.members_val.items() if k[1].get()])
        #Label(self,text = show_text).place(x = 120,y= self.show_amt_h)
        self.show_amt_h += 20
        self.calculator.add_expense(int(self.expense_amt.get()),self.giver_list.get(self.giver_list.curselection()),[k[0] for k in self.members_val.items() if k[1].get()])
        self.amount.delete(0,'end')
    
    def show_curr_balance(self):
        text = ''
        for name,amt in self.calculator.balance.items():
            text = text + str(name) + ':' + str(amt) + '\n'
        messagebox.showinfo("Balance", text)
        
    def show_detail(self):
        #text = ''
        #for rows in self.calculator.detail.iterrows():
        #    text = text + str(rows['amount']) + ' paid by ' + str(rows['giver']) + ' recieve from ' + ','.join(rows['reciver']) + '\n'
        messagebox.showinfo("Detail", self.calculator.detail.__str__())

    def closing_account(self):
        text = self.calculator.close_account()
        messagebox.showinfo("Closing Account", text)

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