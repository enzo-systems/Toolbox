#!/usr/bin/env python3
"""
Docstring -
ROBÔ: GURU
FUNÇÃO: Analisa logs e fornece diagnósticos preditivos sobre o status do sistema.
Ou seja, Diagnóstico: Analisador de logs do sistema (Alpha).
STATUS: Em desenvolvimento / Alpha - Nível 1  
"""

import requests
import sys

def buscar_sabedoria(comando):
    # Tenta buscar primeiro em Português (pt_BR)
    base_url_pt = f"https://raw.githubusercontent.com/tldr-pages/tldr/main/pages.pt_BR/common/{comando}.md"
    base_url_pt_linux = f"https://raw.githubusercontent.com/tldr-pages/tldr/main/pages.pt_BR/linux/{comando}.md"
    
    # Fallback para Inglês se não tiver tradução
    base_url_en = f"https://raw.githubusercontent.com/tldr-pages/tldr/main/pages/common/{comando}.md"
    base_url_en_linux = f"https://raw.githubusercontent.com/tldr-pages/tldr/main/pages/linux/{comando}.md"

    urls_para_tentar = [base_url_pt, base_url_pt_linux, base_url_en, base_url_en_linux]

    conteudo_raw = ""
    sucesso = False

    print(f"🔍 Buscando conhecimento sobre: '{comando}'...")

    for url in urls_para_tentar:
        try:
            r = requests.get(url)
            if r.status_code == 200:
                conteudo_raw = r.text
                sucesso = True
                break
        except:
            continue

    if not sucesso:
        print(f"❌ Não encontrei nada sobre '{comando}'. Tente um comando mais comum (ex: tar, grep, chmod).")
        return

    # --- O PULO DO GATO: Formatação para Discord ---
    # O conteúdo vem em Markdown simples. Vamos deixar BONITO para o Discord.
    
    linhas = conteudo_raw.split('\n')
    
    print("\n" + "="*40)
    print("   COPIE O TEXTO ABAIXO E COLE NO DISCORD")
    print("="*40 + "\n")

    # Cabeçalho do Discord
    saida_discord = f"**💡 Dica Rápida: Dominando o `{comando}`**\n\n"
    
    for linha in linhas:
        if linha.startswith('>'): 
            # Descrição do comando
            saida_discord += f"_{linha.replace('>', '').strip()}_\n"
        elif linha.startswith('-'):
            # Explicação do exemplo
            saida_discord += f"\n🔹 **{linha.replace('-', '').strip()}**\n"
        elif linha.startswith('`'):
            # O código em si (colocamos em bloco bash para ficar colorido)
            codigo = linha.replace('`', '').strip()
            saida_discord += f"```bash\n{codigo}\n```"

    saida_discord += "\n_Fonte: tldr-pages | Curadoria: Enzo_"
    
    print(saida_discord)
    print("\n" + "="*40)

# Input do usuário
if len(sys.argv) > 1:
    cmd = sys.argv[1]
else:
    cmd = input("Qual comando Linux você quer explicar hoje? (ex: tar): ")

buscar_sabedoria(cmd.lower())
