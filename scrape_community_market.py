import pandas as pd
import requests
import lxml.html as lh
import re

url = 'https://mlb19.theshownation.com/community_market?page=' + str(1) + '&type_id=0'

#Create a handle, page, to handle the contents of the website
page = requests.get(url)

#Store the contents of the website under doc
doc = lh.fromstring(page.content)

#Parse data that are stored between <tr>..</tr> of HTML
tr_elements = doc.xpath('//tr')

content_list = list()

for t in tr_elements[1:]:
    content = t.text_content().strip()
    content = re.sub('\n+', '\n', content).split('\n')
    print(tuple(content))