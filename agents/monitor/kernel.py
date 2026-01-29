# Arquivo: agents/kernel_probe.py
import logging

def probe():
    """Lógica isolada de sondagem do Kernel"""
    logging.info("Módulo KernelProbe carregado. Lendo /proc...")
    
    # 1. Load Average
    try:
        with open('/proc/loadavg', 'r') as f:
            load = f.read().split()[0:3]
            print(f"\n[CPU] Load: {load[0]} | {load[1]} | {load[2]}")
    except Exception:
        print("[CPU] Erro de leitura.")

    # 2. Memória
    try:
        mem_stats = {}
        with open('/proc/meminfo', 'r') as f:
            for line in f:
                parts = line.split(':')
                if len(parts) == 2:
                    mem_stats[parts[0].strip()] = int(parts[1].strip().split()[0])
        
        total = mem_stats.get('MemTotal', 0) // 1024
        livre = mem_stats.get('MemAvailable', 0) // 1024
        used = total - livre
        print(f"[MEM] Usada: {used}MB / {total}MB")
    except Exception:
        print("[MEM] Erro de leitura.")
    
    print("-" * 20 + "\n")