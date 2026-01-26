#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Enzo ToolBox - Orchestrator (Cérebro Central)
Arquitetura: Modular Monolithic
Author: Enzo (O Arquiteto)
System: Debian Linux
"""

import sys
import time
import logging
import scraper  # <--- [NOVO] O Módulo Scraper é carregado aqui

# [1] Configuração de Logging (A "Caixa Preta" do Avião)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [KERNEL] - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()] # Joga o log no Terminal
)

def inicializar_motor():
    """Prepara o ambiente, carrega configs e verifica conexões."""
    logging.info("Inicializando sistemas... Alocando memória.")
    # Aqui carregaremos as variáveis de ambiente (.env) futuramente
    time.sleep(0.5) # Simulação de carga de drivers
    logging.info("Motor V12 pronto. Aguardando input.")

def processar_comando(comando):
    """
    O Router. Decide para qual 'Agente' mandar a tarefa.
    Não resolve nada, apenas delega.
    """
    cmd = comando.lower().strip()

    if cmd == "exit":
        logging.info("Desligando motores...")
        sys.exit(0)
    
    elif cmd == "help":
        print("\n--- COMANDOS DISPONÍVEIS ---")
        print("1. finance  -> Agente de Mercado (Em breve)")
        print("2. scraper  -> Agente de Coleta (ATIVO)") # <--- Atualizado
        print("3. system   -> Monitoramento Linux")
        print("----------------------------\n")

    # [Gatilho para o Scraper]
    elif cmd.startswith("scraper"):
        partes = comando.split()
        
        # Se o usuário digitar: "scraper news"
        if len(partes) > 1 and partes[1] == "news":
            logging.info("Modo Sniper ativado: Buscando notícias no Python.org...")
            resultado = scraper.buscar_noticias_python()
            print(f"\n>> [DADO EXTRAÍDO]: {resultado}\n")
            
        else:
            # Modo Padrão (Se digitar só "scraper" ou "scraper google.com")
            alvo = "https://www.google.com"
            if len(partes) > 1:
                alvo = partes[1]
            
            logging.info("Acionando Agente Scraper (Modo Genérico)...")
            resultado = scraper.buscar_titulo(alvo) 
            print(f"\n>> [RETORNO]: {resultado}\n")

    # [Gatilho para Módulos Futuros]
    elif cmd == "system":
        logging.info("Chamando módulo System...")
        # from agents import system_monitor
        # system_monitor.run()
        print(">> [MÓDULO SYSTEM]: CPU: 12% | RAM: 1.4GB (Simulado)")

    else:
        logging.warning(f"Comando desconhecido: {comando}")

def main_loop():
    """
    O Loop Infinito (Event Loop).
    Mantém o processo vivo na CPU aguardando interrupções.
    """
    inicializar_motor()

    while True:
        try:
            # O cursor piscando é o 'input' bloqueante. 
            # O processador descansa aqui até você teclar algo.
            user_input = input("Enzo@ToolBox:~$ ")
            processar_comando(user_input)
        
        except KeyboardInterrupt:
            # Captura o Ctrl+C para sair com elegância, sem crashar.
            print("\n")
            logging.info("Interrupção forçada pelo piloto (Ctrl+C).")
            break
        except Exception as e:
            # O Airbag. Se algo explodir, o programa não fecha, ele loga e continua.
            logging.error(f"Erro Crítico no Loop Principal: {e}")

# [2] A Chave de Ignição Segura
if __name__ == "__main__":
    main_loop()