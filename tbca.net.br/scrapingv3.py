import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib3.exceptions import InsecureRequestWarning
from time import sleep

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# def get_links(a):
    
#     links = []
#     setlinks = []
    
#     url = f"http://www.tbca.net.br/base-dados/composicao_alimentos.php?pagina={a}"
    
#     response = requests.get(url, verify=False)

#     soup = BeautifulSoup(response.text, 'html.parser')
    
#     alimentos = soup.find("tbody")
    
#     for items in alimentos.findAll("a"):
#         links.append(items.get("href"))
        
#     for items in links:
#         if "http://www.tbca.net.br/base-dados/" + items not in setlinks:
#             setlinks.append("http://www.tbca.net.br/base-dados/" + items)
     
#     return setlinks

# def fileLinks(a):
#     with open("links.txt", "w") as f:
#         for items in a:
#             f.write(items + '\n')
            
# fileLinks(get_links())

def counterSave(a):
    with open("contador.txt", "w") as f:
        f.write(str(a))

def getCounterSave():
    with open("contador.txt", "r") as f:
        cont = f.read()        
        return int(cont)    
    
def getLine(x):
    with open("links.txt", "r") as f:
        linha = f.readlines()
        return linha[x]
    
def getNumberLines():
    with open("alimentos.csv", "r", encoding="utf8") as f:
        num = len(f.readlines())
        return int(num)

def parser_Alimentos(url): 

    response = requests.get(url, verify=False)

    if response.status_code == 200:
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        nomeAlimento = soup.find("h5").text[27:300].strip()
        
        if ", << " in nomeAlimento:
            nomeAlimento = nomeAlimento.split(", << ", 2)[0]
        elif ", <<" in nomeAlimento:
            nomeAlimento = nomeAlimento.split(", <<", 2)[0]    
        elif ",  <<" in nomeAlimento:
            nomeAlimento = nomeAlimento.split(",  <<", 2)[0]
        elif ",  << " in nomeAlimento:
            nomeAlimento = nomeAlimento.split(",  << ", 2)[0]
        elif " << " in nomeAlimento:
            nomeAlimento = nomeAlimento.split(" << ", 2)[0]    
        elif "  << " in nomeAlimento:
            nomeAlimento = nomeAlimento.split("  << ", 2)[0]    

        table = soup.find('table')

        if table:

            rows = table.find_all('tr')

            desired_columns = ['Proteína', 'Lipídios', 'Carboidrato total', 'Colesterol', 'Fibra alimentar', 'Ácidos graxos saturados', 'Ácidos graxos trans', 'Sódio', 'Açúcar de adição']
            kcal = ['kcal']
            
            data_dict = {"Alimento, Amostra 100g": nomeAlimento,
                         'Valor energético (kcal)': '0',
                         'Proteína': '0',
                         'Lipídios': '0',
                         'Ácidos graxos saturados': '0',
                         'Ácidos graxos trans': '0',
                         'Carboidrato total': '0', 
                         'Fibra alimentar': '0',
                         'Açúcar': '0',
                         'Sódio': '0',
                         'Colesterol': '0'}
            
            for row in rows:
                cells = row.find_all('td')
                if len(cells) >= 3:  
                    column_name = cells[0].text.strip()
                    kcal_col_name = cells[1].text.strip()
                    if kcal_col_name in kcal:
                        value = cells[2].text.strip()
                        data_dict['Valor energético (kcal)'] = value
                    elif column_name in desired_columns:
                        value = cells[2].text.strip()
                        data_dict[column_name] = value
            return data_dict
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
              
        
def savecsv(result):
    try:
        dct = {k:[v] for k,v in result.items()} 
        df = pd.DataFrame(dct)
        df.to_csv("alimentos.csv", index=False, mode='a', header=False)
    except:
        pass
    
#print(parser_Alimentos("https://tabnut.dis.epm.br/alimento/05134/frango-capao-carne-pele-miudos-e-pescoco-cozido-assado"))

def main():   
    
    urls = getLine(getCounterSave()).strip()
    
    urlcount = getCounterSave()

    for i in range(urlcount, 5674):
        
        sleep(5)

        alimentos = parser_Alimentos(f"{urls}")
            
        numlinhas = getNumberLines()
            
        urls = getLine(getCounterSave()).strip()
            
        cont = numlinhas
            
        print(f"Total: {cont}")
            
        counterSave(cont)
            
        savecsv(alimentos)
            
if __name__ == '__main__':
    main()

