import requests
from bs4 import BeautifulSoup
import lxml
from archiver import *

#find links photos
def get_Links_photo(link):
    all_links =[]
    html = requests.get(link).text
    soup = BeautifulSoup(html,"lxml")
    for link in soup.find_all('img'):
        one = str(link.get('src'))
        if one != "None":
            all_links.append(f'{one}')
    print("All links saved!")
    return all_links
    
    
#save image       
def save_image(all_links,site_link):
    directory_new()
    name = 0
    for link in all_links:
        link = correct_link(link,site_link)
        image_bytes = requests.get(link).content
        with open(f'.\\images\\image{name}.png', 'wb') as file:
            file.write(image_bytes)
        name += 1
        print(f'Photo saved! - {link}')
    print("All photo saved!")

#if link not correct trying to do correct
def correct_link(link,site_link):
    clear_link = ('/'.join(site_link.split('/')[:3]))
    if "https" in link:
        return link
    else:
        link = str(clear_link) + str(link)
    return link







            