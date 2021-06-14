import random as rd

def create_name():
	with open(r'C:\Users\PC\Desktop\code\insta_bot\txtFiles\names.txt', encoding='utf-8') as f:
		lines = []
		for line in f:
			lines.append(line)

	lines = [line.replace(' ', '') for line in lines]
	name = f'{rd.choice(lines)}'.rstrip("\n").lower()
	return name


def create_surname():
	with open(r'C:\Users\PC\Desktop\code\insta_bot\txtFiles\surnames.txt', encoding='utf-8') as f2:
		lines2 = []
		for line2 in f2:
			lines2.append(line2)

	lines2 = [line2.replace(' ', '') for line2 in lines2]		
	surname = f'{rd.choice(lines2)}'.rstrip("\n").lower()
	return surname



def fullName(name=create_name(), surname=create_surname()):
	return f'{name} {surname}'


print(fullName())