lines = int(input())

inp = []

for i in range(0, lines):
	temp = input()
	inp.append(temp)

for j in range(0, lines):
	line = inp[j]
	char = ''
	char1 = line[0]
	noofchars = 0
	for k in range(0, len(line)):
		char = line[k]
		if char == char1:
			noofchars += 1
		else:
			print(noofchars, end = "")
			print(char1, end = "")
			noofchars = 1
			char1 = char

		if k == len(line) - 1:
			print(noofchars, end = "")
			print(char1, end = "")
	print("")