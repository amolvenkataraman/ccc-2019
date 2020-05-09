lines = int(input())

temp1 = []
number = []
character = []

for i in range(1, lines + 1):
	temp = input()
	temp1 = temp.split()
	number.append(int(temp1[0]))
	character.append(temp1[1])

for j in range(0, lines):
	for k in range(0, number[j]):
		print(character[j], end = "")
	print("")