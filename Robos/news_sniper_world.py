"""
Docstring -
ROBÔ: Web Scraping
FUNÇÃO: Procura informações específicas em toda internet.
Ou seja, Coletor de Dados: Raspagem de notícias.
STATUS: Ativo e funcional - Nível 2 
"""

import requests
import xml.etree.ElementTree as ET
import json
import os
import time

# --- CONFIGURAÇÃO: SNIPER GLOBAL (Google News) ---
TERMOS_ALVO = ["Inteligência Artificial", "Linux", "Python", "Cibersegurança"]
ARQUIVO_MEMORIA = "Logs/memoria_world.json" # Memória exclusiva deste robô

def carregar_memoria():
    if os.path.exists(ARQUIVO_MEMORIA):
        try:
            with open(ARQUIVO_MEMORIA, 'r') as f:
                return json.load(f)
        except:
            return []
    return []

def salvar_memoria(lista_vistos):
    # Salva apenas os últimos 500 links
    with open(ARQUIVO_MEMORIA, 'w') as f:
        json.dump(lista_vistos[-500:], f)

def buscar_google_news():
    print(f"🌍 Iniciando Varredura Global (Google News RSS)...")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Compatible; SniperBot/2.0)'
    }
    
    memoria = carregar_memoria()
    novas_descobertas = []

    for termo in TERMOS_ALVO:
        print(f"   Targeting: [{termo}]...")
        
        # URL do RSS do Google News Brasil
        url = f"https://news.google.com/rss/search?q={termo}&hl=pt-BR&gl=BR&ceid=BR:pt-419"
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            
            # O Google retorna XML. Vamos analisar a árvore.
            root = ET.fromstring(response.content)
            
            # Pega até 3 notícias por termo
            contador_termo = 0
            for item in root.findall('./channel/item'):
                if contador_termo >= 3: break 
                
                titulo = item.find('title').text
                link = item.find('link').text
                
                if link not in memoria:
                    print(f"   🔥 ALVO ATINGIDO: {titulo}")
                    print(f"      Link: {link}\n")
                    
                    memoria.append(link)
                    novas_descobertas.append(titulo)
                    contador_termo += 1
            
            time.sleep(1) # Respira para não ser bloqueado

        except Exception as e:
            print(f"❌ Erro ao buscar '{termo}': {e}")

    if novas_descobertas:
        salvar_memoria(memoria)
        print(f"✅ Missão cumprida. {len(novas_descobertas)} notícias globais arquivadas.")
    else:
        print("💤 Nenhuma novidade no front global.")

if __name__ == "__main__":
    buscar_google_news()
