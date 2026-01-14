#!/bin/bash

# ============================================================
# NOME: Audit Project (Raio-X do Projeto)
# FUNÇÃO: Lista a estrutura de pastas e o conteúdo de todos os .py
# USO: ./audit_project.sh > relatorio_completo.txt
# ============================================================

# Cores para facilitar a leitura no terminal
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}##################################################${NC}"
echo -e "${GREEN}###        RELATÓRIO DE ESTRUTURA E CÓDIGO     ###${NC}"
echo -e "${GREEN}##################################################${NC}"
echo ""

# 1. Imprime a árvore (Visualização Espacial)
echo -e "${YELLOW}>>> ESTRUTURA DE DIRETÓRIOS:${NC}"
if command -v tree &> /dev/null; then
    # -a: All files
    # -I: Ignore pattern
    # --dirsfirst: Pastas primeiro (mais organizado)
    tree -a -I '.git*|.venv*|__pycache__*|.pytest_cache*' --dirsfirst
else
    echo "❌ Erro: O comando 'tree' não está instalado."
fi

echo ""
echo -e "${GREEN}##################################################${NC}"
echo -e "${GREEN}###             CONTEÚDO DOS ARQUIVOS          ###${NC}"
echo -e "${GREEN}##################################################${NC}"

# 2. Busca inteligente (Find com Pruning)
# Explicação Técnica: Usamos '-prune' para que o 'find' NEM ENTRE 
# nas pastas .venv ou .git. Isso economiza I/O e tempo.
find . -type d \( -name ".git" -o -name ".venv" -o -name "__pycache__" -o -name ".idea" -o -name ".vscode" \) -prune -o -type f -name "*.py" -print | sort | while read -r file; do
    echo ""
    echo -e "${CYAN}==================================================${NC}"
    echo -e "${CYAN}📁 ARQUIVO: $file${NC}"
    echo -e "${CYAN}==================================================${NC}"
    
    # Exibe o conteúdo
    cat "$file"
    
    echo ""
    echo -e "${YELLOW}⬇️  FIM DE $(basename "$file")${NC}"
done

echo ""
echo -e "${GREEN}✅ Auditoria Finalizada.${NC}"
