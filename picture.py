import requests
from identity import create_name

def get_pp():
	url = 'https://thispersondoesnotexist.com/image'
	filename = f'{create_name()}.png'
	response = requests.get(url)

	with open(f'C:/Users/PC/Desktop/code/Projects/insta_bot/img/{filename}', 'wb') as f:
		f.write(response.content)





get_pp()