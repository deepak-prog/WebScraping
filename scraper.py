# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 18:31:55 2019

@author: ananthd
"""

import requests
from bs4 import BeautifulSoup
import re
import texttable as tt


url = 'https://www.amazon.ca/BOOST-Protein-Chocolate-Replacement-Shake/dp/B079LN55PD/ref=sr_1_13?crid=3GXY76BP73LAG&keywords=protein+shake&qid=1562363254&s=gateway&sprefix=prot%2Caps%2C218&sr=8-13'
#url = 'https://www.amazon.ca/Six-Star-Protein-Powder-Chocolate/dp/B06Y29T19Y/ref=sr_1_14?crid=3GXY76BP73LAG&keywords=protein+shake&qid=1562371091&s=gateway&sprefix=prot%2Caps%2C218&sr=8-14'
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
page = requests.get(url,headers =headers)
soup = BeautifulSoup(page.content,'html.parser')

title =soup.find(id= 'productTitle').text
title = title.strip()

price = price = soup.find(id = 'priceblock_ourprice').text
by = soup.find(id = 'bylineInfo').text

descr = soup.find(id = 'feature-bullets')
new_descr = descr.text
new_descr = re.sub(r"\s+", " ", new_descr)
isinstock = soup.find(id="availability").text
isinstock = isinstock.strip()

tab = tt.Texttable()
headings = ['Title','Is in Stock','Price','By','Description']
data = [title,isinstock,price,by,new_descr]
tab.header(headings)
tab.add_row(data)
s = tab.draw()
print(s)