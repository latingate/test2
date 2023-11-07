import requests
from bs4 import BeautifulSoup

def add_numbers(x,y) -> int:
    return x+y

print (add_numbers(7,2.3))

request = requests.get('https://uppersite.com')
bs = BeautifulSoup(request.content, 'html.parser').prettify()
print (bs)
