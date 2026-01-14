#!/usr/bin/env python3
"""
NÍVEL 3: Agente Navegador Visual (Integrado ao ToolBox)
LOCAL: ~/Projetos/ToolBox/Agentes_Navegador/bot_formulario_visual.py
"""
import sys
import time
import pyautogui
import pandas as pd
import webbrowser
from pathlib import Path

# --- Configuração de Caminhos (Dinâmica e à prova de falhas) ---
# O arquivo está em ToolBox/Agentes_Navegador
BASE_DIR = Path(__file__).resolve().parent.parent 
# Agora BASE_DIR = ~/Projetos/ToolBox

# Ajuste conforme o que tem dentro da sua pasta Data (csv ou inputs)
ARQUIVO_CSV = BASE_DIR / "Data" / "csv" / "produtos_automacao_formulario.csv"
PASTA_IMAGENS = BASE_DIR / "Data" / "ui_assets"

# Se a pasta Config for usada no futuro, ela já está mapeada
sys.path.append(str(BASE_DIR))

# --- Configurações Visuais ---
CONFIDENCE_LEVEL = 0.7 
pyautogui.PAUSE = 0.5

def esperar_e_clicar(nome_imagem, tempo_limite=20, offset_x=0, offset_y=0):
    """Busca visual com timeout e offset."""
    caminho_img = str(PASTA_IMAGENS / nome_imagem)
    inicio = time.time()
    
    while True:
        try:
            localizacao = pyautogui.locateCenterOnScreen(caminho_img, confidence=CONFIDENCE_LEVEL, grayscale=True)
            if localizacao:
                x, y = localizacao
                pyautogui.click(x + offset_x, y + offset_y)
                return True
        except pyautogui.ImageNotFoundException:
            pass 
        except Exception:
            pass # Ignora erros pontuais de leitura

        if time.time() - inicio > tempo_limite:
            return False
        time.sleep(0.5)

# --- EXECUÇÃO ---
print(f"🔧 [KERNEL] Iniciando processo em: {BASE_DIR}")

# 1. Carregamento e Higienização Inteligente (A Maestria com Pandas)
try:
    print("   📂 Lendo e tratando dados...", end=" ")
    tabela = pd.read_csv(ARQUIVO_CSV)
    
    # Tratamento em lote (muito mais rápido que fazer no loop)
    tabela["obs"] = tabela["obs"].fillna("") 
    tabela["custo"] = tabela["custo"].fillna(0)
    
    # Converte colunas numéricas para string e ajusta vírgula de uma vez
    cols_numericas = ["preco_unitario", "custo"]
    for col in cols_numericas:
        tabela[col] = tabela[col].astype(str).str.replace(".", ",", regex=False)
        
    print("Feito!")
except FileNotFoundError:
    print(f"\n❌ Erro Crítico: Não achei o CSV em: {ARQUIVO_CSV}")
    print("   Verifique se a pasta 'csv' existe dentro de 'Data'.")
    exit()

# 2. Navegador
site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
try:
    webbrowser.get('firefox').open(site)
except:
    webbrowser.open(site)
    
# 3. Login
if esperar_e_clicar("campo_email_automatizar_visual.png", offset_y=35):
    pyautogui.write("hackeando_hashtag@gmail.com")    
    pyautogui.press("tab")
    pyautogui.write("senha_hacker")
    pyautogui.press("tab")
    pyautogui.press("enter")
else:
    print("❌ Falha no Login: Campo não encontrado.")
    exit()

# 4. Loop de Preenchimento (Agora limpo e rápido)
for i, linha in enumerate(tabela.index):
    print(f"   📝 Processando item {i+1}/{len(tabela)}", end="\r")
    
    # Sincronia Visual (Ancoragem)
    if not esperar_e_clicar("campo_codigo_automatizar_visual.png", tempo_limite=3, offset_y=35):
        pyautogui.press("tab") # Fallback se a visão falhar
    
    # Preenchimento (Dados já estão limpos)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    
    pyautogui.write(tabela.loc[linha, "preco_unitario"]) # Já formatado
    pyautogui.press("tab")
    
    pyautogui.write(tabela.loc[linha, "custo"]) # Já formatado
    pyautogui.press("tab")
    
    obs = tabela.loc[linha, "obs"]
    if obs:
       pyautogui.write(str(obs))
    pyautogui.press("tab")
    
    pyautogui.press("enter")
    pyautogui.press("pgup")
    time.sleep(0.5)

print("\n✅ Automação Finalizada com Sucesso.")