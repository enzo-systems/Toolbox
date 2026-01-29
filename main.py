#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Arquivo: main.py

"""
Enzo ToolBox - Orchestrator V1.3
Refatorado para arquitetura modular profunda (Nested Packages).
"""

import sys
import logging
import time

# 1. Integração com o Cérebro de Configuração
# Garante que sabemos onde estamos no disco antes de qualquer coisa
from config.settings import BASE_DIR

# 2. Importação do Agente Realocado
# Caminho antigo: from agents import kernel_probe
# Caminho novo (Lógico -> Físico): agents.monitor.kernel -> agents/monitor/kernel.py
from agents.monitor import kernel

# Configuração de Logs
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [ORCHESTRATOR] - %(levelname)s - %(message)s'
)

def processar_comando(comando):
    """Dispatcher: Recebe string -> Aciona Ponteiro de Função"""
    cmd = comando.lower().strip()

    if cmd == "exit":
        logging.info("Encerrando processo (SIGTERM voluntário).")
        sys.exit(0)
    
    elif cmd == "sys":
        # Aciona a função 'probe' dentro do módulo 'kernel'
        kernel.probe()
    
    elif cmd == "help":
        print("\n--- MENU DE COMANDOS ---")
        print("  sys   -> Hardware Probe (/proc reader)")
        print("  exit  -> Kill process\n")
    
    else:
        logging.warning(f"Instrução inválida: {comando}, tente help")

def main():
    print(f"\n[BOOTLOADER] Root Path: {BASE_DIR}")
    logging.info("Carregando módulos de monitoramento...")
    time.sleep(0.2) # Debounce simulado
    
    print("--- Enzo ToolBox V1.3 (Modular) ---\n")
    
    while True:
        try:
            # Input Bloqueante (Aguardando STDIN)
            user_input = input("Enzo@ToolBox:~$ ")
            
            if not user_input: continue # Ignora Enter vazio
            processar_comando(user_input)
            
        except KeyboardInterrupt:
            # Captura Ctrl+C
            print("\n[INTERRUPT] Parada forçada pelo usuário.")
            break
        except Exception as e:
            # Captura Crash não tratado
            logging.critical(f"RAM Dump (Erro): {e}")

if __name__ == "__main__":
    main()