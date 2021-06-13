import requests
from identity import create_name

url = 'https://thispersondoesnotexist.com/'

filename = f'{create_name()}.png'
r = requests.get(url, allow_redirects=True)
open(filename, 'wb').write(r.content)