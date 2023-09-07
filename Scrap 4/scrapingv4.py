import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_food_data():
    base_url = 'https://fdc.nal.usda.gov'
    search_url = f'https://fdc.nal.usda.gov/fdc-app.html#/'
    
    response = requests.get(search_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    food_links = soup.find_all('a', class_='result-description')
    
    data = []
    
    for link in food_links:
        food_url = base_url + link['href']
        food_data = extract_food_data(food_url)
        data.append(food_data)
    
    return data

def extract_food_data(food_url):
    response = requests.get(food_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    food_name = soup.find('h1').text.strip()
    energy = soup.find('div', class_='nutval').text.strip()
    protein = soup.find('div', id='proteinVal').text.strip()
    total_lipid = soup.find('div', id='lipidVal').text.strip()
    carbohydrate = soup.find('div', id='carbohydrateVal').text.strip()
    sugars = soup.find('div', id='sugarsVal').text.strip()
    
    food_data = {
        'Food Item': food_name,
        'Energy (kcal)': energy,
        'Protein (g)': protein,
        'Total Lipid (g)': total_lipid,
        'Carbohydrate (g)': carbohydrate,
        'Sugars (g)': sugars,
    }
    
    return food_data

def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

if __name__ == '__main__':
    scraped_data = scrape_food_data()
    save_to_csv(scraped_data, 'food_data.csv')
