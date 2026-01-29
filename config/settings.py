# config/settings.py
import os
from pathlib import Path

# Resolve a Raiz do Projeto (Onde está o .git)
# Lógica: Arquivo atual -> Pai (Config) -> Pai (Raiz)
BASE_DIR = Path(__file__).resolve().parent.parent

# Caminhos Absolutos Dinâmicos
DATA_DIR = BASE_DIR / "data"
LOGS_DIR = BASE_DIR / "logs"
AGENTS_DIR = BASE_DIR / "agents"

# Garante que os diretórios existam (Idempotência)
DATA_DIR.mkdir(exist_ok=True)
LOGS_DIR.mkdir(exist_ok=True)