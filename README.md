# **Projeto Pipeline de Dados**

Este repositório contém um projeto de pipeline de dados com o objetivo de **extrair, transformar e carregar** (ETL) dados provenientes de dois formatos diferentes: **JSON** e **CSV**. O projeto foi desenvolvido como parte de um exercício prático sugerido pelo **ChatGPT**, com bases de dados fictícias geradas pelo modelo. Foi uma ótima maneira de praticar habilidades de manipulação de dados e construção de pipelines eficientes.

## **Estrutura do Projeto**

A organização do projeto é a seguinte:

📦 Projeto Pipeline de Dados ┣ 📂 data_raw ┃ ┣ 📄 customers_data.json ┃ ┣ 📄 sales_data.csv ┣ 📂 data_processed ┃ ┣ 📄 merged_Data.csv ┣ 📂 notebooks ┃ ┣ 📄 pipeline_etl.ipynb ┣ 📂 scripts ┃ ┣ 📄 classe.py ┃ ┣ 📄 teste.py ┗ 


- **data_raw**: Contém os dados brutos fornecidos sem manipulação (JSON e CSV).
- **data_processed**: Armazena o arquivo final com os dados limpos e combinados.
- **notebooks**: Contém o código em Jupyter Notebook com todo o processo de ETL.
- **scripts**: Contém o código organizado no formato de classes e os testes.

## **Tecnologias Utilizadas**

- Python
- Jupyter Notebook
- Manipulação de arquivos JSON e CSV
- Manipulação e transformação de dados

## **Execução do Projeto**

### **1. Extração dos Dados**

No primeiro passo, os dados são extraídos de dois arquivos: um JSON com informações de clientes e um CSV contendo dados de vendas.


### **2. Transformação dos Dados**

Após a extração, o arquivo JSON é convertido em CSV para facilitar a junção com os dados de vendas.


### **3.Carga e Junção dos Dados**

Por fim, os dois arquivos CSV são unidos em um único arquivo, contendo todas as informações relevantes, como o histórico de compras dos clientes e suas respectivas vendas.



### **Arquivo Classe.py**

Este arquivo contém a lógica principal da classe Dados, que implementa os métodos de leitura, transformação e junção dos dados.


### **Arquivo Teste.py**

O arquivo teste.py contém a execução dos testes para validar o pipeline de ETL.

### **Conclusão**

Este projeto de pipeline de dados foi uma excelente oportunidade para consolidar conhecimentos em ETL, utilizando Python para manipulação de arquivos JSON e CSV, e boas práticas na criação de scripts reutilizáveis e organização do código.
