#!/usr/bin/env python3
"""
FERRAMENTA: Agente Navegador Visual (Labs)
OBJETIVO: Preenchimento de formulário usando Visão Computacional + Pandas.
APRENDIZADO: Ancoragem visual (Image Rec) vs. Coordenadas fixas.
"""
import sys
import time
import pyautogui
import pandas as pd
import webbrowser
from pathlib import Path

# --- 1. Configuração do Ambiente (Manual e Transparente) ---
# Define onde estamos para importar módulos vizinhos se precisar
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

# Caminhos diretos (Sem abstração excessiva para você ver o que está acontecendo)
ARQUIVO_CSV = BASE_DIR / "Data" / "csv" / "produtos_automacao_formulario2.csv"
PASTA_IMAGENS = BASE_DIR / "Data" / "ui_assets"

# Configurações do Robô
CONFIDENCE_LEVEL = 0.8  # Precisa ser 80% igual à imagem
pyautogui.PAUSE = 0.5   # Pausa entre comandos para não atropelar

def esperar_e_clicar(nome_imagem, timeout=10, offset_y=0):
    """
    Tenta encontrar a imagem na tela. 
    Se achar: Clica (com ajuste vertical opcional) e retorna True.
    Se não achar: Retorna False.
    """
    img_path = str(PASTA_IMAGENS / nome_imagem)
    inicio = time.time()
    
    while (time.time() - inicio) < timeout:
        try:
            # Procura o centro da imagem na tela
            pos = pyautogui.locateCenterOnScreen(img_path, confidence=CONFIDENCE_LEVEL, grayscale=True)
            if pos:
                pyautogui.click(pos.x, pos.y + offset_y)
                return True
        except:
            pass # Continua tentando até o tempo acabar
        
        time.sleep(0.5)
    
    return False

# --- 2. Início da Execução (O Lab) ---
print(f"🔧 [ToolBox] Iniciando Agente Visual...")

# Carregamento e Limpeza dos Dados (Pandas Vectorizado)
try:
    print(f"   📂 Lendo CSV: {ARQUIVO_CSV.name}...", end=" ")
    df = pd.read_csv(ARQUIVO_CSV)
    
    # Tratamento de dados (Aprendizado: Fazer antes do loop é mais rápido)
    df = df.fillna("") # Tira os NaNs
    # Converte colunas numéricas para string trocando ponto por vírgula
    for col in ["preco_unitario", "custo"]:
        df[col] = df[col].astype(str).str.replace(".", ",", regex=False)
        
    print("OK!")
except Exception as e:
    print(f"\n❌ Erro ao abrir CSV: {e}")
    exit()

# Abrir Navegador
site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
try:
    webbrowser.get('firefox').open(site)
except:
    print(f"\n❌ Erro ao abrir CSV: {e}")
    exit()
    
# Login (Uso prático da Visão)
print("   👁️  Procurando campo de login...")
if esperar_e_clicar("campo_email_automatizar_visual.png", offset_y=35):
    pyautogui.write("hackeando_hashtag@gmail.com")
    pyautogui.press("tab")
    pyautogui.write("senha_hacker")
    pyautogui.press("tab")
    pyautogui.press("enter")
else:
    print("❌ Falha: Não encontrei o campo de email. (Verifique o arquivo .png)")
    exit()

# Loop de Cadastro
print("   🚀 Iniciando cadastro em lote...")
time.sleep(2) # Espera login carregar

for i, linha in df.iterrows():
    # Sincronia: Garante que estamos na tela certa antes de digitar
    # Se não achar a imagem, tenta um TAB de segurança
    if not esperar_e_clicar("campo_codigo_automatizar_visual.png", timeout=5, offset_y=35):
        pyautogui.press("tab")

    # Preenchimento (Dados já limpos lá em cima)
    pyautogui.write(str(linha["codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(linha["marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(linha["tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(linha["categoria"]))
    pyautogui.press("tab")
    pyautogui.write(linha["preco_unitario"])
    pyautogui.press("tab")
    pyautogui.write(linha["custo"])
    pyautogui.press("tab")
    
    if linha["obs"]:
        pyautogui.write(str(linha["obs"]))
    pyautogui.press("tab")
    
    pyautogui.press("enter") # Enviar
    pyautogui.press("pgup")  # Voltar ao topo
    
    print(f"      Item {i+1} cadastrado.")

print("✅ Processo finalizado.")