#!/usr/bin/env python3
"""
Docstring -
ROBÔ: Web Scraper
FUNÇÃO: acessa todas as informações de sites específicos.
STATUS: Ativo e funcional - Nível 2 
"""
# --- Playground de Testes ---
import requests

print("Tentando acessar o Google...")
resposta = requests.get('https://www.google.com')

if resposta.status_code == 200:
    print("SUCESSO: O robô conseguiu acessar o site!")
    print(f"Tamanho da página baixada: {len(resposta.text)} caracteres.")
else:
    print("FALHA: O site rejeitou a conexão.")
