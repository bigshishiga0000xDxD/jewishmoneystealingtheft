import requests
from bs4 import BeautifulSoup

link = input('HTTP link to the site you want to hack.\n')
output_file = input('Name of the output .html file.\n')

resp = requests.get(link)
if resp.status_code != 200:
    raise RuntimeError('Website is not available at the moment')

page = resp.text
soup = BeautifulSoup(page, 'html.parser')

with open(output_file, mode='w') as f:
    for x in soup.find_all('p'):
        print(x, file=f)

print('Done!')