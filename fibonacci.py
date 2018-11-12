

import sys

def commandCall(argNum):
	return sys.argv[int(argNum)]

userNum = int(commandCall(1))
fibList = [1,1]

for i in range(0, userNum):
	c = fibList[-1] + fibList[-2]
	fibList.append(c)
end = userNum - 1
print(fiblist.pop(end))