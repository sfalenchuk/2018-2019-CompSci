class Bear:
	def__init__(self, name, hunger, energy, tiredness):
		self.hunger = hunger
		self.energy = energy
		self.name = name
		self.tiredness = tiredness

	def eat(self, amount):
		status = ""
		if self.hunger > 0:
			self.tiredness -= amount
			self.energy += amount
			status = self.name+ "just rested!"
		else:
			status = self.name+ "refused to sleep."
		return status

	def eat(self, amount):
		status = ""
		if self.hunger > 0:
			self.hunger -= amount
			self.energy += amount
			status = self.name+ "just ate!"
		else:
			status = self.name+ "refused to eat."
		return status

	def stats(self):
		return "Name: "+self.name+" \nEnergy: "+str(self.energy)+"\nHunger: "+str(self.hunger)

bearname = input("Whay do you want to name your doga?")
bear1 = Bear("Bro", 0, 5)
bear1 = Bear("bearname", 5, 3)

while True:
	print(bear1.stats())
	print(bear2.stats())
	choice = input("Whatcha wanna do?")
		if choice is "eat":
			print(bear1.eat(2))
			print(bear2.eat(2))
		else:
			print("Can't do that.")

