#!/usr/bin/env python3
# --- DOCSTRINGS --- 
"""
NÍVEL 4: Sintetizador de Inteligência Auditiva
FUNÇÃO: Processamento de áudio e síntese vocal para interfaces.
CONCEITOS: DSP (Digital Signal Processing), TTS (Text-to-Speech), Waveform.
"""

import torch
from TTS.api import TTS
import os
import subprocess

#ffmpeg -i referencia.m4a referencia.wav <<-- transforma extensao do audio
#python robo_enzo.py <<cria o audio do roteiro.
#aplay resultado.wav  <<<comando para ouvir o audio

# --- Configurações ---
ARQUIVO_ROTEIRO = "roteiro.txt"
ARQUIVO_REF = "referencia.wav"
ARQUIVO_FINAL = "audio_final.wav"
PASTA_TEMP = "temp_audios"

# Limpa a tela
os.system('clear')
print("🎬 Iniciando Estúdio Enzo V3 (Modo Longo)...")

# 1. Preparação
if not os.path.exists(ARQUIVO_ROTEIRO):
    print(f"❌ Erro: O arquivo {ARQUIVO_ROTEIRO} não existe!")
    exit()

# Cria pasta temporária para guardar os pedaços
os.makedirs(PASTA_TEMP, exist_ok=True)

# 2. Carregar Texto e Limpar
print("📖 Lendo o roteiro...")
with open(ARQUIVO_ROTEIRO, "r", encoding="utf-8") as f:
    texto_bruto = f.read()

# Estratégia de Quebra: Divide por pontuação para não estourar o limite
# Substitui quebras de linha por espaços para fluidez
texto_limpo = texto_bruto.replace("\n", " ")
frases = []
# Divide por pontos finais, exclamações e interrogações
raw_sentences = texto_limpo.replace("!", ".").replace("?", ".").split(".")

for frase in raw_sentences:
    f = frase.strip()
    if len(f) > 2: # Ignora frases vazias ou muito curtas
        frases.append(f)

print(f"✂️  Texto dividido em {len(frases)} partes para processamento.")

# 3. Carregar IA
device = "cpu"
print("⏳ Carregando o modelo XTTS...")
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

# 4. Loop de Geração (Frase por Frase)
arquivos_gerados = []

print("🎙️  Começando a gravação em partes...")
for i, frase in enumerate(frases):
    nome_arquivo = os.path.join(PASTA_TEMP, f"parte_{i:03d}.wav")
    print(f"   [{i+1}/{len(frases)}] Processando: \"{frase[:30]}...\"")
    
    try:
        tts.tts_to_file(
            text=frase,
            speaker_wav=ARQUIVO_REF,
            language="pt",
            file_path=nome_arquivo
        )
        arquivos_gerados.append(nome_arquivo)
    except Exception as e:
        print(f"   ⚠️ Erro na frase {i}: {e}")

# 5. Juntar tudo com FFmpeg
print("🔗 Unindo os arquivos de áudio...")

# Cria lista para o ffmpeg ler
lista_ffmpeg = "lista_para_unir.txt"
with open(lista_ffmpeg, "w") as f:
    for arquivo in arquivos_gerados:
        f.write(f"file '{arquivo}'\n")

# Comando do sistema para unir
comando = f"ffmpeg -f concat -safe 0 -i {lista_ffmpeg} -c copy {ARQUIVO_FINAL} -y -loglevel error"
os.system(comando)

# Limpeza da bagunça
os.remove(lista_ffmpeg)
import shutil
shutil.rmtree(PASTA_TEMP) # Remove a pasta de pedaços

print("------------------------------------------------")
print(f"✅ SUCESSO! Áudio final salvo como: {ARQUIVO_FINAL}")
print("------------------------------------------------")
