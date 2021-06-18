#https://stackoverflow.com/questions/2659312/how-do-i-convert-a-numpy-array-to-and-display-an-image
import random as rd
from username import create_username
from password import create_pass

def create_name():
	with open(r'C:\Users\PC\Desktop\code\Projects\insta_bot\txtFiles\names.txt', encoding='utf-8') as f:
		lines = []
		for line in f:
			lines.append(line)

	lines = [line.replace(' ', '') for line in lines]
	name = f'{rd.choice(lines)}'.rstrip("\n").lower()
	return name


def create_surname():
	with open(r'C:\Users\PC\Desktop\code\Projects\insta_bot\txtFiles\surnames.txt', encoding='utf-8') as f2:
		lines2 = []
		for line2 in f2:
			lines2.append(line2)

	lines2 = [line2.replace(' ', '') for line2 in lines2]		
	surname = f'{rd.choice(lines2)}'.rstrip("\n").lower()
	return surname



def fullName(name=create_name(), surname=create_surname()):
	return f'{name} {surname}'



person = {
	"firstname": create_name(),
	"surname": create_surname(),
	"username": create_username(),
	"password": create_pass()
}

"""
ToDo:
1) Store user information on firebase
2) Convert profile picture to numpy arrays and convert them back to img then display
3) List all stored data from firebase
"""

