#!/usr/bin/env bash
# NÍVEL 1: Automação de Infraestrutura
# FUNÇÃO: Realiza o backup incremental e rotativo do repositório ToolBox.
# CONCEITOS: Shell Scripting, Gestão de Ciclo de Vida de Dados, Resiliência.

set -euo pipefail

# --- LOCALIZAÇÃO DINÂMICA ---
SCRIPTPATH="$(cd "$(dirname "$0")" && pwd)"
BASE_DIR="$(cd "$SCRIPTPATH/.." && pwd)"
BACKUP_DEST="$(cd "$BASE_DIR/.." && pwd)/.ToolBox_Backups"

# --- INTEGRAÇÃO COM LOGS (Padrão ToolBox) ---
LOG_FILE="$BASE_DIR/Logs/system_toolbox.log"

# Trap para erros
trap 'echo "❌ ERRO CRÍTICO na linha $LINENO em: $SCRIPTPATH" | tee -a "$LOG_FILE"' ERR

# ==============================================================================
# EXECUÇÃO
# ==============================================================================

echo "🚀 [Nível 1] Iniciando protocolo de backup..."
mkdir -p "$BACKUP_DEST"

TIMESTAMP=$(date +"%Y-%m-%d_%H%M%S")
FILENAME="toolbox_backup_$TIMESTAMP.tar.gz"

echo "📦 Compactando módulos da Arquitetura (incluindo Data)..."

# Incluímos 'Data' na lista, pois é onde residem os resultados dos seus robôs
tar -czf "$BACKUP_DEST/$FILENAME" \
    -C "$BASE_DIR" \
    "Robos" \
    "Scripts" \
    "Config" \
    "Docker" \
    "Docs" \
    "Data" \
    "Imagens" \
    "CloneVoz"

# --- MANUTENÇÃO E LOGGING ---

# Rotação de backups (Mantém os últimos 7 dias)
find "$BACKUP_DEST" -type f -name "toolbox_backup_*.tar.gz" -mtime +7 -delete

# Registro no Log Central
echo "$(date '+%Y-%m-%d %H:%M:%S') - [SUCCESS] - Backup gerado: $FILENAME" >> "$LOG_FILE"

echo "✅ SUCESSO: Backup salvo em $BACKUP_DEST/$FILENAME"