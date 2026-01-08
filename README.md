# 🛠️ ToolBox - Ecossistema de Agentes Autônomos

### 📂 Visão Geral e Arquitetura
Este repositório opera através de **Agentes Especializados** e uma infraestrutura de dados organizada por tipos e domínios.

* **Agentes de Dados:** Inteligência de busca, scraping e coleta de dados.
* **Agentes de Monitor:** Integridade de redes, latência e diagnóstico de sistemas.
* **Agentes de Visao:** Processamento de imagem, higienização e privacidade.
* **Agentes de Voz:** Síntese vocal e inteligência auditiva.
* **Infraestrutura:** Gestão de logs, configurações e persistência de dados.

---

### 🛰️ /Agentes_Dados
> Coleta e processamento de notícias e oportunidades (Scraping/RSS).

- **[career_hunter.py](./Agentes_Dados/career_hunter.py)**: (2026-01-08) | *NÍVEL 2: Career Hunter STATUS: Corrigido com Debug de Caminhos Absolutos.*
- **[cotacao_dolar.py](./Agentes_Dados/cotacao_dolar.py)**: (2026-01-08) | *NÍVEL 2: Agente Financeiro Autônomo FUNÇÃO: Captura cotações em tempo real via API e gera séries históricas. CONCEITOS: Integração de APIs REST, Configuração Centralizada, Persistência CSV.*
- **[global_news_sniper.py](./Agentes_Dados/global_news_sniper.py)**: (2026-01-08) | *NÍVEL 2: Agente de Inteligência de Dados (Global Sniper) FUNÇÃO: Coleta e processa notícias internacionais via RSS (Feedparser). CONCEITOS: RSS Parsing, Normalização de Dados, Persistência JSON.*
- **[news_sniper.py](./Agentes_Dados/news_sniper.py)**: (2026-01-08) | *NÍVEL 2: Agente de Extração de Dados (News Sniper) STATUS: Corrigido com Debug de Caminhos Absolutos.*

### 🖥️ /Agentes_Monitor
> Monitoramento de integridade web e diagnóstico de hardware/OS.

- **[sentinela.py](./Agentes_Monitor/sentinela.py)**: (2026-01-08) | *NÍVEL 2: Sentinela de Infraestrutura FUNÇÃO: Vigia a conectividade e gerencia a rotatividade de logs do sistema. CONCEITOS: I/O de Sistema, RotatingFileHandler, Daemonize Simulation.*
- **[ssl_hunter.py](./Agentes_Monitor/ssl_hunter.py)**: (2026-01-08) | *NÍVEL 2: Auditor de Criptografia e Redes FUNÇÃO: Varredura e validação de certificados SSL/TLS em domínios externos. CONCEITOS: pyOpenSSL, Protocolos de Segurança, Persistência de Auditoria.*
- **[system_expert.py](./Agentes_Monitor/system_expert.py)**: (2026-01-08) | *NÍVEL 1: Agente de Diagnóstico de Infraestrutura FUNÇÃO: Analisa comandos Linux e gera documentação formatada para comunidades. CONCEITOS: Shell Integration, Log Parsing, Integração com API TLDR.*
- **[watchdog_sentinela.py](./Agentes_Monitor/watchdog_sentinela.py)**: (2026-01-08) | *NÍVEL 2: Watchdog (Supervisor de Resiliência) FUNÇÃO: Valida o heartbeat do Sentinela e dispara alertas visuais no Fedora. CONCEITOS: Auditoria de Heartbeat, Notificação de Sistema (GNOME), Resiliência.*
- **[web_monitor.py](./Agentes_Monitor/web_monitor.py)**: (2026-01-08) | *NÍVEL 2: Agente de Integridade de Redes FUNÇÃO: Monitora disponibilidade e latência de serviços web críticos. CONCEITOS: Socket Programming, HTTP Status Monitoring, Tempo de Resposta.*

### 👁️ /Agentes_Visao
> Processamento de imagens, filtros e remoção de metadados.

- **[vision_processor.py](./Agentes_Visao/vision_processor.py)**: (2026-01-08) | *NÍVEL 3: Processador de Visão Computacional (Vision Processor) FUNÇÃO: Higienização e formatação de fotos de perfil (LinkedIn Style) em lote. CONCEITOS: Pillow, Pipeline de I/O, Processamento em Batch.*

### 🎙️ /Agentes_Voz
> Conversão de texto em fala (TTS) e inteligência auditiva.

- **[voice_synthesizer.py](./Agentes_Voz/voice_synthesizer.py)**: (2026-01-08) | *NÍVEL 4: Sintetizador de Inteligência Auditiva (Voice Cloner) FUNÇÃO: Processamento de áudio e síntese vocal (TTS) com auto-conversão de formatos. CONCEITOS: DSP, Wrappers de FFmpeg, Pipeline de Áudio Automatizado.*

### 📜 /Scripts
> Utilitários de manutenção, backup e automação de infraestrutura.

- **[backup_toolbox.sh](./Scripts/backup_toolbox.sh)**: (2026-01-07) | *NÍVEL 1: Automação de Infraestrutura*

### ⚙️ /Config
> Cérebro do projeto (Settings, caminhos absolutos e variáveis).

- **[settings.py](./Config/settings.py)**: (2026-01-08) | *NÍVEL 1: Gestor de Ambiente e Caminhos (Versão Agentes V2) FUNÇÃO: Centraliza a inteligência de diretórios e separação por tipo de dado. CONCEITOS: Abstração de Caminhos, Configuração Centralizada, Higiene de Dados.*

### 📊 /Data
> Repositório central organizado por subpastas (csv, json, images, audio).

- **[csv/cotacao_dolar.csv](./Data/csv/cotacao_dolar.csv)**: (2026-01-08)
- **[input_images/minha_foto.jpg](./Data/input_images/minha_foto.jpg)**: Novo
- **[json/auditoria_ssl.json](./Data/json/auditoria_ssl.json)**: (2026-01-08)
- **[json/global_news_memory.json](./Data/json/global_news_memory.json)**: (2026-01-08)
- **[json/memoria_world.json](./Data/json/memoria_world.json)**: (2026-01-08)
- **[json/news_sniper_memory.json](./Data/json/news_sniper_memory.json)**: (2026-01-08)
- **[json/sentinela_status.json](./Data/json/sentinela_status.json)**: (2026-01-08)
- **[json/vagas_encontradas.json](./Data/json/vagas_encontradas.json)**: (2026-01-08)
- **[json/web_monitor_results.json](./Data/json/web_monitor_results.json)**: (2026-01-08)
- **[output_images/perfil_minha_foto.png](./Data/output_images/perfil_minha_foto.png)**: Novo

### 📝 /Logs
> Registro de atividades, histórico de erros e auditoria.

- *Aguardando geração de dados ou scripts.*

### 📦 /Assets
> Recursos estáticos, modelos e arquivos fixos do sistema.

- *Aguardando geração de dados ou scripts.*

---
### 🛠️ Stack Tecnológico e Engenharia
- **Core Executivo:** Python 3.x & Bash Scripting (Automação de Infraestrutura).
- **Domínios de Inteligência:**
    - `Requests` & `BeautifulSoup4`: Engenharia de extração e consumo de APIs REST.
    - `Pillow (PIL)`: Pipeline de processamento de imagem e manipulação de metadados.
    - `gTTS`: Síntese de voz e processamento de fluxos de áudio.
- **Resiliência e Monitoramento:**
    - `Socket`: Diagnósticos de conectividade em baixo nível (TCP/UDP).
    - `Logging (RotatingFileHandler)`: Gestão de logs cíclicos com controle de volumetria.
    - `Subprocess`: Orquestração de comandos do sistema operacional (Fedora/Linux).
- **Arquitetura de Dados:**
    - **Persistência Estruturada:** Armazenamento em CSV (Séries temporais) e JSON (Status/Auditoria).
    - **Estratégia de I/O:** Separação rigorosa entre `input_` (Matéria-prima) e `output_` (Processados).
    - **Portabilidade:** Gestão de caminhos absolutos via `Pathlib` para integridade entre ambientes.
