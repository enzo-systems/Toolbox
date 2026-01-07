"""
Docstring-------------------------------------------------
ROBÔ: SENTINELA
FUNÇÃO: Navega na Internet como um Agent.
        Ou seja, Agente Navegador: Navega na web como um agente autônomo.
STATUS: Operacional com rotação de logs - Nível 2.
"""
#!/usr/bin/env python3
import requests
import logging
import os
from dotenv import load_dotenv

# 1. Configuração Sênior (Fonte 8)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def explorar_site(url):
    # 2. O Disfarce (User-Agent)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }

    try:
        logging.info(f"🛰️  Tentando acessar: {url}")
        
        # 3. A Requisição com Timeout (Regra da Fonte 8 para não travar)
        response = requests.get(url, headers=headers, timeout=10)

        # 4. Verificação de Sucesso (Status 200 = OK)
        if response.status_code == 200:
            logging.info(f"✅ Conexão estabelecida!")
            logging.info(f"📄 Tamanho dos dados recebidos: {len(response.text)} bytes")
            
            # Vamos ver um pedacinho do que ele "leu"
            print("-" * 30)
            print(response.text[:500]) # Mostra os primeiros 500 caracteres do HTML
            print("-" * 30)
            
        else:
            logging.warning(f"⚠️ O servidor barrou o robô. Código: {response.status_code}")

    except Exception as e:
        logging.error(f"❌ Erro na missão: {e}")

if __name__ == "__main__":
    # Teste com um site que aceita bem robôs (Wikipedia ou Google)
    explorar_site("https://pt.wikipedia.org/wiki/Python")