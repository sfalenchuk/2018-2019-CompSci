class Account:
	def__init__(self, balance):
		self.name = name
		self.balance = balance
		self.status = status

	def deposit(self, balance):
		status = ""
		if self.balance > 0:
			self.balance += amount
			status = self.name+ ("has now made a deposit of "amount" dollars!")
		else:
			status = self.name+ "can't do that"
		return status

	def withdraw(self, balance):
		status = ""
		if self.balance > 0:
			self.balance += amount
			status = self.name+ ("has now made a withdraw of "amount" dollars!")
		elif amount > balance:
			status = self.name+ "doesn't have enough money"
		else:
			status = self.name+ "can't do that"
		return status

	def stats(self):
		return "Name: "+self.name+" \nBalance: "+str(self.balance)

account = Account("accountname", 5)

while True:
	print(account1.stats())
	choice = input("Whatcha wanna do?")
		if choice is "deposit":
			amount = input("how many dollars?")
			print(account.deposit(amount))
		elif choice is "withdraw":
			amount = input("how many dollars?")
			print(account.withdraw(amount))
		else:
			print("Can't do that.")