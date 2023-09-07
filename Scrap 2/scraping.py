import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib3.exceptions import InsecureRequestWarning
from time import sleep

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def get_links(a):
    
    links = []
    setlinks = []
    
    url = f"http://www.tbca.net.br/base-dados/composicao_alimentos.php?pagina={a}"
    
    response = requests.get(url, verify=False)

    soup = BeautifulSoup(response.text, 'html.parser')
    
    alimentos = soup.find("tbody")
    
    for items in alimentos.findAll("a"):
        links.append(items.get("href"))
        
    for items in links:
        if "http://www.tbca.net.br/base-dados/" + items not in setlinks:
            setlinks.append("http://www.tbca.net.br/base-dados/" + items)
     
    return setlinks
        
def parser_Alimentos(a): 

    response = requests.get(a, verify=False)
    
    soup = BeautifulSoup(response.text, 'html.parser')

    nomeAlimento = soup.find("h5").text[25:250].strip()
    setNomeAlimento = nomeAlimento.split(", <<", 1)[0]
    setTNomeAlimento = nomeAlimento.split(",  <<", 1)[0]
    
    nutriAlimento = soup.find("tbody")
    
    nutri = []
    
    for items in nutriAlimento.findAll("td"):
        nutri.append(items.text)
    
    print(len(nutri))
    print(a)
    print(nutri)
              
    if len(nutri) == 111: #testado
        setKcal = nutri[5]
        setProt = nutri[17] 
        setLip = nutri[20]
        setCol= nutri[32]
        setCarb = nutri[11]
        setFibra = nutri[23]
    elif len(nutri) == 148: #testado
        setKcal = nutri[6]
        setProt = nutri[22] 
        setLip = nutri[26]
        setCol= nutri[42]
        setCarb = nutri[14]
        setFibra = nutri[30] 
    elif len(nutri) == 152: #testado
        setKcal = nutri[6]
        setProt = nutri[22] 
        setLip = nutri[26]
        setCol= nutri[42]
        setCarb = nutri[14]
        setFibra = nutri[30] 
    elif len(nutri) == 185: #testado
        setKcal = nutri[7]
        setProt = nutri[27] 
        setLip = nutri[32]
        setCol= nutri[52]
        setCarb = nutri[17]
        setFibra = nutri[37]
    elif len(nutri) == 190: #
        setKcal = nutri[7]
        setProt = nutri[27] 
        setLip = nutri[32]
        setCol= nutri[52]
        setCarb = nutri[17]
        setFibra = nutri[37]
    elif len(nutri) == 259: #testado
        setKcal = nutri[9]
        setProt = nutri[37] 
        setLip = nutri[44]
        setCol= nutri[72]
        setCarb = nutri[23]
        setFibra = nutri[51]
    elif len(nutri) == 296: #testado
        setKcal = nutri[10]
        setProt = nutri[42] 
        setLip = nutri[50]
        setCol= nutri[82]
        setCarb = nutri[26]
        setFibra = nutri[58]
    elif len(nutri) == 333: #9 #testado 
        setKcal = nutri[11] # 1
        setProt = nutri[47] # 5 
        setLip = nutri[56] # 6 
        setCol= nutri[92] # 10
        setCarb = nutri[29] # 3
        setFibra = nutri[65] # 7
    elif len(nutri) == 370: #10 #testado
        setKcal = nutri[12]
        setProt = nutri[52] 
        setLip = nutri[62]
        setCol= nutri[102]
        setCarb = nutri[32]
        setFibra = nutri[72] 
    elif len(nutri) == 444: #12 #testado
        setKcal = nutri[14]
        setProt = nutri[62] 
        setLip = nutri[74]
        setCol= nutri[122]
        setCarb = nutri[38]
        setFibra = nutri[86] 
    elif len(nutri) == 518: #14 #testado
        setKcal = nutri[16] 
        setProt = nutri[72]  
        setLip = nutri[86] 
        setCol= nutri[142]
        setCarb = nutri[44]
        setFibra = nutri[100]     

    result = {
        "Alimento, Amostra 100g": setTNomeAlimento,
        "Energia (kcal)": setKcal,
        "Proteina (g)": setProt,
        "Lipidios (g)": setLip,
        "Colesterol (mg)": setCol,
        "Carboidrato (g)": setCarb,
        "Fibra Alimentar (g)": setFibra
    }

    return result

def savecsv(result):
    dct = {k:[v] for k,v in result.items()} 
    df = pd.DataFrame(dct)
    df.to_csv("alimentos2.csv", index=False, header=False)
    
        
#print(parser_Alimentos("http://www.tbca.net.br/base-dados/int_composicao_alimentos.php?cod_produto=C0006K"))

def main():
    
        for x in range(1, 2):
            
            print(f"Pagina: {x}")

            urls = get_links(x)

            for url in urls:
        
                alimentos = parser_Alimentos(url)

                print(f"Total: {len(alimentos)}")

                savecsv(alimentos)


        
if __name__ == '__main__':
    main()
