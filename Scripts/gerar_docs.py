#!/usr/bin/env python3 
# --- DOCSTRINGS ---
"""
ROBÔ: ARQUITETO DE DOCS (V2.5 - Full Auto)
FUNÇÃO: Geração integral do ecossistema de documentação (Raiz + Subpastas).
STATUS: Operacional - Nível 1
"""

import os
import re
import subprocess

# --- 1. MANIFESTO DO PROJETO (VISÃO ARQUITETURAL) ---
MANIFESTO = """# 🛠️ ToolBox - Ecossistema de Automação Sênior

### 📂 Visão Geral e Arquitetura
Este repositório é um ecossistema de automação modular desenvolvido para ambiente **Linux (Fedora/Debian/Ubuntu)**. O projeto integra agentes inteligentes e utilitários de infraestrutura sob uma arquitetura de níveis (1 a 4), focando em:

* **Inteligência de Dados:** Agentes autônomos para extração e processamento via *Web Scraping* e integração com *APIs REST*.
* **Segurança e Redes:** Ferramentas de auditoria de criptografia (SSL) e diagnóstico de conectividade de baixo nível.
* **Processamento de Mídia:** Pipelines para manipulação de imagem e síntese vocal, explorando automação visual e auditiva.
* **Resiliência de Sistema:** Scripts de manutenção de infraestrutura e gestão de processos em background (*Daemons*) com foco em persistência estruturada em CSV e JSON.

---
"""

# --- 2. DEFINIÇÕES TÉCNICAS (Atualizado com a 9ª Pasta) ---
DEFINICOES = {
    "Robos": "Unidade de Agentes Autônomos especializados por nível de complexidade.",
    "Scripts": "Utilitários de Automação de Infraestrutura e Manutenção de Sistema (Nível 1).",
    "Config": "Gestor de Parâmetros, Caminhos (Settings) e Variáveis de Ambiente (Nível 1).",
    "Docker": "Orquestrador de Containers e Ambientes Isolados (Nível 1).",
    "Docs": "Repositório de Documentação Técnica e Manuais do Projeto.",
    "Logs": "Registro de Atividades, Históricos e Depuração de Processos.",
    "Imagens": "Módulos de Processamento Visual e Manipulação de Imagens (Nível 3).",
    "CloneVoz": "Módulos de Processamento de Áudio e Síntese Vocal.",
    "Data": "Repositório de Dados Estruturados (JSON/CSV) gerados pelos robôs (Persistência)."
}

MAPA_MODULOS = {
    "Robos": "### 🤖 /Robos",
    "Scripts": "### 📂 /Scripts",
    "Config": "### ⚙️ /Config",
    "Docker": "### 🐳 /Docker",
    "Docs": "### 📚 /Docs",
    "Logs": "### 📝 /Logs",
    "Imagens": "### 🖼️ /Imagens",
    "CloneVoz": "### 🎙️ /CloneVoz",
    "Data": "### 📊 /Data"
}

STACK_TECNOLOGICO = """
---
### 🛠️ Stack Tecnológico
- **Linguagem:** Python 3.x / Bash
- **OS:** Linux (Fedora / Debian / Ubuntu)
- **Libs Principais:**
    - `requests`: Integração com APIs e requisições HTTP.
    - `BeautifulSoup4`: Extração de dados de HTML (Web Scraping).
    - `Pillow (PIL)`: Processamento e manipulação de imagens (Nível 3).
    - `pyOpenSSL`: Auditoria e gestão de certificados SSL.
    - `logging`: Sistema de rastreabilidade e histórico de eventos.
    - `socket`: Verificações de baixo nível de conectividade.
    - `csv/json`: Persistência de dados estruturados.
- **Conceitos:** Web Scraping, Image Processing, Daemon Processes, Logging, API REST, Persistência de Dados.
"""

# --- 3. LOGICA DE EXTRAÇÃO ---

def extrair_docstring(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            conteudo = f.read()
            if filepath.endswith('.py'):
                match = re.search(r'"""(.*?)"""', conteudo, re.DOTALL)
                if match: return f" | *{match.group(1).strip().replace('\n', ' ')}*"
            elif filepath.endswith('.sh'):
                for l in conteudo.split('\n'):
                    if l.startswith('#') and '!' not in l and len(l.strip()) > 5:
                        return f" | *{l.replace('#', '').strip()}*"
    except: pass
    return ""

def get_git_info(filepath):
    try:
        cmd = ['git', 'log', '-1', '--format=%s (%cd)', '--date=short', filepath]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout.strip() if result.stdout.strip() else "Aguardando commit"
    except: return "Novo"

def gerar_lista_arquivos(pasta, link_relativo=True):
    if not os.path.exists(pasta): return []
    extensoes = ('.py', '.sh', '.json', '.yml')
    arquivos = sorted([f for f in os.listdir(pasta) if f.endswith(extensoes) and f != 'README.md'])
    
    linhas = []
    for arq in arquivos:
        caminho = os.path.join(pasta, arq)
        git_info = get_git_info(caminho)
        desc = extrair_docstring(caminho)
        prefixo = f"./{pasta}/" if not link_relativo else "./"
        linhas.append(f"- **[{arq}]({prefixo}{arq})**: {git_info}{desc}")
    return linhas if linhas else ["- *Pasta estruturada.*"]

# --- 4. EXECUÇÃO ---

def main():
    # Iniciamos o conteúdo com o Manifesto Fixo
    conteudo_raiz = MANIFESTO

    # Adicionamos as seções de módulos dinamicamente
    for pasta, header in MAPA_MODULOS.items():
        if os.path.exists(pasta):
            conteudo_raiz += f"\n{header}\n{DEFINICOES[pasta]}\n\n"
            conteudo_raiz += "\n".join(gerar_lista_arquivos(pasta, False)) + "\n"

    # Finalizamos com o Stack Tecnológico
    conteudo_raiz += STACK_TECNOLOGICO

    # Salva o README principal
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(conteudo_raiz)
    
    # Atualiza sub-readmes
    for pasta in DEFINICOES.keys():
        if os.path.exists(pasta):
            with open(os.path.join(pasta, "README.md"), 'w', encoding='utf-8') as f:
                f.write(f"# 📁 /{pasta}\n\n> {DEFINICOES[pasta]}\n\n## 📜 Arquivos\n")
                f.write("\n".join(gerar_lista_arquivos(pasta, True)))

    print("🚀 Auditoria Suprema Concluída! README.md foi totalmente reconstruído pelo Arquiteto.")

if __name__ == "__main__":
    main()