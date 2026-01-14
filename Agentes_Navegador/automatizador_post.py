#!/usr/bin/env python3
"""
NÍVEL 4: Agente de Protocolo HTTP (Requests)
TÁTICA: Bypass de Interface Gráfica (Headless).
OBJETIVO: Injeção direta de dados no servidor via POST Request.
VANTAGEM: Imune a resolução de tela, navegador ou lentidão gráfica.
"""
import sys
import requests
import pandas as pd
from pathlib import Path

# --- Configuração ---
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR)) # Para importar settings se precisar

ARQUIVO_CSV = BASE_DIR / "Data" / "csv" / "produtos_automacao_formulario2.csv"

# URLs do Alvo (Engenharia Reversa)
URL_LOGIN = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# OBS: Geralmente o endpoint de login é o mesmo da página, mas com método POST.
# Se falhar, verifique no F12 se o 'Action URL' é diferente.

def carregar_dados():
    try:
        print(f"📂 Lendo CSV...", end=" ")
        df = pd.read_csv(ARQUIVO_CSV)
        df = df.fillna("")
        # Normalização
        for col in ["preco_unitario", "custo"]:
            df[col] = df[col].astype(str).str.replace(".", ",", regex=False)
        print("OK!")
        return df
    except Exception as e:
        print(f"\n❌ Erro CSV: {e}")
        exit()

def executar_hack():
    # 1. Criar uma Sessão (O Segredo)
    # A session mantém os Cookies de autenticação automaticamente.
    # Sem isso, você loga, mas na próxima requisição o site "esquece" quem você é.
    client = requests.Session()

    # O Disfarce (User-Agent)
    # Faz o servidor achar que somos um Chrome no Linux, não um script Python.
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    client.headers.update(headers)

    # 2. Realizar Login
    print("🔓 Tentando autenticação via HTTP...", end=" ")
    
    # Payload de Login (Baseado no padrão HTML do site)
    payload_login = {
        "email": "hackeando_hashtag@gmail.com",
        "senha": "senha_hacker"
        # DICA: Se falhar, verifique no F12 se o nome do campo é 'email' mesmo.
    }
    
    response = client.post(URL_LOGIN, data=payload_login)
    
    # Verificação de Sucesso (Básica)
    # Se logar, geralmente ele redireciona ou muda o conteúdo.
    if response.status_code == 200 and "intensivao" in response.url:
        print("✅ Sucesso! Sessão capturada.")
    else:
        print(f"\n❌ Falha no login. Código: {response.status_code}")
        print("   Verifique se os nomes dos campos (email/senha) mudaram no F12.")
        # Debug: Descomente abaixo para ver o HTML que voltou
        # print(response.text) 
        # exit()

    # 3. Injeção de Dados (Cadastro)
    df = carregar_dados()
    URL_CADASTRO = "https://dlp.hashtagtreinamentos.com/python/intensivao/cadastrar"
    
    print(f"🚀 Iniciando injeção de {len(df)} pacotes...")

    sucessos = 0
    for i, linha in df.iterrows():
        # Monta o pacote de dados exato que o formulário enviaria
        payload_produto = {
            "codigo": linha["codigo"],
            "marca": linha["marca"],
            "tipo": linha["tipo"],
            "categoria": linha["categoria"],
            "preco_unitario": linha["preco_unitario"],
            "custo": linha["custo"],
            "obs": linha["obs"]
        }
        
        # Disparo silencioso
        resp = client.post(URL_CADASTRO, data=payload_produto)
        
        if resp.status_code == 200:
            sucessos += 1
            sys.stdout.write(f"\r   [Packet {i+1}/{len(df)}] ⚡ Enviado. Status: 200 OK")
            sys.stdout.flush()
        else:
            print(f"\n   ⚠️ Falha no item {i+1}: {resp.status_code}")

    print(f"\n\n🏁 Missão Cumprida. {sucessos} itens injetados via Backend.")

if __name__ == "__main__":
    executar_hack()