# Import
from utils.get_datetime import get_date, get_time

# Variable
language = 'pt-br'

# Functions
def get_message(message):
    '''
    Get the message the system will print

    Args:
        message (str): Message required

    Returns:
        str: Message required, in the setted language
    '''
    if language == 'pt-br':
        messages = {
            'program_beginning': 'Iniciando o programa...\n',
            'error_request': 'Erro: Algo deu errado na hora de pesquisar na URL.',
            'error_store': 'Erro: Algo deu errado na hora de identificar a loja.',
            'error_date': 'Erro: Algo deu errado na hora de registrar a data.',
            'error_time': 'Erro: Algo deu errado na hora de registrar o horário.',
            'error_insert': 'Erro: Algo deu errado na hora de inserir os dados no Banco de Dados.',
            'line':  f'{"-" * 100}' + '\n'
        }
    elif language == 'en':
        messages = {
            'program_beginning': 'Starting the program...\n',
            'error_request': 'Error: Something went wrong when trying to use the URL.',
            'error_store': 'Error: Something went wrong when trying to identify the store.',
            'error_date': 'Error: Something went wrong when trying to register the date.',
            'error_time': 'Error: Something went wrong when trying to register the time.',
            'error_insert': 'Error: Something went wrong when trying to insert the data in the Database.',
            'line':  f'{"-" * 100}' + '\n'
        }
    return messages.get(message, '...')

def print_product_search_beginning(table):
    '''
    Print when the search of the current product in the list begins

    Args:
        table (str): SQL table of the product
    '''
    date = get_date()
    time = get_time()
    if language == 'pt-br':
        print(f'{date} - {time} -> Iniciando a busca dos dados de "{table}"')
    elif language == 'en':
        print(f'{date} - {time} -> Starting to search the data of "{table}"')

def print_product_search_ending(table):
    '''
    Print when the search of the current product in the list ends

    Args:
        table (str): SQL table of the product
    '''
    date = get_date()
    time = get_time()
    if language == 'pt-br':
        print(f'{date} - {time} -> Finalizando a busca dos dados de "{table}"')
    elif language == 'en':
        print(f'{date} - {time} -> Finishing to search the data of "{table}"')

def print_success_insert():
    '''
    Print when the data is inserted in the Database
    '''
    date = get_date()
    time = get_time()
    if language == 'pt-br':
        print(f'{date} - {time} -> Dados inseridos no Banco de Dados.\n')
    elif language == 'en':
        print(f'{date} - {time} -> The data was inserted in the Database.\n')
