import requests
from bs4 import BeautifulSoup
import re

url = "https://www.sio.no/mat-og-drikke/spisesteder-og-kaffebarer"
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'}
request = requests.get(url,headers=header)
soup = BeautifulSoup(request.text, 'html.parser')    
text = soup.find('div',id="jump284")
# print(text)
regex = 'h4>Dagens</h4><ul class=\"dinner\"><li>(.*?)</li>'
m = re.findall(regex, str(text))
print(m[0])
