from classe import Dados

path_json = r"C:\Users\gusta\OneDrive\Área de Trabalho\Portfólio Programação\Projeto do pai de pipeline\data_raw\customers_data.json"

path_csv = r"C:\Users\gusta\OneDrive\Área de Trabalho\Portfólio Programação\Projeto do pai de pipeline\data_raw\sales_data.csv"

path_json_transformado = r"C:\Users\gusta\OneDrive\Área de Trabalho\Portfólio Programação\Projeto do pai de pipeline\data_raw\customers_data.csv"

path_output = r"C:\Users\gusta\OneDrive\Área de Trabalho\Portfólio Programação\Projeto do pai de pipeline\data_processed\merged_Data.csv"

#Extract

dadosA = Dados(path_json, 'json')

dadosB = Dados(path_csv, 'csv')

print(dadosA.qtd_dados)
print(dadosB.qtd_dados)


#Transform



dadosA.transforma_json_em_csv(path_json_transformado)

novos_dadosA =dadosA.le_csv_transformado(path_json_transformado)

#Load

dadosA.join_files(path_csv, path_json_transformado, path_output)




