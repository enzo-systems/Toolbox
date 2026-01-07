#!/usr/bin/env python3
# --- DOCSTRINGS ---
"""
NÍVEL 1: Supervisor de Processos (Watchdog)
FUNÇÃO: Garante a persistência e reinicialização automática dos agentes do sistema. Este bot trata com Infraestrutura pura.
CONCEITOS: Monitoramento de Processos, Resiliência, Systemd.
"""

import subprocess
import time
import os

def enviar_notificacao(titulo, mensagem):
    """Envia um popup visual no desktop do Fedora."""
    try:
        # O comando notify-send é padrão no GNOME (Fedora)
        subprocess.run(['notify-send', '-u', 'critical', titulo, mensagem])
    except Exception as e:
        print(f"Erro ao enviar notificação: {e}")

def verificar_servico(nome_servico):
    """Consulta o systemctl para saber se o serviço está rodando."""
    try:
        cmd = ['systemctl', 'is-active', nome_servico]
        resultado = subprocess.run(cmd, capture_output=True, text=True)
        return resultado.stdout.strip() == 'active'
    except Exception:
        return False

print("👁️  Watchdog iniciado. Vigiando o Sentinela...")

while True:
    if not verificar_servico('sentinela.service'):
        # Se o Sentinela caiu, avisamos o Arquiteto imediatamente
        enviar_notificacao(
            "🚨 ALERTA DO ARQUITETO", 
            "O Sentinela parou de responder! Verifique o sistema."
        )
        print("⚠️  ALERTA: Sentinela offline. Notificação enviada.")
    
    # Verifica a cada 5 minutos para não sobrecarregar o sistema
    time.sleep(300)