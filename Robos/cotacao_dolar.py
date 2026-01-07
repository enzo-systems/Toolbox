"""
Objetivo: Robô que busca a cotação do dólar dentro do site do google
"""
import requests
from bs4 import BeautifulSoup

def pegar_dolar():
    url = "https://www.google.com/search?q=cotacao+dolar"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    
    # O "Binóculo" entra em ação
    soup = BeautifulSoup(response.text, 'html.parser')

    # No Google, a cotação geralmente fica em uma classe específica
    # Nota: Web Scraping é frágil, se o Google mudar o site, temos que ajustar
    try:
        # Tentando encontrar o valor numérico
        resultado = soup.find("span", {"class": "DFlfde"}).text
        centavos = soup.find("span", {"class": "vW7d1c"}).text # Às vezes o valor é quebrado
        
        print(f"💵 Cotação do Dólar agora: R$ {resultado}")
    except:
        print("❌ O Google mudou a estrutura. Precisamos de um binóculo melhor!")

if __name__ == "__main__":
    pegar_dolar()