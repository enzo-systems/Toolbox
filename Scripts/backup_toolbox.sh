#!/bin/bash

# ==============================================================================
#ARQUITETURA AUTÔNOMA - NÍVEL 1 
#Script: backup_toolbox.sh
#Objetivo: Automação de infraestrutura e backup de segurança
# ==============================================================================
# 1. TRAVAS DE SEGURANÇA 
# set -e: Aborta em erro.
# set -u: Aborta se variável não definida.
# set -o pipefail: Aborta se falha no pipe.
set -euo pipefail

# 2. LOCALIZAÇÃO DINÂMICA DE DIRETÓRIOS FÍSICOS
# A lógica 'cd ... && pwd' resolve links simbólicos e garante o caminho real.

# SCRIPTPATH: Onde este script reside (ex: .../Projetos/ToolBox/Scripts)
SCRIPTPATH="$(cd "$(dirname "$0")" && pwd)"

# BASE_DIR: A raiz da ToolBox (Sobe 1 nível a partir de Scripts)
BASE_DIR="$(cd "$SCRIPTPATH/.." && pwd)"

# BACKUP_DEST: Pasta oculta criada FORA da raiz do projeto para segurança
# Sobe 1 nível a partir da ToolBox (ex: .../Projetos/.ToolBox_Backups)
BACKUP_DEST="$(cd "$BASE_DIR/.." && pwd)/.ToolBox_Backups"

# 3. RASTREABILIDADE DE ERROS
# Trap para indicar a linha exata do erro no terminal caso algo falhe
trap 'echo "❌ ERRO CRÍTICO na linha $LINENO em: $SCRIPTPATH"' ERR

# ==============================================================================
# 4. EXECUÇÃO DA INFRAESTRUTURA
# ==============================================================================

echo "🚀 [Nível 1] Iniciando protocolo de backup..."
echo "📂 Raiz do Projeto (Físico): $BASE_DIR"
echo "🔒 Destino Seguro (Oculto):  $BACKUP_DEST"

# Garante que a pasta oculta de destino exista
if [ ! -d "$BACKUP_DEST" ]; then
    echo "⚠️ Criando diretório de armazenamento..."
    mkdir -p "$BACKUP_DEST"
fi

# Definição de nomes
TIMESTAMP=$(date +"%Y-%m-%d_%H%M%S")
FILENAME="toolbox_backup_$TIMESTAMP.tar.gz"

echo "📦 Compactando módulos da Arquitetura..."

# Compactação seletiva baseada na estrutura de pastas
# Excluímos 'Logs/' pois contém dados temporários ignorados pelo Git
tar -czf "$BACKUP_DEST/$FILENAME" \
    -C "$BASE_DIR" \
    "Robos" \
    "Scripts" \
    "Config" \
    "Docker" \
    "Docs"

# ==============================================================================
# 5. MANUTENÇÃO AUTOMÁTICA
# ==============================================================================

# Rotação de backups (Conceito de manutenção)
# Mantém o diretório limpo removendo arquivos com mais de 7 dias
find "$BACKUP_DEST" -type f -name "toolbox_backup_*.tar.gz" -mtime +7 -delete

echo "✅ SUCESSO: Backup salvo em $BACKUP_DEST/$FILENAME"