#!/usr/bin/env python3
"""
Docstring -
ROBÔ: SENTINELA
FUNÇÃO: Monitora a conexão de rede a cada 60 segundos e evita que o log cresça demais.
Ou seja, Zelador de Infra: Monitora rede e rotaciona logs para não encher o disco.
STATUS: Operacional com rotação de logs - Nivel 1. 
"""

import time
import socket
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime

# --- CONFIGURAÇÃO DO ARQUITETO (VERSÃO BLINDADA) ---
# Definimos um Handler que rotaciona o arquivo para ele não crescer infinitamente.
# maxBytes = 5MB (5 * 1024 * 1024)
# backupCount = 3 (Mantém o atual + 3 arquivos antigos de histórico)
log_handler = RotatingFileHandler(
    'Log/sentinela.log', 
    maxBytes=5*1024*1024, 
    backupCount=3
)

# Aplicamos a configuração usando o nosso handler rotativo
logging.basicConfig(
    handlers=[log_handler],
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def checar_conexao():
    """Tenta conectar ao DNS do Google (8.8.8.8) na porta 53.
    É mais rápido e silencioso que um ping."""
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False

print("🛡️  Sentinela iniciado. Rodando em background com proteção de log...")
print("📝  Verifique o arquivo 'sentinela.log'. Limite automático: 5MB.")

# --- O LOOP INFINITO (DAEMON) ---
while True:
    if checar_conexao():
        # Em vez de print, usamos logging.info
        logging.info("STATUS: ONLINE - A rede está operante.")
    else:
        # Se cair, logamos como WARNING (Aviso)
        logging.warning("ALERTA: OFFLINE - Conexão perdida!")
    
    # O Arquiteto define o ritmo. 
    # Dorme por 60 segundos para não gastar CPU à toa.
    time.sleep(60) 