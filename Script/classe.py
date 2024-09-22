import json

import csv

class Dados:
    
    def __init__(self,path, tipo_dados):
        self.path = path
        self.tipo_dados = tipo_dados
        self.dados = self.leitura_dados()
        self.qtd_dados = self.size_data()
        
        
    def leitura_json(self):
        dados_json = []
        with open(self.path, 'r') as file:
            dados_json = json.load(file)
        return dados_json
    
    def leitura_csv(self):
        dados= []
        with open(self.path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                dados.append(row)
        return dados
    
    
    def leitura_dados(self):
        dados = []
        
        
        if self.tipo_dados == 'json':
            dados = self.leitura_json()
        elif self.tipo_dados == 'csv':
            dados = self.leitura_csv()
            
        return dados    
        
        
    def size_data(self):
        return len(self.dados)
    
    def transforma_json_em_csv(self, path):
        dados_json = self.dados
        with open(path, mode='w', newline='') as file:
            writer = csv.writer(file)
            header = ["ID", "Name", "Email", "Address", "Purchase_History_1", "Purchase_History_2", "Purchase_History_3"]
            writer.writerow(header)
            for id_, details in dados_json.items():
                purchase_history = details.get("Purchase_History", [])
                row = [
                    id_,
                    details.get("Name"),
                    details.get("Email"),
                    details.get("Address"),
                    purchase_history[0] if len(purchase_history) > 0 else '',
                    purchase_history[1] if len(purchase_history) > 1 else '',
                    purchase_history[2] if len(purchase_history) > 2 else '',
                ]
                writer.writerow(row)
                
                
    def le_csv_transformado(self, path):
        dados_transformados = []
        with open(path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                dados_transformados.append(row)
        return dados_transformados
        
    
    def join_files(self, path_csv1, path_csv2, path_output):
        with open(path_csv1, 'r') as file1, open(path_csv2, 'r') as file2:
            csv1 = list(csv.DictReader(file1))
            csv2 = list(csv.DictReader(file2))
        
        merged_data = []
        for row1 in csv1:
            customer_id = row1['Customer_ID']
            for row2 in csv2[:50]:
                if row2['ID'] == customer_id:
                    merged_row = {**row1, **row2}
                    merged_data.append(merged_row)
                    break
        
        with open(path_output, 'w', newline='') as output_file:
            fieldnames = list(merged_data[0].keys())
            writer = csv.DictWriter(output_file, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(merged_data)
        
        print(f"Arquivo combinado salvo em {path_output}")