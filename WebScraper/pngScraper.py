import requests
from bs4 import BeautifulSoup

site_map = 'http://www.pngmart.com/sitemap.xml'

response = requests.get(site_map)
xml = response.text
soup = BeautifulSoup(xml, 'xml')

site_maps = []
for loc in soup.find_all('loc'):
    url = loc.text
    if 'posts' in url:
        # print(url)
        site_maps.append(url)

site_map_1 = site_maps[0] # update to use all site maps to get all images
response = requests.get(site_map_1)
soup = BeautifulSoup(response.text, 'xml')

png_list = []
for loc in soup.find_all('loc'):
    url = loc.text
    if 'PNG' in url:
        png_list.append(url)

for image_url in png_list[0:5]:
    response = requests.get(image_url)
    image = requests.get(image_url)
    image_title = image_url.split('/')[-1]

    with open(image_title, 'wb') as file:
        file.write(image.content)

