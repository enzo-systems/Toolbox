#!/usr/bin/env python3
# --- DOCSTRINGS --- 
"""
NÍVEL 3: Processador de Visão Computacional
FUNÇÃO: Análise, redimensionamento e extração de metadados de imagens.
CONCEITOS: Pillow, Filtros de Imagem, Manipulação de Matrizes.
"""
import sys
from PIL import Image, ImageOps, ImageDraw

# Função que converte uma imagem
def criar_foto_linkedin(caminho_entrada, caminho_saida="minha_foto_convertida.png"):
    print(f"Processando: {caminho_entrada}...")
    
    try:
        # 1. Carregar e corrigir rotação (Exif)
        img = Image.open(caminho_entrada)
        img = ImageOps.exif_transpose(img)
        img = img.convert("RGBA")
        
        # 2. Zoom Out (Padding) - SEU VALOR PREFERIDO: 0.20
        # Cria uma borda branca para o rosto não ficar colado na lente
        fator_zoom = 0.20 
        borda = int(min(img.size) * fator_zoom)
        img_com_borda = ImageOps.expand(img, border=borda, fill='white')

        # 3. Corte Quadrado Inteligente
        min_lado = min(img_com_borda.size)
        tamanho_quadrado = (min_lado, min_lado)
        
        # Centro equilibrado (Testa/Queixo)
        # 0.5 = Centro Horizontal | 0.35 = Um pouco acima do centro vertical (Olhos)
        img_quadrada = ImageOps.fit(img_com_borda, tamanho_quadrado, centering=(0.5, 0.35))
        
        # 4. Máscara Circular
        mascara = Image.new('L', tamanho_quadrado, 0)
        draw = ImageDraw.Draw(mascara)
        draw.ellipse((0, 0) + tamanho_quadrado, fill=255)
        img_quadrada.putalpha(mascara)

        # 5. Redimensionamento e Compressão (Padrão Web/LinkedIn)
        print("Redimensionando para 500x500px (Otimizado)...")
        img_final = img_quadrada.resize((500, 500), Image.Resampling.LANCZOS)

        # 6. Salvar
        if not caminho_saida.lower().endswith('.png'):
            caminho_saida += ".png"
            
        # optimize=True compacta o PNG sem perder qualidade visível
        img_final.save(caminho_saida, "PNG", optimize=True, compress_level=9)
        
        print(f"\n✅ SUCESSO! Foto salva em: {caminho_saida}")
        print("Pronta para upload.")

    except Exception as e:
        print(f"\n❌ Erro: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Pega o nome do arquivo que você digitou no terminal
        criar_foto_linkedin(sys.argv[1])
    else:
        print("--- Como usar ---")
        print("python3 corta_foto.py sua_foto.jpg")
