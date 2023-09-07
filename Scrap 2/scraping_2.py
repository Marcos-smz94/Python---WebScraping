import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib3.exceptions import InsecureRequestWarning
from time import sleep

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

lennutri = []

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

def parser_Alimentos(a): 
    
    nomeAlimento = soup.find("h2").text[18:]


    response = requests.get(a, verify=False)
    
    soup = BeautifulSoup(response.text, 'html.parser')


    nutriAlimento = soup.find("tbody")
    
    nutri = []
    

    
    for items in nutriAlimento.findAll("td"):
        nutri.append(items.text)
        
    lennutri.append(len(nutri))
    
    # print(len(nutri))
    # print(a)
    # print(nutri)
    
    try:
        if len(nutri) == 65:  # testado
            setKcal = nutri[8]
            setProt = nutri[13] 
            setLip = nutri[18]
            setCarb = nutri[23]
            setFibra = nutri[28]
            setCol= nutri[63]
        elif len(nutri) == 70:  # testado
            setKcal = nutri[8]
            setProt = nutri[13] 
            setLip = nutri[18]
            setCarb = nutri[23]
            setFibra = nutri[28]
            setCol= nutri[68]    
        elif len(nutri) == 75:  # testado
            setKcal = nutri[8]
            setProt = nutri[13] 
            setLip = nutri[18]
            setCarb = nutri[23]
            setFibra = nutri[28]
            setCol= nutri[73]    
        elif len(nutri) == 80:  # testado
            setKcal = nutri[8]
            setProt = nutri[13] 
            setLip = nutri[18]
            setCarb = nutri[23]
            setFibra = nutri[28]
            setCol= nutri[78]
        elif len(nutri) == 85:  # testado
            setKcal = nutri[8]
            setProt = nutri[13] 
            setLip = nutri[18]
            setCarb = nutri[23]
            setFibra = nutri[28]
            setCol= nutri[83]
        elif len(nutri) == 90:  # testado
            setKcal = nutri[8]
            setProt = nutri[13] 
            setLip = nutri[18]
            setCarb = nutri[23]
            setFibra = nutri[28]
            setCol= nutri[88]
        elif len(nutri) == 95:  # testado
            setKcal = nutri[8]
            setProt = nutri[13] 
            setLip = nutri[18]
            setCarb = nutri[23]
            setFibra = nutri[28]
            setCol= "*"
        elif len(nutri) == 105:  # testado
            setKcal = nutri[8]
            setProt = nutri[13] 
            setLip = nutri[18]
            setCarb = nutri[23]
            setFibra = nutri[28]
            setCol= "*"
        elif len(nutri) == 114:  # testado
            setKcal = nutri[9]
            setProt = nutri[15] 
            setLip = nutri[21]
            setCarb = nutri[27]
            setFibra = nutri[33]
            setCol = nutri[111]     
        elif len(nutri) == 119:  # testado
            setKcal = nutri[10]
            setProt = nutri[17] 
            setLip = nutri[24]
            setCarb = nutri[31]
            setFibra = nutri[38]
            setCol = "*"  
        elif len(nutri) == 120: # testado
            setKcal = nutri[8]
            setProt = nutri[13] 
            setLip = nutri[18]
            setCarb = nutri[23]
            setFibra = nutri[28]
            setCol = nutri[118]       
        elif len(nutri) == 126:  # testado
            setKcal = nutri[9]
            setProt = nutri[15] 
            setLip = nutri[21]
            setCarb = nutri[27]
            setFibra = "*"
            setCol = "*"    
        elif len(nutri) == 130:  # testado
            setKcal = nutri[8]
            setProt = nutri[13] 
            setLip = nutri[18]
            setCarb = nutri[23]
            setFibra = nutri[28]
            setCol= nutri[128]
        elif len(nutri) == 132: # testado
            setKcal = nutri[9]
            setProt = nutri[15] 
            setLip = nutri[21]
            setCarb = nutri[27]
            setFibra = nutri[33]
            setCol= "*"    
        elif len(nutri) == 138: # testado
            setKcal = nutri[9]
            setProt = nutri[15] 
            setLip = nutri[21]
            setCarb = nutri[27]
            setFibra = nutri[33]
            setCol= "*" 
        elif len(nutri) == 140:  # testado
            setKcal = nutri[8]
            setProt = nutri[13] 
            setLip = nutri[18]
            setCarb = nutri[23]
            setFibra = nutri[28]
            setCol= nutri[173]
        elif len(nutri) == 144: # testado
            setKcal = nutri[9]
            setProt = nutri[15] 
            setLip = nutri[21]
            setCarb = nutri[27]
            setFibra = nutri[33]
            setCol= nutri[141]    
        elif len(nutri) == 150: # testado
            setKcal = nutri[8]
            setProt = nutri[13] 
            setLip = nutri[18]
            setCarb = nutri[23]
            setFibra = nutri[28]
            setCol= nutri[143]
        elif len(nutri) == 156: # testado 
            setKcal = nutri[9]
            setProt = nutri[15] 
            setLip = nutri[21]
            setCarb = nutri[27]
            setFibra = nutri[33]
            setCol= nutri[153]
        elif len(nutri) == 160: # testado 
            setKcal = nutri[8]
            setProt = nutri[13] 
            setLip = nutri[18]
            setCarb = nutri[23]
            setFibra = nutri[28]
            setCol= nutri[153]
        elif len(nutri) == 162: # testado
            setKcal = nutri[9]
            setProt = nutri[15] 
            setLip = nutri[21]
            setCarb = nutri[27]
            setFibra = nutri[33]
            setCol= nutri[159]
        elif len(nutri) == 168: # testado 
            setKcal = nutri[9]
            setProt = nutri[15] 
            setLip = nutri[21]
            setCarb = nutri[27]
            setFibra = nutri[33]
            setCol= nutri[165]
        elif len(nutri) == 174: # testado 
            setKcal = nutri[9]
            setProt = nutri[15] 
            setLip = nutri[21]
            setCarb = nutri[27]
            setFibra = nutri[33]
            setCol= nutri[171]
        elif len(nutri) == 175: # testado
            setKcal = nutri[10]
            setProt = nutri[17] 
            setLip = nutri[24]
            setCarb = nutri[31]
            setFibra = nutri[38]
            setCol= nutri[171]
        elif len(nutri) == 180: # testado 
            setKcal = nutri[9]
            setProt = nutri[15] 
            setLip = nutri[21]
            setCarb = nutri[27]
            setFibra = nutri[33]
            setCol= nutri[171]
        elif len(nutri) == 182: # testado 
            setKcal = nutri[10]
            setProt = nutri[17] 
            setLip = nutri[24]
            setCarb = nutri[31]
            setFibra = nutri[38]
            setCol= nutri[178]    
        elif len(nutri) == 186: # testado 
            setKcal = nutri[9]
            setProt = nutri[15] 
            setLip = nutri[21]
            setCarb = nutri[27]
            setFibra = nutri[33]
            setCol= nutri[177]    
        elif len(nutri) == 192: # testado 
            setKcal = nutri[9]
            setProt = nutri[15] 
            setLip = nutri[21]
            setCarb = nutri[27]
            setFibra = nutri[33]
            setCol= nutri[183]
        elif len(nutri) == 196: # testado 
            setKcal = nutri[10]
            setProt = nutri[17] # 2
            setLip = nutri[24] # 3
            setCarb = nutri[31] # 4
            setFibra = nutri[38] # 5
            setCol= nutri[185] # 30  
        elif len(nutri) == 203: # testado 
            setKcal = nutri[10]
            setProt = nutri[17] # 2
            setLip = nutri[24] # 3
            setCarb = nutri[31] # 4
            setFibra = nutri[38] # 5
            setCol= nutri[192] # 30
        elif len(nutri) == 210: # testado 
            setKcal = nutri[10]
            setProt = nutri[17] # 2
            setLip = nutri[24] # 3
            setCarb = nutri[31] # 4
            setFibra = nutri[38] # 5
            setCol= nutri[199] # 30
        elif len(nutri) == 224: # testado
            setKcal = nutri[10] # 1
            setProt = nutri[17] # 2
            setLip = nutri[24] # 3
            setCarb = nutri[31] # 4
            setFibra = nutri[38] # 5
            setCol= nutri[213] # 30
        elif len(nutri) == 232: # testado
            setKcal = nutri[11]
            setProt = nutri[19] 
            setLip = nutri[27]
            setCarb = nutri[35]
            setFibra = nutri[43]
            setCol= nutri[219]    
        elif len(nutri) == 256: # testado
            setKcal = nutri[11]
            setProt = nutri[19] 
            setLip = nutri[27]
            setCarb = nutri[35]
            setFibra = nutri[43]
            setCol= nutri[243]
        elif len(nutri) == 288: # testado
            setKcal = nutri[12] # 1
            setProt = nutri[21] # 2
            setLip = nutri[30] # 3
            setCarb = nutri[39] # 4
            setFibra = nutri[48] # 5
            setCol= nutri[273] # 30
        elif len(nutri) == 320: # testado
            setKcal = nutri[13]
            setProt = nutri[23] 
            setLip = nutri[33]
            setCarb = nutri[43]
            setFibra = nutri[53]
            setCol= nutri[303]
        elif len(nutri) == 352: # testado
            setKcal = nutri[14]
            setProt = nutri[25] 
            setLip = nutri[36]
            setCarb = nutri[47]
            setFibra = nutri[58]
            setCol= nutri[333]
        elif len(nutri) == 384: # testado
            setKcal = nutri[15]
            setProt = nutri[27] 
            setLip = nutri[39]
            setCarb = nutri[51]
            setFibra = nutri[63]
            setCol= nutri[363]
        elif len(nutri) == 416: # testado
            setKcal = nutri[16]
            setProt = nutri[29] 
            setLip = nutri[42]
            setCarb = nutri[55]
            setFibra = nutri[68]
            setCol= nutri[393]
        elif len(nutri) == 448: # testado
            setKcal = nutri[17]
            setProt = nutri[31] 
            setLip = nutri[45]
            setCarb = nutri[59]
            setFibra = nutri[73]
            setCol= nutri[423]
        elif len(nutri) == 480: # testado
            setKcal = nutri[18]
            setProt = nutri[33] 
            setLip = nutri[48]
            setCarb = nutri[63]
            setFibra = nutri[78]
            setCol= nutri[453]
            
        result = {
            "Alimento, Amostra 100g": nomeAlimento,
            "Energia (kcal)": setKcal,
            "Proteina (g)": setProt,
            "Lipidios (g)": setLip,
            "Colesterol (mg)": setCol,
            "Carboidrato (g)": setCarb,
            "Fibra Alimentar (g)": setFibra
        }

        return result
    
    except (UnboundLocalError, IndexError):
            with open("erros.txt", "a") as f:
                f.write(f"{lennutri[-1]}, {a.strip()}" + '\n')
            with open("alimentos.csv", "a") as f:
                f.write("Erro" + '\n')
        
        
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

    for i in range(urlcount, 3676):
        
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

