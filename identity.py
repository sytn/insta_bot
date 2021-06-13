import random as rd

def create_name():
	with open('names.txt', encoding='utf-8') as f:
		lines = []
		for line in f:
			lines.append(line)

	lines = [line.replace(' ', '') for line in lines]
	name = f'{rd.choice(lines)}'.rstrip("\n").lower()
	return name


def create_surname():
	with open('surnames.txt', encoding='utf-8') as f2:
		lines2 = []
		for line2 in f2:
			lines2.append(line2)

	lines2 = [line2.replace(' ', '') for line2 in lines2]		
	surname = f'{rd.choice(lines2)}'.rstrip("\n").lower()
	return surname






# class Person:
# 	def __init__(self):
# 		#self.firstname = firstname
# 		#self.lastname = lastname
# 		pass


# 	def firstname(self):
# 		pass

fullname = f'{create_name()} {create_surname()}'
print(fullname)