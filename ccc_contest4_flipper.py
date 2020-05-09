line1 = [1, 2]
line2 = [3, 4]
temp = [0, 0]

flips = input()

for i in flips:
	temp = [0, 0]
	if i == 'H':
		temp = line1
		line1 = line2
		line2 = temp
	elif i == 'V':
		temp[0] = line1[0]
		temp[1] = line2[0]
		line1[0] = line1[1]
		line2[0] = line2[1]
		line1[1] = temp[0]
		line2[1] = temp[1]

for l1 in line1:
	print(l1, end = " ")
print("")

for l2 in line2:
	print(l2, end = " ")
print("")