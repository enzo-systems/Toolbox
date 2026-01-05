# --- Robo Vagas: Web Scraper ---
import requests
from bs4 import BeautifulSoup

# 1. Definir o alvo (Site de empregos oficial do Python - é leve e não bloqueia fácil)
url = "https://www.python.org/jobs/"
print(f"--> Acessando: {url}")

# 2. O Robô bate na porta
resposta = requests.get(url)

if resposta.status_code == 200:
    # 3. Colocar os "óculos" (Transformar texto bruto em objeto navegável)
    soup = BeautifulSoup(resposta.text, 'html.parser')
    
    # 4. Achar a agulha no palheiro
    # No site do Python, as vagas ficam dentro de tags <h2> com a classe "listing-company"
    # Como eu sei isso? Eu (Enzo+Gemini) inspecionei o site antes.
    vagas = soup.find_all('h2', class_='listing-company')
    
    print(f"\nEncontrei {len(vagas)} vagas recentes:\n")
    print("-" * 40)
    
    # 5. Loop para mostrar uma por uma
    for vaga in vagas:
        # Extrair o texto limpo, tirando espaços em branco extras
        titulo = vaga.get_text(strip=True)
        print(f"[VAGA] {titulo}")
        
    print("-" * 40)
    
else:
    print("O site bloqueou ou está fora do ar.")
import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/jobs/"
print(f"--> Monitorando: {url}")

resposta = requests.get(url)

if resposta.status_code == 200:
    soup = BeautifulSoup(resposta.text, 'html.parser')
    vagas = soup.find_all('h2', class_='listing-company')
    
    contador = 0
    print("\n--- OPORTUNIDADES FILTRADAS (BRASIL / REMOTO) ---\n")
    
    for vaga in vagas:
        texto_completo = vaga.get_text(strip=True).lower() # Converte tudo pra minúsculo pra facilitar a busca
        
        # AQUI ESTÁ A INTELIGÊNCIA DO ROBÔ
        # Só mostre se tiver "brazil", "remote" ou "latam" no texto
        if "brazil" in texto_completo or "remote" in texto_completo or "latam" in texto_completo:
            print(f"[ALVO ENCONTRADO] {vaga.get_text(strip=True)}")
            contador += 1
            
    if contador == 0:
        print("Nenhuma vaga no perfil encontrada hoje.")
    else:
        print(f"\nTotal de alvos: {contador}")
        
else:
    print("Erro ao acessar o site.")
