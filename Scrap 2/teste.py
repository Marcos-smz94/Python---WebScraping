
import requests
from bs4 import BeautifulSoup
import csv

url = 'https://tabnut.dis.epm.br/alimento/14120/bebida-alcoolica-vinho-de-mesa-branco-muller-thurgau'

def parser_Alimentos(url): 

    response = requests.get(url, verify=False)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        table = soup.find('table')

        if table:
            rows = table.find_all('tr')

            desired_columns = ['Valor energético (kcal)', 'Proteína', 'Gorduras totais',
                            'Carboidratos (por diferença)', 'Colesterol', 'Fibra alimentar']
            

            data_dict = {}

           
            for row in rows:
                cells = row.find_all('td')
                if len(cells) >= 3:  
                    column_name = cells[0].text.strip()
                    if column_name in desired_columns:
                        value = cells[2].text.strip()
                        data_dict[column_name] = value
            return data_dict
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
            
            
