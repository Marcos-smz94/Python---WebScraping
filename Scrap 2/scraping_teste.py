from requests_html import HTMLSession
import csv
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from time import sleep

session = HTMLSession(verify=False)

def get_links(a):
    sleep(5)
    links = []
    setlinks = []
    sleep(5)
    url = f"http://www.tbca.net.br/base-dados/composicao_alimentos.php?pagina={a}"
    sleep(5)
    response = session.get(url)
    sleep(5)
    alimentos = response.html.find("table>tbody a")
    sleep(5)
    for items in alimentos:
        sleep(5)
        links.append(items.html.find("a", first=True).attrs["href"])
        sleep(5)
        
    for items in links:
        sleep(5)
        if "http://www.tbca.net.br/base-dados/" + items not in setlinks:
            setlinks.append("http://www.tbca.net.br/base-dados/" + items)
            sleep(5)
    
    return setlinks
        
def parser_Alimentos(a): 
    sleep(5)
    response = session.get(a)
    sleep(5)

    nomeAlimento = response.html.find("h5", first=True).text[25:250].strip()
    sleep(5)
    setNomeAlimento = nomeAlimento.split(", <<", 1)[0]
    sleep(5)


    nutriAlimento = response.html.find("tbody td")
    sleep(5)
    nutri = []
    sleep(5)
    for items in nutriAlimento:
        sleep(5)
        nutri.append(items.text)
        sleep(5)
        
    #print(len(nutri))
    #print(a)
              
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
    elif len(nutri) == 185: #testado
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
        "Alimento, Amostra 100g": setNomeAlimento,
        "Energia (kcal)": setKcal,
        "Proteina (g)": setProt,
        "Lipidios (g)": setLip,
        "Colesterol (mg)": setCol,
        "Carboidrato (g)": setCarb,
        "Fibra Alimentar (g)": setFibra
    }

    return result

def savecsv(result):
    keys = result[0].keys()
    
    with open ("alimentos.csv", "w") as f:
        dic_writer = csv.DictWriter(f, keys)
        dic_writer.writeheader()
        dic_writer.writerows(result)
        
#print(parser_Alimentos("http://www.tbca.net.br/base-dados/int_composicao_alimentos.php?cod_produto=C0006K"))

def main():
    sleep(5)
    alimentos = []
    sleep(5)
    for x in range(1, 2):
        sleep(5)
        print(f"Pagina: {x}")
        sleep(5)
        urls = get_links(x)
        sleep(5)
        for url in urls:
            sleep(5)
            alimentos.append(parser_Alimentos(url))
            sleep(5)
        print(f"Total: {len(alimentos)}")
        sleep(5)
        savecsv(alimentos)
        sleep(5)
        
if __name__ == '__main__':
    main()

main()