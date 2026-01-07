# 🛠️ ToolBox - Ecossistema de Automação Sênior

### 📂 Visão Geral e Arquitetura
Este repositório é um ecossistema de automação modular desenvolvido para ambiente **Linux (Fedora/Debian/Ubuntu)**. O projeto integra agentes inteligentes e utilitários de infraestrutura sob uma arquitetura de níveis (1 a 4), focando em:

* **Inteligência de Dados:** Agentes autônomos para extração e processamento via *Web Scraping* e integração com *APIs REST*.
* **Segurança e Redes:** Ferramentas de auditoria de criptografia (SSL) e diagnóstico de conectividade de baixo nível.
* **Processamento de Mídia:** Pipelines para manipulação de imagem e síntese vocal, explorando automação visual e auditiva.
* **Resiliência de Sistema:** Scripts de manutenção de infraestrutura e gestão de processos em background (*Daemons*) com foco em persistência estruturada em CSV e JSON.

---

### 🤖 /Robos
Unidade de Agentes Autônomos especializados por nível de complexidade.

- **[career_hunter.py](./Robos/career_hunter.py)**: Aguardando commit | *Docstring - ROBÔ: Web Scraper FUNÇÃO: Procura informações vagas de empregos em sites específicos. Ou seja, Coletor de Dados: Busca oportunidades em sites específicos. STATUS: Ativo e funcional - Nível 2*
- **[cotacao_dolar.py](./Robos/cotacao_dolar.py)**: Last Config (2026-01-07) | *NÍVEL 2: Agente Financeiro Autônomo FUNÇÃO: Captura cotações em tempo real via API e gera séries históricas estruturadas. Este bot trata Dados e APIs CONCEITOS: Integração de APIs REST, Persistência CSV, Séries Temporais.*
- **[global_news_sniper.py](./Robos/global_news_sniper.py)**: Aguardando commit | *NÍVEL 2: Agente  FUNÇÃO: Coletor internacional de notícias com suporte a múltiplos idiomas. CONCEITOS:*
- **[news_sniper.py](./Robos/news_sniper.py)**: Last Config (2026-01-07) | *NÍVEL 2: Agente de Extração de Dados FUNÇÃO: Coleta notícias de fontes globais via Web Scraping. CONCEITOS: BeautifulSoup, requests, persistência em JSON.*
- **[sentinela.py](./Robos/sentinela.py)**: Last Config (2026-01-07) | *NÍVEL 1: Agente de Monitoramento de Infraestrutura FUNÇÃO: Vigia a integridade do sistema, gerencia conectividade e rotatividade de logs. Este bot é a base, o vigia do sistema CONCEITOS: I/O de Sistema, Gestão de Logs, Daemonize.*
- **[ssl_hunter.py](./Robos/ssl_hunter.py)**: Last Config (2026-01-07) | *NÍVEL 2: Auditor de Criptografia e Redes FUNÇÃO: Varredura e validação de certificados SSL/TLS em domínios externos. Este bot trata com segurança e rede CONCEITOS: pyOpenSSL, Protocolos de Segurança, Diagnóstico de Rede.*
- **[system_expert.py](./Robos/system_expert.py)**: Aguardando commit | *NÍVEL 2: Agente  FUNÇÃO: Crawler especializado em monitoramento de portais de emprego. CONCEITOS:*
- **[watchdog_sentinela.py](./Robos/watchdog_sentinela.py)**: Last Config (2026-01-07) | *NÍVEL 1: Supervisor de Processos (Watchdog) FUNÇÃO: Garante a persistência e reinicialização automática dos agentes do sistema. Este bot trata com Infraestrutura pura. CONCEITOS: Monitoramento de Processos, Resiliência, Systemd.*
- **[web_monitor.py](./Robos/web_monitor.py)**: Aguardando commit | *NÍVEL 2: Agente  FUNÇÃO: Crawler especializado em monitoramento de portais de emprego. CONCEITOS: Agente de integridade de serviços web e tempo de resposta.*

### 📂 /Scripts
Utilitários de Automação de Infraestrutura e Manutenção de Sistema (Nível 1).

- **[backup_toolbox.sh](./Scripts/backup_toolbox.sh)**: Last Config (2026-01-07) | *NÍVEL 1: Automação de Infraestrutura*

### ⚙️ /Config
Gestor de Parâmetros, Variáveis de Ambiente e Definições Globais (Nível 1).

- *Pasta estruturada.*

### 🐳 /Docker
Orquestrador de Containers e Ambientes Isolados (Nível 1).

- *Pasta estruturada.*

### 📚 /Docs
Repositório de Documentação Técnica e Manuais do Projeto.

- *Pasta estruturada.*

### 📝 /Logs
Registro de Atividades, Históricos e Depuração de Processos.

- *Pasta estruturada.*

### 🖼️ /Imagens
Módulos de Processamento Visual e Manipulação de Imagens (Nível 3).

- **[image_processor.py](./Imagens/image_processor.py)**: Aguardando commit | *NÍVEL 3: Processador de Visão Computacional FUNÇÃO: Análise, redimensionamento e extração de metadados de arquivos de imagem. CONCEITOS: Pillow, Filtros de Imagem, Manipulação de Matrizes.*

### 🎙️ /CloneVoz
Módulos de Processamento de Áudio e Síntese Vocal.

- **[voice_synthesizer.py](./CloneVoz/voice_synthesizer.py)**: Aguardando commit | *NÍVEL 4: Sintetizador de Voz e Áudio FUNÇÃO: Processamento de áudio e clonagem vocal para interfaces homem-máquina. CONCEITOS: Processamento de Sinal Digital, Síntese de Voz.*

---
### 🛠️ Stack Tecnológico
- **Linguagem:** Python 3.x / Bash
- **OS:** Linux (Fedora / Debian / Ubuntu)
- **Libs Principais:**
    - `requests`: Integração com APIs e requisições HTTP.
    - `BeautifulSoup4`: Extração de dados de HTML (Web Scraping).
    - `Pillow (PIL)`: Processamento e manipulação de imagens (Nível 3).
    - `pyOpenSSL`: Auditoria e gestão de certificados SSL.
    - `logging`: Sistema de rastreabilidade e histórico de eventos.
    - `socket`: Verificações de baixo nível de conectividade.
    - `csv/json`: Persistência de dados estruturados.
- **Conceitos:** Web Scraping, Image Processing, Daemon Processes, Logging, API REST, Persistência de Dados.
