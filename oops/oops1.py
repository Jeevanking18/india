class BankAccount:
    def __init__(self,AccountNo,AccountName,AccountBalance,Branch):
        self.AccountNo=AccountNo
        self.AccountName=AccountName
        self.AccountBalance=AccountBalance
        self.Branch=Branch
    def display(self):
        print(self.AccountBalance,self.AccountName,self.AccountNo,self.Branch)
    def diposit(self,amount):
        self.AccountBalance = self.AccountBalance + amount
    def withdraw(self,amount):
        self.AccountBalance= self.AccountBalance -  amount    
    def CheckBalance(self):
        print(self.AccountBalance)       
        
obj1=BankAccount(1234567,"jeevan",10000,"kotharoad")
obj2=BankAccount(6327728,"sirisha",20000,"vzm")

obj1.display()        
obj2.display()
obj1.diposit(40000)
bal=obj1.CheckBalance()
print(f"Jeevan you have balance in your account is {bal}")
       