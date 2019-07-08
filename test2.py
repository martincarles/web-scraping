import sys
import requests
import locale
from bs4 import BeautifulSoup

# For extracting the price from amazon.fr urls
locale.setlocale(locale.LC_ALL, 'fr_FR.UTF8')
conv = locale.localeconv()

def grabPrice(soup):
    price = soup.find(id="priceblock_ourprice").get_text().strip(conv['currency_symbol'].decode('utf-8'))
    return price.replace(',', '.')

baseurl = 'https://www.amazon.fr/Nintendo-0045496420888-Super-Mario-Odyssey/dp/B072KJWYL9/ref=pd_cart_bmx_2_4/257-8065545-6131911?_encoding=UTF8&pd_rd_i=B072KJWYL9&pd_rd_r=dcd8efc8-621d-4a3a-93de-08e3dab64f39&pd_rd_w=oLl0G&pd_rd_wg=r7ubY&pf_rd_p=f8312a30-6d14-46e9-924d-e020f0329168&pf_rd_r=ZD2HX75F166M3R1Q27P0&psc=1&refRID=ZD2HX75F166M3R1Q27P0'

# If a url is provided use it, otherwise use the default one
url = sys.argv[1] if len(sys.argv) > 1 else baseurl

page = requests.get(url)

# Parse the html content
soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle").get_text()
price = grabPrice(soup)

print 'Produit:', title.strip()
print 'Prix:', price, 'Euros'
