class Account:
	def __init__(self, balance, status, name):
		self.name = name
		self.balance = balance
		self.status = status

	def deposit(self, amount):
		status = ""
		if self.balance >= 0:
			self.balance += amount
			status = self.name+ (" has now made a deposit of "+str(amount)+" dollars!")
		else:
			status = self.name+ " can't do that"
		return status

	def withdraw(self, amount):
		status = ""
		if amount > balance:
			status = self.name+ " doesn't have enough money"
		elif self.balance > 0:
			self.balance -= amount
			status = self.name+ (" has now made a withdraw of "+str(amount)+" dollars!")
		else:
			status = self.name+ " can't do that"
		return status

	def stats(self):
		return "Name: "+self.name+" \nBalance: "+str(self.balance)

account = Account(5, "open", "Sasha")

while True:
	print(account.stats())
	choice = input("Whatcha wanna do?")
	if choice == "deposit":
		amount = int(input("how many dollars?"))
		print(account.deposit(amount))
	elif choice == "withdraw":
		amount = int(input("how many dollars?"))
		print(account.withdraw(amount))
	else:
		print("Can't do that.")