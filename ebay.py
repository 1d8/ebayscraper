from bs4 import BeautifulSoup
from requests import get

headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
dictionary = {}
search = input('Enter Search Term: ')
search = search.replace(' ', '+')

for i in range(1, 5):
    i = str(i)
    url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=' + search + '&_sacat=0&_pgn=' + i
    response = get(url, headers=headers)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    price = html_soup.find_all('span', class_='s-item__price')
    listingname = html_soup.find_all('h3', class_='s-item__title')
    shipping_info = html_soup.find_all('span', class_='s-item__shipping s-item__logisticsCost')
    image = html_soup.find_all('img', class_='s-item__image-img')
    
    for i in price:
        cost = price[0]
        cost = cost.text
        title = listingname[0]
        title = title.text
        shipping = shipping_info[0]
        shipping = shipping.text
        img = image[0]
        dictionary["Title:"] = title
        dictionary["Price:"] = cost
        dictionary["Shipping:"] = shipping
        dictionary["Image:"] = img
        for key, value in dictionary.items():
            print(key)
            print(value)
            print()
            listingname.pop(0)
            shipping_info.pop(0)
            price.pop(0)
            image.pop(0)
        
