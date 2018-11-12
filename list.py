import random

a = []

print(a)

a.append(5)
a.append(3)
a.append(8)
a.append(8)

print(a)

a += [1,2,3,4,5] + a

print(a)

#a.insert(0,5)

#remove from list

del a[5]
print(a.pop())

print(a)

print(len(a))

#remove random from list

x = random.randint(len(a)-1)
del a[x]
print(a)

print(a[-1])

y,z = 5,10
y,z = z,y
print(y,z)

a[0], a[-1] = a[-1], a[0]

print(a)

for i in range(2,10,2):
	print(i)