"""
ROBÔ: ARQUITETO DE DOCS (V2 - Nível 2)
FUNÇÃO: Lê metadados do Git e Docstrings para auto-gerar READMEs.
CORREÇÃO: Inclusão das pastas de infraestrutura e reconhecimento de Scripts Bash.
"""

import os
import re
import subprocess

# --- Configurações Atualizadas (Incluindo a nova estrutura) ---
MAPA_MODULOS = {
    "Robos": {"root": r"### 🤖 /Robos", "sub": r"## 📜 Lista de Scripts"},
    "Scripts": {"root": r"### 📂 /Scripts", "sub": r"## 📜 Lista de Scripts"},
    "Config": {"root": r"### ⚙️ /Config", "sub": r"## 📜 Configurações"},
    "Docker": {"root": r"### 🐳 /Docker", "sub": r"## 📜 Infraestrutura"},
    "Docs": {"root": r"### 📚 /Docs", "sub": r"## 📜 Documentação"},
    "Logs": {"root": r"### 📝 /Logs", "sub": r"## 📜 Registros"}
}

def extrair_docstring(filepath):
    """Lê a descrição inicial de arquivos .py ou comentários iniciais de .sh"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            conteudo = f.read()
            # Para Python (aspas triplas)
            if filepath.endswith('.py'):
                match = re.search(r'"""(.*?)"""', conteudo, re.DOTALL)
                if match:
                    return f" | *{match.group(1).strip().replace('\n', ' ')}*"
            # Para Bash/Shell (primeiras linhas de comentário após a Shebang)
            elif filepath.endswith('.sh'):
                linhas = conteudo.split('\n')
                for linha in linhas:
                    if linha.startswith('#') and '!' not in linha and len(linha) > 5:
                        return f" | *{linha.replace('#', '').strip()}*"
    except Exception:
        pass
    return ""

def get_git_info(filepath):
    """Pega a última mensagem de commit do Git."""
    try:
        cmd = ['git', 'log', '-1', '--format=%s (%cd)', '--date=short', filepath]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
        return "Novo arquivo (Aguardando commit)"
    except Exception:
        return "Erro ao ler Git"

def gerar_lista_arquivos(pasta):
    """Gera lista Markdown incluindo .py, .sh, .json e .md"""
    linhas = []
    if os.path.exists(pasta):
        # Agora busca .py, .sh, .json e .md (exceto o próprio README)
        extensoes_permitidas = ('.py', '.sh', '.json', '.md')
        arquivos = sorted([f for f in os.listdir(pasta) if f.endswith(extensoes_permitidas) and f != 'README.md'])
        
        for arquivo in arquivos:
            caminho_completo = os.path.join(pasta, arquivo)
            git_info = get_git_info(caminho_completo)
            descricao = extrair_docstring(caminho_completo)
            linhas.append(f"- **[{arquivo}](./{pasta}/{arquivo})**: {git_info}{descricao}")
    
    if not linhas:
        return ["- *Pasta estruturada (aguardando arquivos de sistema).*"]
    return linhas

def atualizar_conteudo(texto_original, header_regex, nova_lista_linhas):
    """Substitui o conteúdo entre o cabeçalho e a próxima seção."""
    pattern = re.compile(f"({header_regex}.*?)(?=\n###|\\Z)", re.DOTALL)
    match = pattern.search(texto_original)
    if not match: return texto_original

    bloco_inteiro = match.group(1)
    # Busca onde começa a lista de arquivos para preservar o texto de introdução do cabeçalho
    divisao = re.search(r"(?=\n- )", bloco_inteiro)
    
    texto_intro = bloco_inteiro[:divisao.start()].strip() if divisao else bloco_inteiro.strip()
    novo_bloco = f"{texto_intro}\n" + "\n".join(nova_lista_linhas) + "\n"
    return texto_original.replace(bloco_inteiro, novo_bloco)

def main():
    # 1. Atualizar README Principal (Raiz)
    if os.path.exists('README.md'):
        with open('README.md', 'r', encoding='utf-8') as f:
            conteudo_root = f.read()
        
        modificou_root = False
        for pasta, headers in MAPA_MODULOS.items():
            # Só tenta atualizar se o cabeçalho existir no README
            if headers["root"] in conteudo_root:
                lista = gerar_lista_arquivos(pasta)
                novo_conteudo = atualizar_conteudo(conteudo_root, headers["root"], lista)
                if novo_conteudo != conteudo_root:
                    conteudo_root = novo_conteudo
                    modificou_root = True
        
        if modificou_root:
            with open('README.md', 'w', encoding='utf-8') as f:
                f.write(conteudo_root)
            print("✅ README.md (Raiz) atualizado com a nova estrutura de pastas.")

    # 2. Atualizar READMEs das Subpastas (Opcional, se existirem)
    for pasta, headers in MAPA_MODULOS.items():
        sub_readme = os.path.join(pasta, 'README.md')
        if os.path.exists(sub_readme):
            with open(sub_readme, 'r', encoding='utf-8') as f:
                conteudo_sub = f.read()
            lista = gerar_lista_arquivos(pasta)
            lista_local = [l.replace(f"./{pasta}/", "") for l in lista]
            novo_conteudo_sub = atualizar_conteudo(conteudo_sub, headers["sub"], lista_local)
            with open(sub_readme, 'w', encoding='utf-8') as f:
                f.write(novo_conteudo_sub)
            print(f"✅ {sub_readme} atualizado.")

if __name__ == "__main__":
    main()