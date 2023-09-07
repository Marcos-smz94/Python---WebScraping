import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib3.exceptions import InsecureRequestWarning
from time import sleep

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def get_links():

    links = []
    setlinks = []
   
    url = f"https://tabnut.dis.epm.br/Alimento"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    
    alimentos = soup.find("tbody")
    
    for items in alimentos.findAll("a"):
        links.append(items.get("href"))
        
    for items in links:
        if "https://tabnut.dis.epm.br" + items not in setlinks:
            setlinks.append("https://tabnut.dis.epm.br" + items)
     
    return setlinks

def fileLinks(a):
    with open("links.txt", "w") as f:
        for items in a:
            f.write(items + '\n')
            
#fileLinks(get_links())

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

    for i in range(urlcount, 3677):
        
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

