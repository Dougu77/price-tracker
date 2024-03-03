# Imports
import requests
from bs4 import BeautifulSoup
from utils.messages import *

# Functions
def request_url(url):
    '''
    Make the HTML request
    
    Args:
        url (str): URL of the product
        
    Returns:
        BeautifulSoup: HTML content of the URL
    '''
    try:
        response = requests.get(url)
        return BeautifulSoup(response.text, 'html.parser')
    except:
        print(get_message('error_request'))
        return None

def get_store(url):
    '''
    Get the store of product, to make the search
    
    Args:
        url (str): URL of the product

    Returns:
        str: First 5 letters of the store name
    '''
    index = url.find('www.') + 4
    return url[index:index + 5]

def get_price(url):
    '''
    Get the price of the product

    Args:
        url (str): URL of the product

    Returns:
        str: Price of the product
    '''
    # Get the required data
    html = request_url(url)
    store = get_store(url)
    price = None
    if store == 'kabum':
        # Find and format the price
        price = html.find(class_ = 'finalPrice')
        if price is not None: price = price.text[3:].replace('.', '').replace(',', '.')
    elif store == 'magaz':
        # Find and format the price
        price = html.find(class_ = 'sc-kpDqfm eCPtRw sc-bOhtcR dOwMgM')
        if price is not None: price = price.text[3:].replace('.', '').replace(',', '.')
    elif store == 'eneba':
        # Find and format the price
        price1 = html.find(class_ = 'L5ErLT dXrfjQ')
        price2 = html.find(class_ = 'TYs67U')
        if price1 is not None: price1 = price1.text[3:].replace('.', '').replace(',', '.')
        if price2 is not None: price2 = price2.text[3:].replace('.', '').replace(',', '.').replace('Preço mais baixo', '')
        if price1 is not None and price2 is None: price = price1
        elif price2 is not None and price1 is None: price = price2
        if price1 is not None and price2 is not None:
            if float(price1) > float(price2): price = price2
            else: price = price1
    else:
        print(get_message('error_store'))
    return price
