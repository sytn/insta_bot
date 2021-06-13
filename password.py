import random as rd

with open('names.txt', encoding='utf-8') as f:
	lines = []
	for line in f:
		lines.append(line)



lines = [line.replace(' ', '') for line in lines]

print(rd.choice(lines).lower())