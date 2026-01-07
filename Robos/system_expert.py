#!/usr/bin/env python3 
"""
NÍVEL 1: Agente de Diagnóstico de Infraestrutura
FUNÇÃO: Analisa comandos Linux e gera documentação formatada para comunidades.
CONCEITOS: Shell Integration, Log Parsing, Integração com API TLDR.
"""

import sys
import requests
import json
from pathlib import Path
from datetime import datetime

# --- BOOTSTRAP: CONEXÃO COM O SETTINGS ---
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.append(str(BASE_DIR))

try:
    from Config.settings import DIRS
    ARQUIVO_ENCICLOPEDIA = DIRS["DATA"] / "enciclopedia_linux.json"
except ImportError:
    ARQUIVO_ENCICLOPEDIA = BASE_DIR / "Data" / "enciclopedia_linux.json"
    ARQUIVO_ENCICLOPEDIA.parent.mkdir(parents=True, exist_ok=True)

def buscar_sabedoria(comando):
    # URLs de busca (Ordem: PT-BR Common -> Linux -> EN Common -> Linux)
    urls = [
        f"https://raw.githubusercontent.com/tldr-pages/tldr/main/pages.pt_BR/common/{comando}.md",
        f"https://raw.githubusercontent.com/tldr-pages/tldr/main/pages.pt_BR/linux/{comando}.md",
        f"https://raw.githubusercontent.com/tldr-pages/tldr/main/pages/common/{comando}.md",
        f"https://raw.githubusercontent.com/tldr-pages/tldr/main/pages/linux/{comando}.md"
    ]

    print(f"🔍 Buscando conhecimento sobre: '{comando}'...")
    conteudo_raw = ""
    
    for url in urls:
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                conteudo_raw = r.text
                break
        except:
            continue

    if not conteudo_raw:
        print(f"❌ Comando '{comando}' não encontrado na base TLDR.")
        return None

    return formatar_para_discord(comando, conteudo_raw)

def formatar_para_discord(comando, raw_text):
    linhas = raw_text.split('\n')
    saida_discord = f"**💡 Dica Rápida: Dominando o `{comando}`**\n\n"
    
    for linha in linhas:
        if linha.startswith('>'): 
            saida_discord += f"_{linha.replace('>', '').strip()}_\n"
        elif linha.startswith('-'):
            saida_discord += f"\n🔹 **{linha.replace('-', '').strip()}**\n"
        elif linha.startswith('`'):
            codigo = linha.replace('`', '').strip()
            saida_discord += f"```bash\n{codigo}\n```"

    saida_discord += "\n_Fonte: tldr-pages | Curadoria: ToolBox_"
    return saida_discord

def arquivar_comando(comando, formatado):
    """Guarda a consulta na nossa base de dados local."""
    base = {}
    if ARQUIVO_ENCICLOPEDIA.exists():
        with open(ARQUIVO_ENCICLOPEDIA, 'r', encoding='utf-8') as f:
            base = json.load(f)
    
    base[comando] = {
        "data_consulta": datetime.now().strftime("%Y-%m-%d"),
        "conteudo": formatado
    }

    with open(ARQUIVO_ENCICLOPEDIA, 'w', encoding='utf-8') as f:
        json.dump(base, f, indent=4, ensure_ascii=False)
    print(f"💾 Conhecimento arquivado em: {ARQUIVO_ENCICLOPEDIA.name}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        cmd_input = sys.argv[1]
    else:
        cmd_input = input("Qual comando Linux você quer explicar hoje? (ex: tar): ")

    resultado = buscar_sabedoria(cmd_input.lower())
    
    if resultado:
        print("\n" + "="*40)
        print(resultado)
        print("="*40 + "\n")
        arquivar_comando(cmd_input.lower(), resultado)