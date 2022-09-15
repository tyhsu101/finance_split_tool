import pandas as pd

class split_wise:
    def __init__(self,members:tuple) -> None:
        self.members = members
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
        text = ''
        giver_dic = {k:v for k,v in sorted(self.balance.items(),key = lambda item:item[1]) if v < 0}
        reciver_dic = {k:v for k,v in sorted(self.balance.items(),key = lambda item:item[1],reverse=True) if v > 0}
        rec_key = list(reciver_dic.keys())
        ind_n = 0
        temp_doller = 0
        for i,x in zip(giver_dic.keys(),giver_dic.values()):
            ttl_accnt = 0
            if temp_doller != 0:
                if temp_doller + x < 0:
                    text = text + str(rec_key[ind_n]) + " should give " + str(i) +' '+ str(temp_doller) + 'dollar.\n' 
                    ttl_accnt += temp_doller
                    temp_doller = 0
                    ind_n += 1
                else:
                    text = text + str(rec_key[ind_n]) + " should give " + str(i) + ' '+ str(x) + 'dollar.\n'
                    temp_doller += x
                    continue
            while ttl_accnt + reciver_dic[rec_key[ind_n]] + x < 0:
                text = text + str(rec_key[ind_n]) + " should give " + str(i) +' '+ str(reciver_dic[rec_key[ind_n]]) + 'dollar.\n'
                ttl_accnt += reciver_dic[rec_key[ind_n]]
                ind_n += 1
            if ttl_accnt + x < 0:
                text = text + str(rec_key[ind_n]) + " should give " + str(i) + ' ' + str(0 - (ttl_accnt + x)) + 'dollar.\n'
                temp_doller = ttl_accnt + reciver_dic[rec_key[ind_n]] + x
            elif ttl_accnt + x == 0:
                ind_n += 1
        return text

def main():
    pass

if __name__ == '__main__':
    pass