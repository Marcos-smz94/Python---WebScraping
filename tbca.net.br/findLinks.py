import requests
from bs4 import BeautifulSoup
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

def fileLinks(a):
    with open("links.txt", "a") as f:
        for items in a:
            f.write(items + '\n')
            
for i in range(1,58):
    sleep(10)
    fileLinks(get_links(i))