"""
NÍVEL 1: Gestor de Ambiente e Caminhos
FUNÇÃO: Centraliza a inteligência de diretórios e parâmetros globais do sistema.
CONCEITOS: Abstração de Caminhos, Configuração Centralizada.
"""

import os
from pathlib import Path

# Caminho Base do Projeto (Raiz da ToolBox)
BASE_DIR = Path(__file__).resolve().parent.parent

# Definição dos Diretórios Principais
DIRS = {
    "ROBOS": BASE_DIR / "Robos",
    "SCRIPTS": BASE_DIR / "Scripts",
    "CONFIG": BASE_DIR / "Config",
    "DOCS": BASE_DIR / "Docs",
    "LOGS": BASE_DIR / "Logs",
    "IMAGENS": BASE_DIR / "Imagens",
    "CLONEVOZ": BASE_DIR / "CloneVoz",
    "DOCKER": BASE_DIR / "Docker",
    "DATA": BASE_DIR / "Data"
}

# Garante que TODAS as pastas do dicionário existam
for folder_path in DIRS.values():
    folder_path.mkdir(parents=True, exist_ok=True)

# Configurações de Câmbio (Puxando do dicionário DIRS)
CAMBIO_CONFIG = {
    "url_api": "https://economia.awesomeapi.com.br/last/USD-BRL",
    "arquivo_saida": DIRS["DATA"] / "cotacao_dolar.csv"
}

# Configurações de Logs Globais
LOGGING_CONF = {
    "format": '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    "datefmt": '%Y-%m-%d %H:%M:%S',
    "arquivo_log": DIRS["LOGS"] / "system_toolbox.log"
}