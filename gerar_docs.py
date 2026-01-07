
"""
Docstring -
ROBÔ: ARQUITETO DE DOCS (V2.1 - Clean)
FUNÇÃO: Padronização total da estrutura e remoção de poluição visual.
STATUS: Ativo e funcional - Nível 1
"""

import os
import re
import subprocess

# --- Configurações de Identidade Sênior ---
DEFINICOES = {
    "Robos": "Agentes autônomos e scripts de monitoramento/extração de dados (Nível 2).",
    "Scripts": "Utilitários de Automação de Infraestrutura e Manutenção de Sistema (Nível 1).",
    "Config": "Gestor de Parâmetros, Variáveis de Ambiente e Definições Globais (Nível 1).",
    "Docker": "Orquestrador de Containers e Ambientes Isolados (Nível 1).",
    "Docs": "Repositório de Documentação Técnica e Manuais do Projeto.",
    "Logs": "Registro de Atividades, Históricos e Depuração de Processos.",
    "Imagens": "Módulos de Processamento Visual e Manipulação de Imagens (Nível 3).",
    "CloneVoz": "Módulos de Processamento de Áudio e Síntese Vocal."
}

MAPA_MODULOS = {
    "Robos": "### 🤖 /Robos",
    "Scripts": "### 📂 /Scripts",
    "Config": "### ⚙️ /Config",
    "Docker": "### 🐳 /Docker",
    "Docs": "### 📚 /Docs",
    "Logs": "### 📝 /Logs",
    "Imagens": "### 🖼️ /Imagens",
    "CloneVoz": "### 🎙️ /CloneVoz"
}

def extrair_docstring(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            conteudo = f.read()
            if filepath.endswith('.py'):
                match = re.search(r'"""(.*?)"""', conteudo, re.DOTALL)
                if match: return f" | *{match.group(1).strip().replace('\n', ' ')}*"
            elif filepath.endswith('.sh'):
                linhas = conteudo.split('\n')
                for l in linhas:
                    if l.startswith('#') and '!' not in l and len(l) > 5:
                        return f" | *{l.replace('#', '').strip()}*"
    except: pass
    return ""

def get_git_info(filepath):
    try:
        cmd = ['git', 'log', '-1', '--format=%s (%cd)', '--date=short', filepath]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout.strip() if result.stdout.strip() else "Novo arquivo"
    except: return "Erro Git"

def gerar_lista_arquivos(pasta, link_relativo=True):
    linhas = []
    if os.path.exists(pasta):
        extensoes = ('.py', '.sh', '.json', '.yml')
        arquivos = sorted([f for f in os.listdir(pasta) if f.endswith(extensoes) and f != 'README.md'])
        for arq in arquivos:
            caminho_arq = os.path.join(pasta, arq)
            git_info = get_git_info(caminho_arq)
            desc = extrair_docstring(caminho_arq)
            prefixo = f"./{pasta}/" if not link_relativo else "./"
            linhas.append(f"- **[{arq}]({prefixo}{arq})**: {git_info}{desc}")
    return linhas if linhas else ["- *Pasta organizada (aguardando módulos).*"]

def atualizar_readme_principal():
    if not os.path.exists('README.md'): return
    with open('README.md', 'r', encoding='utf-8') as f:
        conteudo = f.read()

    for pasta, header in MAPA_MODULOS.items():
        if header in conteudo:
            definicao = DEFINICOES.get(pasta, "")
            lista = gerar_lista_arquivos(pasta, link_relativo=False)
            
            # Monta o bloco: Cabeçalho + Definição + Lista
            nova_secao = f"{header}\n{definicao}\n" + "\n".join(lista) + "\n"
            
            # Regex para substituir até o próximo cabeçalho ou fim do arquivo
            pattern = re.compile(rf"({re.escape(header)}.*?)(\n###|\n---|\Z)", re.DOTALL)
            conteudo = pattern.sub(rf"{nova_secao}\2", conteudo)

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(conteudo)
    print("✅ README.md Principal atualizado com definições técnicas.")

def atualizar_readmes_subpastas():
    for pasta in DEFINICOES.keys():
        if os.path.exists(pasta):
            caminho_readme = os.path.join(pasta, "README.md")
            conteudo = f"# 📁 /{pasta}\n\n> {DEFINICOES[pasta]}\n\n## 📜 Arquivos\n"
            conteudo += "\n".join(gerar_lista_arquivos(pasta, link_relativo=True))
            with open(caminho_readme, 'w', encoding='utf-8') as f:
                f.write(conteudo)
            print(f"✅ Sub-README /{pasta} atualizado.")

def main():
    atualizar_readme_principal()
    atualizar_readmes_subpastas()

if __name__ == "__main__":
    main()