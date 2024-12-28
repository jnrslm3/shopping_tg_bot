import requests
from bs4 import BeautifulSoup

def get_page_links():
    base_url = "https://www.asos.com/men/new-in/cat/?cid=27110&page="
    links = []
    for page in range(1, 16):
        url = f"{base_url}{page}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}
        
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        product_links = soup.find_all('a', class_="productLink_KM4PI")
        
        for link in product_links:
            links.append(link['href'])
    
    return links

def get_product_info(links):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}
    
    products = []

    for url in links:
        full_url = url
        response = requests.get(full_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        

        product_name = soup.find('h1', class_="jcdpl")
        product_description = soup.find('h1', class_="jcdpl")
        product_sub_category = soup.find('div', class_="F_yfF").find('strong') 
        product_image = soup.find_all("img", class_="gallery-image")
        for i in product_image:
            p_image = i.get('src')
            print(p_image)

        p_name = product_name.text.strip()
        p_description = product_description.text.strip()
        p_sub_category = product_sub_category.text.strip()
        p_url = full_url
        
        

    # product.append({
    #     'name': product_name,
    #     'description': product_description,
    #     'price': 55,
    #     'image'::
    #     'materials':
    #     'category':
    #     'sub_category':
    #     'url':
    # })


if __name__ == "__main__":
    links = get_page_links()
    get_product_info(links)
