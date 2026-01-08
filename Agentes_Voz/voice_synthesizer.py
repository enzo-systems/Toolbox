#!/usr/bin/env python3
"""
NÍVEL 4: Sintetizador de Inteligência Auditiva (Voice Cloner)
FUNÇÃO: Processamento de áudio e síntese vocal (TTS) com auto-conversão de formatos.
CONCEITOS: DSP, Wrappers de FFmpeg, Pipeline de Áudio Automatizado.
"""

import sys
import os
import subprocess
import shutil
from pathlib import Path
# [NOVO] Aceite automático da licença para não travar o robô
os.environ["COQUI_TOS_AGREED"] = "1"
import torch
from TTS.api import TTS

# --- BOOTSTRAP: CONEXÃO COM O SETTINGS ---
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.append(str(BASE_DIR))

try:
    from Config.settings import DIRS
    DIR_ENTRADA = DIRS["IN_VOICE"]   # Data/input_audio
    DIR_SAIDA = DIRS["OUT_VOICE"]    # Data/output_audio
except ImportError:
    # Fallback
    DIR_ENTRADA = BASE_DIR / "Data" / "input_audio"
    DIR_SAIDA = BASE_DIR / "Data" / "output_audio"

# Garante infraestrutura
DIR_ENTRADA.mkdir(parents=True, exist_ok=True)
DIR_SAIDA.mkdir(parents=True, exist_ok=True)

# --- CONFIGURAÇÃO DE ARQUIVOS ---
NOME_ROTEIRO = "roteiro.txt"
NOME_REF_M4A = "referencia.m4a"
NOME_REF_WAV = "referencia.wav"
NOME_FINAL = "audio_clonado_final.wav"

def preparar_audio_referencia():
    """Converte M4A para WAV automaticamente se necessário."""
    caminho_m4a = DIR_ENTRADA / NOME_REF_M4A
    caminho_wav = DIR_ENTRADA / NOME_REF_WAV

    # Se já tem o WAV, beleza.
    if caminho_wav.exists():
        print(f"✅ Áudio de referência (WAV) encontrado: {caminho_wav.name}")
        return caminho_wav

    # Se não tem WAV, mas tem M4A, converte.
    if caminho_m4a.exists():
        print(f"🔄 Convertendo {caminho_m4a.name} para WAV...")
        try:
            comando = [
                'ffmpeg', '-i', str(caminho_m4a), 
                str(caminho_wav), '-y', '-loglevel', 'error'
            ]
            subprocess.run(comando, check=True)
            print("✅ Conversão concluída com sucesso.")
            return caminho_wav
        except Exception as e:
            print(f"❌ Erro ao converter áudio (Você tem ffmpeg instalado?): {e}")
            return None
            
    print(f"❌ ERRO: Nenhum arquivo de voz encontrado em {DIR_ENTRADA}")
    print(f"   👉 Coloque '{NOME_REF_M4A}' ou '{NOME_REF_WAV}' lá.")
    return None

def ler_roteiro():
    caminho_roteiro = DIR_ENTRADA / NOME_ROTEIRO
    if not caminho_roteiro.exists():
        print(f"❌ Roteiro não encontrado: {caminho_roteiro}")
        print(f"   👉 Crie um arquivo '{NOME_ROTEIRO}' em {DIR_ENTRADA}")
        return None
    
    with open(caminho_roteiro, "r", encoding="utf-8") as f:
        return f.read()

def processar_sintese():
    print("🎬 Iniciando Estúdio de Voz (V4 - Auto)...")
    
    # 1. Preparação de Arquivos
    arquivo_ref = preparar_audio_referencia()
    if not arquivo_ref: return

    texto_bruto = ler_roteiro()
    if not texto_bruto: return

    # 2. Processamento de Texto
    texto_limpo = texto_bruto.replace("\n", " ")
    frases = [f.strip() for f in texto_limpo.replace("!", ".").replace("?", ".").split(".") if len(f.strip()) > 2]
    
    print(f"✂️  Roteiro dividido em {len(frases)} blocos.")

    # 3. Carregar IA
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"⏳ Carregando modelo XTTS (Dispositivo: {device})...")
    try:
        tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
    except Exception as e:
        print(f"❌ Erro ao carregar modelo TTS: {e}")
        return

    # 4. Geração em Loop
    pasta_temp = DIR_SAIDA / "temp_parts"
    pasta_temp.mkdir(exist_ok=True)
    
    arquivos_gerados = []
    print("🎙️  Gravando...")

    for i, frase in enumerate(frases):
        caminho_temp = pasta_temp / f"parte_{i:03d}.wav"
        print(f"   [{i+1}/{len(frases)}] Sintetizando: \"{frase[:30]}...\"")
        
        try:
            tts.tts_to_file(
                text=frase,
                speaker_wav=str(arquivo_ref),
                language="pt",
                file_path=str(caminho_temp)
            )
            arquivos_gerados.append(caminho_temp)
        except Exception as e:
            print(f"   ⚠️ Falha no bloco {i}: {e}")

    # 5. Unificação (Merge)
    if arquivos_gerados:
        print("🔗 Unificando áudios...")
        caminho_lista = pasta_temp / "lista_files.txt"
        caminho_final = DIR_SAIDA / NOME_FINAL
        
        with open(caminho_lista, "w") as f:
            for arq in arquivos_gerados:
                f.write(f"file '{arq.name}'\n")
        
        # Comando FFmpeg para concatenar
        cmd = f"ffmpeg -f concat -safe 0 -i {caminho_lista} -c copy {caminho_final} -y -loglevel error"
        
        # Executa comando no diretório da pasta temporária para evitar problemas de path
        subprocess.run(cmd, shell=True, cwd=pasta_temp)
        
        # Limpeza
        shutil.rmtree(pasta_temp)
        print(f"\n✅ SUCESSO ABSOLUTO!\n   🎧 Ouça agora: {caminho_final}")
    else:
        print("❌ Nenhum áudio foi gerado.")

if __name__ == "__main__":
    processar_sintese()