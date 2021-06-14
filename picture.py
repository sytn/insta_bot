import requests
from identity import create_name

url = 'https://thispersondoesnotexist.com/image'
filename = f'{create_name()}.png'
response = requests.get(url)

with open(f'C:/Users/PC/Desktop/code/insta_bot/img/{filename}', 'wb') as f:
	f.write(response.content)






#file = open(filename, "wb")
#file.write(response.content)
#file.close()

# import requests
# from identity import create_name

# url = 'https://thispersondoesnotexist.com/image'

# filename = f'{create_name()}.png'
# r = requests.get(url, allow_redirects=True)
# open(filename, 'wb').write(r.content)