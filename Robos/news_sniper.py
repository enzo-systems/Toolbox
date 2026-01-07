"""
Docstring-------------------------------------------------
ROBÔ: Web Scraping
FUNÇÃO: Procura informações específicas em sites específicos.
        Ou seja, Coletor de Dados: Raspagem de notícias.
STATUS: Ativo e funcional - Nível 2
"""
import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime

# --- CONFIGURAÇÃO DO ARQUITETO ---
# Onde vamos caçar?
URL_ALVO = "https://www.tabnews.com.br"

# O que estamos procurando? (Case insensitive - ele converte tudo pra minusculo pra comparar)
PALAVRAS_CHAVE = ["inteligência artificial", "linux", "python"]

# Onde guardar a memória do que já vimos?
ARQUIVO_MEMORIA = "Logs/memoria_news.json"

def carregar_memoria():
    """Lê o arquivo JSON para saber quais notícias já processamos."""
    if os.path.exists(ARQUIVO_MEMORIA):
        try:
            with open(ARQUIVO_MEMORIA, 'r') as f:
                return json.load(f)
        except:
            return [] # Se der erro, retorna lista vazia
    return []

def salvar_memoria(lista_vistos):
    """Atualiza o arquivo JSON com as novas notícias vistas."""
    with open(ARQUIVO_MEMORIA, 'w') as f:
        json.dump(lista_vistos, f)

def caçar_noticias():
    print(f"🕵️  Iniciando varredura no TabNews...")
    
    # 1. Fingir ser um navegador real (Bypass básico)
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }

    try:
        response = requests.get(URL_ALVO, headers=headers)
        response.raise_for_status() # Para se der erro 404/500
    except Exception as e:
        print(f"❌ Erro ao conectar: {e}")
        return

    # 2. Transformar o HTML em Objeto Python
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 3. Extrair os Links (No TabNews, os titulos ficam dentro de tags <a>)
    # Essa lógica pega TODOS os links da página
    links = soup.find_all('a')

    memoria = carregar_memoria()
    novas_descobertas = []

    print(f"🔎 Analisando {len(links)} links encontrados...")

    for link in links:
        titulo = link.get_text().strip()
        url_noticia = link.get('href')

        # Filtro de Qualidade: Ignora links vazios ou curtos demais
        if not titulo or len(titulo) < 10:
            continue
            
        # Normaliza para busca (tudo minúsculo)
        titulo_lower = titulo.lower()

        # 4. A Lógica do Sniper: Bate com as Keywords?
        encontrou = False
        keyword_achada = ""
        
        for palavra in PALAVRAS_CHAVE:
            if palavra in titulo_lower:
                encontrou = True
                keyword_achada = palavra
                break # Se achou uma, não precisa buscar as outras no mesmo titulo
        
        if encontrou:
            # Verifica se já vimos essa notícia antes (pela URL)
            if url_noticia not in memoria:
                print(f"🎯 ALVO ENCONTRADO [{keyword_achada.upper()}]: {titulo}")
                print(f"   Link: {URL_ALVO}{url_noticia}\n")
                
                # Adiciona à memória para não repetir
                memoria.append(url_noticia)
                novas_descobertas.append(titulo)

    # 5. Salvar o progresso
    if novas_descobertas:
        salvar_memoria(memoria)
        print(f"✅ Varredura concluída. {len(novas_descobertas)} novos alvos registrados.")
    else:
        print("💤 Nada novo sob o sol. O Sniper voltará em breve.")

if __name__ == "__main__":
    caçar_noticias()
