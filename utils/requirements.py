# Imports
import sys
import subprocess
from utils.messages import *

# Function
def install_packages():
    '''
    Install / Update packages
    '''    
    print(get_message('package_install'))
    try:
        subprocess.check_call(['pip', 'install', '-q', '-r', 'requirements.txt'])
    except:
        print(get_message('error_package'))
    else:
        print(get_message('package_success'))
