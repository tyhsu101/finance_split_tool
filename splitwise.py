import pandas as pd

class split_wise:
    def __init__(self,mambers:tuple) -> None:
        self.members = mambers
        self.detail = pd.DataFrame(columns=['amount','giver','reciver','reciver_portion','detail'])
        self.balance = {}
        self.close = {}
    def open_account(self):
        for name in self.members:
            self.balance[name] = 0
    def add_expense(self,amount, giver ,recivers = None,reciver_portion = None  ,detail = ''):
        if reciver_portion != None and sum(reciver_portion) != amount:
            print('Sum up of portion does not equal to total amount!')
            return 0
        ### add into detail
        self.detail.loc[self.detail.shape[0]] = [amount ,giver,recivers,reciver_portion,detail]
        ### giver minus balance
        self.balance[giver] -= amount
        ### reciver add balance
        if recivers == None:
            for name in self.balance.keys():
                    self.balance[name] += amount/(self.members.__len__())
        elif reciver_portion == None:
            for name in recivers:
                self.balance[name] += amount/(recivers.__len__())
        else:
            for name,amt in zip(recivers,reciver_portion):
                self.balance[name] += amt
    def print_detail(self):
        print(self.detail)
    def print_curr_balance(self):
        print(self.balance)
    def close_account(self):
        giver_dic = {k:v for k,v in sorted(self.balance.items(),key = lambda item:item[1]) if v < 0}
        reciver_dic = {k:v for k,v in sorted(self.balance.items(),key = lambda item:item[1]) if v > 0}


def main():
    pass

if __name__ == '__main__':
    pass