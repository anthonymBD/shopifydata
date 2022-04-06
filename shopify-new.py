import requests
import json
import pandas as pd

url = ''

r = requests.get(url)

data = r.json()

product_list = []

for item in data['products']:
    title = item['title']
    product_type = item['product_type']
    for image in item['images']:
        try:
          imgesrc = image['src']
        except:
          image = 'None'
    for variant in item['variants']:
        price = variant['price']
        available = variant ['available']

        product = {
            'title': title,
            'product_type': product_type,
            'price': price,
            'image': imgesrc,
            'available': available
        }
        product_list.append(product)

df = pd.DataFrame(product_list)

df.to_csv('testrun.csv')
print('saved to file')
