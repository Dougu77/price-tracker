# Imports
import sys
import subprocess
from utils.messages import *

# Packages
packages = ['requests', 'beautifulsoup4', 'mysql-connector-python', 'pyodbc']

# Function
def install_packages():
    '''
    Install / Update packages
    '''    
    print(get_message('package_install'))
    try:
        for package in packages:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', package])
    except:
        print(get_message('error_package'))
    else:
        print(get_message('package_success'))
