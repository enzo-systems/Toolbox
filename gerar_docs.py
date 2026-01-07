
"""
Docstring -
ROBÔ: ARQUITETO DE DOCS (V2.1 - Clean)
FUNÇÃO: Padronização total da estrutura e remoção de poluição visual.
STATUS: Ativo e funcional - Nível 1
"""

import os
import re
import subprocess 

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
                if match:
                    return f" | *{match.group(1).strip().replace('\n', ' ')}*"
            elif filepath.endswith('.sh'):
                linhas = conteudo.split('\n')
                for linha in linhas:
                    # Pega a primeira linha de comentário que não seja a shebang
                    if linha.startswith('#') and '!' not in linha and len(linha.strip()) > 1:
                        clean_comment = linha.replace('#', '').replace('=', '').strip()
                        if clean_comment:
                            return f" | *{clean_comment}*"
    except: pass
    return ""

def get_git_info(filepath):
    try:
        cmd = ['git', 'log', '-1', '--format=%s (%cd)', '--date=short', filepath]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout.strip() if result.stdout.strip() else "Novo arquivo"
    except: return "Erro Git"

def gerar_lista_arquivos(pasta):
    linhas = []
    if os.path.exists(pasta):
        # Filtramos arquivos que realmente importam para a documentação
        extensoes = ('.py', '.sh', '.yml', '.json')
        arquivos = sorted([f for f in os.listdir(pasta) if f.endswith(extensoes) and f != 'README.md'])
        
        for arq in arquivos:
            caminho = os.path.join(pasta, arq)
            if os.path.exists(caminho):
                git_info = get_git_info(caminho)
                descricao = extrair_docstring(caminho)
                
                # Se for um .gitkeep ou arquivo sem descrição, colocamos um padrão
                if not descricao and arq == '.gitkeep':
                    continue # Ignora o .gitkeep na listagem visual
                
                linhas.append(f"- **[{arq}](./{pasta}/{arq})**: {git_info}{descricao}")
    
    return linhas if linhas else ["- *Pasta estruturada (aguardando arquivos de sistema).*"]

def main():
    if not os.path.exists('README.md'): return
    
    with open('README.md', 'r', encoding='utf-8') as f:
        conteudo = f.read()

    for pasta, header in MAPA_MODULOS.items():
        if header in conteudo:
            lista = gerar_lista_arquivos(pasta)
            # Regex para substituir tudo entre o cabeçalho e a próxima seção ou fim do arquivo
            pattern = re.compile(rf"({re.escape(header)}.*?)(\n###|\Z)", re.DOTALL)
            nova_secao = f"{header}\n" + "\n".join(lista) + "\n"
            conteudo = pattern.sub(rf"{nova_secao}\2", conteudo)

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(conteudo)
    print("✅ README.md limpo e atualizado!")

if __name__ == "__main__":
    main()