# Rastreador de Preço

- O programa rastreia e armazena os preços de produtos em sites, em um Banco de Dados, dentro de intervalos regulares.
- Sites suportados: [Kabum](https://www.kabum.com.br/), [Magazine Luiza](https://www.magazineluiza.com.br/) e [Eneba](https://www.eneba.com/br/).
- Bancos de Dados suportados: [MySQL](https://www.mysql.com/) e [SQL Server](https://www.microsoft.com/pt-br/sql-server/sql-server-downloads).
- Crie o Banco de Dados seguindo o modelo em [create_db](https://github.com/Dougu77/price-tracker/blob/main/sql/create_db.sql).
- Crie uma tabela para cada produto, seguindo o modelo em [create_table](https://github.com/Dougu77/price-tracker/blob/main/sql/create_table.sql).
- Modifique a variável "language" em [messages](https://github.com/Dougu77/price-tracker/blob/main/utils/messages.py) para escolher o idioma desejado: pt-br ou en.
- Modifique as informações necessárias em [sql_connection](https://github.com/Dougu77/price-tracker/blob/main/utils/sql_connection.py) para acessar o seu Banco de Dados.
- Modifique o intervalo entre uma pesquisa e outra em "sleep", na [main](https://github.com/Dougu77/price-tracker/blob/main/main.py).
- Modifique a lista de produtos a ser pesquisada em [products](https://github.com/Dougu77/price-tracker/blob/main/utils/products.py), seguindo o modelo dos itens já presentes.

# Price Tracker

- The program tracks and stores the prices of products from e-commerces, in a Database, following a regular interval.
- Supported websites: [Kabum](https://www.kabum.com.br/), [Magazine Luiza](https://www.magazineluiza.com.br/) and [Eneba](https://www.eneba.com).
- Supported Databases: [MySQL](https://www.mysql.com/) and [SQL Server](https://www.microsoft.com/pt-br/sql-server/sql-server-downloads).
- Create a Database using [create_db](https://github.com/Dougu77/price-tracker/blob/main/sql/create_db.sql).
- Create a table for each product, using [create_table](https://github.com/Dougu77/price-tracker/blob/main/sql/create_table.sql).
- Modify the variable "language" in [messages](https://github.com/Dougu77/price-tracker/blob/main/utils/messages.py) to choose the desired language: en or pt-br.
- Modify the necessary informations in [sql_connection](https://github.com/Dougu77/price-tracker/blob/main/utils/sql_connection.py) to connect to your Database.
- Modify the interval between one search and another using "sleep", in [main](https://github.com/Dougu77/price-tracker/blob/main/main.py).
- Modify the list of products to be searched in [products](https://github.com/Dougu77/price-tracker/blob/main/utils/products.py), following the examples already there.
