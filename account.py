class Account:
	def __init__(self,firstname,lastname,balance):
		self.firstname=firstname
		self.lastname=lastname
		self.balance=balance
	def welcome(self):
		return "Dear {} {},welcome,your balance is {}".format(self.firstname,self.lastname,self.balance)
	def deposit(self,x):
		self.balance=self.balance+x
		return "Hello {} {},your balance is {}".format(self.firstname,self.lastname,x)
	def withdraw(self,y):
		self.balance=self.balance-y
		return "Dear {} {},you have withdrawn {}".format(self.firstname,self.lastname,y)
	def showbalance(self):
		showbalance=self.showbalance
		return "Hello {} {},current balance is {}".format(self.firstname,self.lastname,self.balance)
		
		