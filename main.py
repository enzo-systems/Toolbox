#!/usr/bin/env python3 
"""
ORQUESTRADOR: main.py
FUNÇÃO: Gerador de Documentação Viva (Living Documentation).
DESCRIÇÃO: Varre a estrutura do projeto e atualiza todos os README.md automaticamente.
STATUS: Operacional - Modo Bibliotecário Sênior agora vai 
"""

import os
import re
import subprocess
from pathlib import Path

# --- CONFIGURAÇÕES DE IGNORAR ---
# Apenas lixo de sistema e controle de versão. Pastas de output SÃO PERMITIDAS.
DIRS_IGNORADOS = {'.venv', '__pycache__', '.git', '.idea', '.vscode'}

# --- 1. MANIFESTO DO PROJETO ---
MANIFESTO = """# 🛠️ ToolBox - Ecossistema de Agentes Autônomos

### 📂 Visão Geral e Arquitetura
Este repositório opera através de **Agentes Especializados** e uma infraestrutura de dados organizada por tipos e domínios.

* **Agentes de Dados:** Inteligência de busca, scraping e coleta de dados.
* **Agentes de Visao:** Processamento de imagem, higienização e privacidade.
* **Agentes de Voz:** Síntese vocal (TTS/XTTS) e inteligência auditiva.
* **Infraestrutura:** Gestão de logs, configurações e persistência de dados.

---
"""

# --- 2. STACK TECNOLÓGICO DETALHADO (RESTAURADO) ---
STACK_TECNOLOGICO = """
---
### 🛠️ Stack Tecnológico e Engenharia
- **Core Executivo:** Python 3.10+ & Bash Scripting (Automação de Infraestrutura).
- **Domínios de Inteligência:**
    - `Coqui TTS (XTTS v2)`: Clonagem de voz Neural e Síntese de Fala de alta fidelidade.
    - `Pillow (PIL)`: Pipeline de processamento de imagem e manipulação de metadados.
    - `Requests` & `BeautifulSoup4`: Engenharia de extração e consumo de dados.
- **Resiliência e Monitoramento:**
    - `Logging (RotatingFileHandler)`: Gestão de logs cíclicos com controle de volumetria.
    - `Subprocess`: Orquestração de comandos do sistema operacional (Fedora/Linux).
- **Arquitetura de Dados:**
    - **Persistência Estruturada:** Armazenamento em CSV (Séries) e JSON (Metadados).
    - **Estratégia de I/O:** Separação rigorosa entre `input_` (Matéria-prima) e `output_` (Processados).
    - **Living Documentation:** Mapeamento dinâmico via `main.py` (incluindo estruturas vazias via `.gitkeep`).
"""

# --- 3. DEFINIÇÕES POR DOMÍNIO ---
DEFINICOES = {
    "Agentes_Dados": "Coleta e processamento de notícias e oportunidades (Scraping/RSS).",
    "Agentes_Visao": "Processamento de imagens, filtros e remoção de metadados.",
    "Agentes_Voz": "Conversão de texto em fala (TTS/XTTS) e inteligência auditiva.",
    "Agentes_Monitor": "Monitoramento de integridade web e diagnóstico de hardware/OS.",
    "Scripts": "Utilitários de manutenção, backup e automação de infraestrutura.",
    "Config": "Cérebro do projeto (Settings, caminhos absolutos e variáveis).",
    "Data": "Repositório central organizado por subpastas (csv, json, images, audio).",
    "Logs": "Registro de atividades, histórico de erros e auditoria."
}

MAPA_MODULOS = {
    "Agentes_Dados": "### 🛰️ /Agentes_Dados",
    "Agentes_Visao": "### 👁️ /Agentes_Visao",
    "Agentes_Voz": "### 🎙️ /Agentes_Voz",
    "Agentes_Monitor": "### 🖥️ /Agentes_Monitor",
    "Scripts": "### 📜 /Scripts",
    "Data": "### 📊 /Data",
    "Logs": "### 📝 /Logs"
}

# --- 4. LÓGICA DE EXTRAÇÃO E AUDITORIA ---

def extrair_docstring(filepath):
    """Lê o cabeçalho do arquivo para explicar o que ele faz."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            conteudo = f.read()
            if filepath.endswith('.py'):
                match = re.search(r'"""(.*?)"""', conteudo, re.DOTALL)
                if match: return f" | *{match.group(1).strip().replace(chr(10), ' ')}*"
            elif filepath.endswith('.sh'):
                comentarios = []
                for l in conteudo.split('\n'):
                    if l.startswith('#') and '!' not in l:
                        comentarios.append(l.replace('#', '').strip())
                if comentarios: return f" | *{' '.join(comentarios[:1])}*"
    except: pass
    return ""

def get_git_info(filepath):
    """Pega a data da última modificação real no Git."""
    try:
        cmd = ['git', 'log', '-1', '--format=%cd', '--date=short', filepath]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return f"({result.stdout.strip()})" if result.stdout.strip() else "(Novo/Local)"
    except: return "(Local)"

def gerar_lista_arquivos(pasta_raiz, link_relativo=True):
    linhas = []
    
    # Varredura
    for root, dirs, files in os.walk(pasta_raiz):
        # Filtra pastas ignoradas
        dirs[:] = [d for d in dirs if d not in DIRS_IGNORADOS]
        
        for f in files:
            # Regra de Ouro: Ignora ocultos, EXCETO .gitkeep
            if f.startswith('.') and f != '.gitkeep': continue 
            if f == 'README.md': continue
            
            caminho_completo = os.path.join(root, f)
            nome_exibicao = os.path.relpath(caminho_completo, pasta_raiz)
            
            # Definição de Ícones e Descrições
            icone = "📄"
            info_git = get_git_info(caminho_completo)
            desc = extrair_docstring(caminho_completo)
            
            if f == '.gitkeep':
                icone = "📂"
                # Remove o nome .gitkeep da exibição para ficar mais limpo
                pasta_pai = os.path.dirname(nome_exibicao)
                nome_exibicao = f"{pasta_pai}/ (Estrutura)"
                desc = " | *Diretório de Output (Mantido via .gitkeep)*"
            elif f.endswith('.py'): icone = "🐍"
            elif f.endswith('.sh'): icone = "🐚"
            elif f.endswith(('.wav', '.mp3')): icone = "🔊"
            elif f.endswith(('.jpg', '.png')): icone = "🖼️"
            elif f.endswith('.json'): icone = "⚙️"
            
            # Cria o link Markdown
            prefixo = f"./{pasta_raiz}/" if not link_relativo else "./"
            # Se for gitkeep, o link aponta para a pasta
            link = f"{prefixo}{os.path.dirname(os.path.relpath(caminho_completo, pasta_raiz))}" if f == '.gitkeep' else f"{prefixo}{nome_exibicao}"
            
            if f == '.gitkeep':
                 linhas.append(f"- {icone} **[{nome_exibicao}]({link})** {desc}")
            else:
                 linhas.append(f"- {icone} **[{nome_exibicao}]({link})** {info_git}{desc}")

    return sorted(linhas) if linhas else ["- *Pasta vazia.*"]

# --- 5. EXECUÇÃO ---

def main():
    print(f"📚 Iniciando Bibliotecário ToolBox em: {os.getcwd()}")
    
    # 1. Gera o README.md Principal (Raiz)
    conteudo_raiz = MANIFESTO
    
    for pasta, header in MAPA_MODULOS.items():
        if os.path.exists(pasta):
            print(f"   - Indexando: {pasta}...")
            conteudo_raiz += f"\n{header}\n> {DEFINICOES.get(pasta, '')}\n\n"
            conteudo_raiz += "\n".join(gerar_lista_arquivos(pasta, link_relativo=False)) + "\n"
            
    conteudo_raiz += STACK_TECNOLOGICO
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(conteudo_raiz)
    
    # 2. Gera os READMEs Internos (Dentro de cada pasta)
    for pasta in DEFINICOES.keys():
        if os.path.exists(pasta):
            with open(os.path.join(pasta, "README.md"), 'w', encoding='utf-8') as f:
                f.write(f"# 📁 Módulo: {pasta}\n\n> {DEFINICOES[pasta]}\n\n## 🧰 Estrutura e Ferramentas\n")
                f.write("\n".join(gerar_lista_arquivos(pasta, link_relativo=True)))

    print("✅ Documentação Viva atualizada (Stack Sênior + Outputs)!")

if __name__ == "__main__":
    main()