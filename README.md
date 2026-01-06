# 🛠️ Toolbox de Automação

### 📂 Estrutura do Projeto
Coleção de scripts e ferramentas de automação desenvolvidas em Python, com foco em ambiente Linux (Fedora).   
Este repositório serve como laboratório pessoal para testes de Web Scraping, Processamento de Imagens, Manipulação de Áudio, Segurança de Redes e Processos em Background (Daemons). 

### 🤖 /Robos 
Scripts utilitários e agentes autônomos.
- **[guru_linux.py](./Robos/guru_linux.py)**: Last commit (2026-01-05) | *ROBÔ: GURU FUNÇÃO: Analisa logs e fornece diagnósticos preditivos sobre o status do sistema. STATUS: Em desenvolvimento / Alpha.*
- **[memoria_world.json](./Robos/memoria_world.json)**: Last commit message (2026-01-05)
- **[news_sniper.py](./Robos/news_sniper.py)**: Last commit (2026-01-05) | *ROBÔ: SNIPER FUNÇÃO: Procura informações específicas em sites específicos. STATUS: Ativo e funcional.*
- **[news_sniper_world.py](./Robos/news_sniper_world.py)**: Last commit (2026-01-05) | *ROBÔ: SNIPER FUNÇÃO: Procura informações específicas em toda internet. STATUS: Ativo e funcional.*
- **[robo_vagas.py](./Robos/robo_vagas.py)**: Last commit (2026-01-05) | *ROBÔ: SNIPER FUNÇÃO: Procura informações vagas de empregos em sites específicos. STATUS: Ativo e funcional.*
- **[sentinela.py](./Robos/sentinela.py)**: Last commit (2026-01-05) | *ROBÔ: SENTINELA FUNÇÃO: Monitora a conexão de rede a cada 60 segundos e evita que o log cresça demais. STATUS: Operacional com rotação de logs.*
- **[sentinela_web.py](./Robos/sentinela_web.py)**: Message Commit (2026-01-06) | *ROBÔ: SENTINELA FUNÇÃO: Navega na Internet como um agent. STATUS: Operacional com rotação de logs.*
- **[ssl_hunter.py](./Robos/ssl_hunter.py)**: Last commit (2026-01-05) | *ROBÔ: SSL HUNTER FUNÇÃO: faz auditoria de segurança em sites específicos. STATUS: Ativo e funcional.*
- **[teste_robo.py](./Robos/teste_robo.py)**: Last commit (2026-01-05) | *ROBÔ: SSL HUNTER FUNÇÃO: acessa todas as informações de sites específicos. STATUS: Ativo e funcional.*
- **[watchdog_sentinela.py](./Robos/watchdog_sentinela.py)**: Last commit (2026-01-05) | *ROBÔ: WATCHDOG SENTINELA FUNÇÃO: Vigia o status do serviço Sentinela via systemctl e avisa o Arquiteto se cair. STATUS: Nível 1 - Operador Invisível.*

### 🖼️ /Imagens
Ferramentas de manipulação de imagem e processamento visual.
- **[corta_foto.py](./Imagens/corta_foto.py)**: Last commit (2026-01-05) | *ROBÔ: MULTIMÍDIA FUNÇÃO: Processamento automatizado Redimensionamento de Foto). STATUS: Testando integração com APIs externas.*

### 🎙️ /CloneVoz
Ferramentas de manipulação clonagem de voz.
- **[robo_enzo.py](./CloneVoz/robo_enzo.py)**: Last commit (2026-01-05) | *ROBÔ: MULTIMÍDIA FUNÇÃO: Transforma um roteiro escrito em áudio baseado na voz sintética do roteirista. STATUS: Testando integração com APIs externas.*

### 📂 /Scripts
- **[backup_toolbox.sh](./Scripts/backup_toolbox.sh)**: message commit (2026-01-06) | *==============================================================================*

### ⚙️ /Config
- *Pasta estruturada (aguardando arquivos de sistema).*

### 🐳 /Docker
- *Pasta estruturada (aguardando arquivos de sistema).*

### 📚 /Docs
- *Pasta estruturada (aguardando arquivos de sistema).*

### 📝 /Logs
- *Pasta estruturada (aguardando arquivos de sistema).*

### 🚀 /Tecnologias
- **Linguagem:** Python 3.x
- **OS:** Linux (Fedora/Debian)
- **Libs:** `requests`, `BeautifulSoup`, `Pillow` (PIL), `OpenSSL`, `logging`, `socket`
- **Conceitos:** Web Scraping, Image Processing, Daemon Processes, Logging.

---
*Mantido por [Enzo Systems](https://github.com/enzo-systems)*
