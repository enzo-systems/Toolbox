#!/usr/bin/env python3
"""
Docstring -
ROBÔ: SENTINELA FINANCEIRO
FUNÇÃO: Captura cotação do dólar via API e mantém histórico em CSV.
Ou seja, Integrador de API: Captura dados financeiros profissionais e gera histórico.
STATUS: Operacional - Nível 2. 
"""

import requests
import logging
import os
import csv
from datetime import datetime

# 1. Configuração de Caminhos e Logs
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILE = os.path.join(BASE_DIR, "Logs", "historico_dolar.csv")

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def salvar_no_historico(valor):
    # Verifica se o arquivo existe para escrever o cabeçalho
    arquivo_novo = not os.path.exists(LOG_FILE)
    
    try:
        with open(LOG_FILE, 'a', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f)
            if arquivo_novo:
                escritor.writerow(["Data/Hora", "Moeda", "Valor (R$)"])
            
            agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            escritor.writerow([agora, "USD", valor])
            logging.info(f"💾 Dados salvos em: {LOG_FILE}")
    except Exception as e:
        logging.error(f"❌ Erro ao salvar arquivo: {e}")

def pegar_dolar():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            dados = response.json()
            valor = float(dados['USDBRL']['bid'])
            
            logging.info(f"💵 Valor capturado: R$ {valor:.2f}")
            
            # CHAMA A FUNÇÃO DE SALVAMENTO
            salvar_no_historico(valor)
            return valor
    except Exception as e:
        logging.error(f"❌ Falha na missão: {e}")

if __name__ == "__main__":
    pegar_dolar() 