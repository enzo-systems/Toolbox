#!/usr/bin/env python3
"""
NÍVEL 3: Processador de Visão Computacional (Vision Processor)
FUNÇÃO: Higienização e formatação de fotos de perfil (LinkedIn Style) em lote.
CONCEITOS: Pillow, Pipeline de I/O, Processamento em Batch.
"""

import sys
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw

# --- BOOTSTRAP: CONEXÃO COM O SETTINGS ---
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.append(str(BASE_DIR))

try:
    from Config.settings import DIRS
    # MUDANÇA ESTRUTURAL:
    # input_images -> Onde você joga as fotos
    # output_images -> Onde o robô entrega o resultado
    DIR_ENTRADA = DIRS["IN_IMAGES"]
    DIR_SAIDA = DIRS["OUT_IMAGES"]
except ImportError:
    # Fallback seguro
    DIR_ENTRADA = BASE_DIR / "Data" / "input_images"
    DIR_SAIDA = BASE_DIR / "Data" / "output_images"

# Garante a infraestrutura física
DIR_ENTRADA.mkdir(parents=True, exist_ok=True)
DIR_SAIDA.mkdir(parents=True, exist_ok=True)

def processar_foto(caminho_arquivo):
    """Aplica a lógica de design (Corte Circular + Zoom)"""
    try:
        nome_arquivo = Path(caminho_arquivo).name
        print(f"   🖼️  Processando: {nome_arquivo}...", end=" ")
        
        img = Image.open(caminho_arquivo)
        img = ImageOps.exif_transpose(img) # Corrige rotação de celular
        img = img.convert("RGBA")
        
        # 1. Lógica de Zoom (Foco no rosto)
        fator_zoom = 0.20 
        borda = int(min(img.size) * fator_zoom)
        img_com_borda = ImageOps.expand(img, border=borda, fill='white')

        # 2. Corte Quadrado Centralizado (Foco 35% do topo)
        min_lado = min(img_com_borda.size)
        tamanho_quadrado = (min_lado, min_lado)
        img_quadrada = ImageOps.fit(img_com_borda, tamanho_quadrado, centering=(0.5, 0.35))
        
        # 3. Máscara Circular (Alpha Channel)
        mascara = Image.new('L', tamanho_quadrado, 0)
        draw = ImageDraw.Draw(mascara)
        draw.ellipse((0, 0) + tamanho_quadrado, fill=255)
        img_quadrada.putalpha(mascara)

        # 4. Resize final e Salvamento
        img_final = img_quadrada.resize((500, 500), Image.Resampling.LANCZOS)
        
        nome_saida = f"perfil_{Path(nome_arquivo).stem}.png"
        caminho_final = DIR_SAIDA / nome_saida
        
        img_final.save(caminho_final, "PNG", optimize=True)
        print(f"✅ Feito!")
        return True

    except Exception as e:
        print(f"❌ Falha: {e}")
        return False

def executar_pipeline():
    print(f"👁️  [Vision Processor] Monitorando esteira: {DIR_ENTRADA}")
    
    # Extensões suportadas
    extensoes = ['*.jpg', '*.jpeg', '*.png', '*.webp']
    arquivos = []
    for ext in extensoes:
        arquivos.extend(DIR_ENTRADA.glob(ext))
    
    if not arquivos:
        print(f"💤 A pasta de entrada está vazia.")
        print(f"   👉 Dica: Coloque fotos em: {DIR_ENTRADA}")
        return

    print(f"🔎 Encontradas {len(arquivos)} imagens para processar.\n")
    
    sucessos = 0
    for arquivo in arquivos:
        if processar_foto(arquivo):
            sucessos += 1
            
    print(f"\n🚀 Processamento concluído. {sucessos}/{len(arquivos)} imagens geradas.")
    print(f"📂 Resultados disponíveis em: {DIR_SAIDA}")

if __name__ == "__main__":
    # Se passar argumento, processa só um. Se não, varre a pasta.
    if len(sys.argv) > 1:
        arquivo_alvo = Path(sys.argv[1])
        # Se o usuário passou só o nome, assumimos que está na pasta de input
        if not arquivo_alvo.exists():
            arquivo_alvo = DIR_ENTRADA / sys.argv[1]
        
        if arquivo_alvo.exists():
            print("👁️  Modo Manual Ativado")
            processar_foto(arquivo_alvo)
            print(f"📂 Saída: {DIR_SAIDA}")
        else:
            print(f"❌ Arquivo não encontrado: {arquivo_alvo}")
    else:
        executar_pipeline()