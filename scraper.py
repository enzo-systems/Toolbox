import requests
from bs4 import BeautifulSoup
import logging

# [CAMUFLAGEM]
# Mentimos para o servidor que somos um PC Gamer rodando Chrome.
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def conectar(url):
    """
    Função Auxiliar (O Carteiro).
    Apenas bate na porta e traz o pacote (HTML) fechado.
    """
    try:
        logging.info(f"Conectando ao alvo: {url}...")
        resposta = requests.get(url, headers=HEADERS, timeout=5)
        
        if resposta.status_code == 200:
            # Retorna a "Sopa" de HTML pronta para cirurgia
            return BeautifulSoup(resposta.content, 'html.parser')
        else:
            logging.warning(f"Erro {resposta.status_code} ao acessar {url}")
            return None
    except Exception as e:
        logging.error(f"Erro de conexão: {e}")
        return None

def buscar_titulo(url_alvo):
    """Modo Básico: Pega apenas o título da aba."""
    soup = conectar(url_alvo)
    if soup:
        titulo = soup.title.string.strip() if soup.title else "Sem Título"
        return f"Título: '{titulo}'"
    return "Falha na conexão."

def buscar_noticias_python():
    """
    [MODO SNIPER]
    Busca dados específicos dentro da estrutura do Python.org.
    Alvo: A widget de 'Upcoming Events' ou 'News'.
    """
    url = "https://www.python.org/"
    soup = conectar(url)
    
    if soup:
        # AQUI É A CIRURGIA:
        # Inspecionando o site, vemos que as notícias ficam numa div específica.
        # Vamos procurar a lista de 'Latest News'
        
        # Procura a div que tem a classe 'shrubbery' (onde ficam as listas no site deles)
        secao = soup.find('div', class_='shrubbery')
        
        if secao:
            # Pega o primeiro item da lista (li) dentro dessa seção
            noticia = secao.find('li')
            if noticia:
                texto = noticia.text.strip()
                # Limpeza de texto (remove quebras de linha feias)
                texto_limpo = " ".join(texto.split())
                return f"🔥 Python.org Última News: [{texto_limpo}]"
        
        return "Estrutura do site mudou. Não achei a notícia."
    
    return "Sem dados."