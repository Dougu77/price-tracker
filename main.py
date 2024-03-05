# Import install_packages()
from utils.requirements import *

# Install / Update packages
install_packages()

# Imports
from utils.get_datetime import *
from utils.http_request import *
from utils.messages import *
from utils.products import *
from utils.sql_connection import *
from time import sleep

# System message
print(get_message('program_beginning'))

# System message
print(get_message('line'))

# Make the program runs constantly
while True:
    
    # Make the search in every element in the products list
    for product in products:
        
        # System message
        print_product_search_beginning(product['table'])
        
        # Get the necessary data to insert in the Database
        price = get_price(product['url'])
        date = get_date()
        time = get_time()
                
        # System message
        print_product_search_ending(product['table'])
        
        # Insert the data in the Database
        insert_info(product['table'], price, date, time)
        
        # System message
        print_success_insert()
    
    # System message
    print(get_message('line'))
    
    # Interval between each search of all products (seconds)
    sleep(60 * 30)
