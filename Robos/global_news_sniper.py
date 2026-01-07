#!/usr/bin/env python3
"""
NÍVEL 2: Agente de Inteligência de Dados
FUNÇÃO: Coleta e processa notícias internacionais via RSS (Feedparser).
CONCEITOS: RSS Parsing, Normalização de Dados, Persistência Estruturada.
"""

import sys
import json
import time
import feedparser  # A forma sênior de ler RSS
from pathlib import Path
from urllib.parse import quote  # Essencial para tratar espaços e acentos na URL

# --- BOOTSTRAP: CONEXÃO COM O SETTINGS ---
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.append(str(BASE_DIR))

try:
    from Config.settings import DIRS
    ARQUIVO_MEMORIA = DIRS["DATA"] / "memoria_world.json"
except ImportError:
    ARQUIVO_MEMORIA = BASE_DIR / "Data" / "memoria_world.json"
    ARQUIVO_MEMORIA.parent.mkdir(parents=True, exist_ok=True)

# --- CONFIGURAÇÃO ---
TERMOS_ALVO = ["Inteligência Artificial", "Linux", "Python", "Cibersegurança"]

def carregar_memoria():
    if ARQUIVO_MEMORIA.exists():
        try:
            with open(ARQUIVO_MEMORIA, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            # Se o arquivo estiver corrompido, retorna lista vazia
            return []
    return []

def salvar_memoria(lista_vistos):
    with open(ARQUIVO_MEMORIA, 'w', encoding='utf-8') as f:
        # Mantendo os últimos 500 para controle de duplicatas
        json.dump(lista_vistos[-500:], f, indent=4, ensure_ascii=False)

def buscar_google_news():
    print(f"🌍 Iniciando Varredura via Feedparser...")
    
    memoria = carregar_memoria()
    novas_descobertas = []

    for termo in TERMOS_ALVO:
        # SENIOR: Encodar o termo para evitar erro de caracteres especiais e espaços
        termo_safe = quote(termo)
        print(f"   Targeting: [{termo}]...")
        
        url = f"https://news.google.com/rss/search?q={termo_safe}&hl=pt-BR&gl=BR&ceid=BR:pt-419"
        
        # O feedparser faz a requisição e o parse do XML
        feed = feedparser.parse(url)
        
        contador_termo = 0
        for entry in feed.entries:
            if contador_termo >= 3: 
                break 
            
            titulo = entry.title
            link = entry.link
            
            if link not in memoria:
                print(f"   🔥 ALVO ATINGIDO: {titulo}")
                memoria.append(link)
                novas_descobertas.append({
                    "titulo": titulo, 
                    "link": link, 
                    "data": entry.get('published', 'N/A')
                })
                contador_termo += 1
        
        # Pausa técnica para evitar bloqueios (Rate Limiting)
        time.sleep(1)

    if novas_descobertas:
        salvar_memoria(memoria)
        print(f"✅ Missão cumprida. {len(novas_descobertas)} novos registros memorizados.")
    else:
        print("💤 Sem novidades no radar.")

if __name__ == "__main__":
    buscar_google_news()