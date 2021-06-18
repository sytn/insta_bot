import random as rd


with open(r'C:\Users\PC\Desktop\code\Projects\insta_bot\txtFiles\names.txt', encoding='utf-8') as f:
	lines = []
	for line in f:
		lines.append(line)



lines = [line.replace(' ', '') for line in lines]





def create_username(x=lines):
	#username = f"{rd.choice(x)+str(rd.randint(0, 10))+str(rd.randint(0, 10))+str(rd.randint(0, 10))+str(rd.randint(0, 10))}"
	username = f'{rd.choice(x)}'.rstrip("\n")
	username = username  + f'{rd.randint(0, 10)}'  + f'{rd.randint(0, 10)}'  + f'{rd.randint(0, 10)}'
	return username.lower()



