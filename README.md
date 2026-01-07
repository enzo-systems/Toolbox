
### 🚀 Tecnologias Utilizadas
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

---
# 🛠️ Toolbox de Automação

### 📂 Estrutura do Projeto
Coleção de scripts e ferramentas de automação desenvolvidas em Python, com foco em ambiente Linux (Fedora).   
Este repositório serve como laboratório pessoal para testes de Web Scraping, Processamento de Imagens, Manipulação de Áudio, Segurança de Redes e Processos em Background (Daemons). 

### 🤖 /Robos
Agentes autônomos e scripts de monitoramento/extração de dados (Nível 2).

- **[cotacao_dolar.py](./Robos/cotacao_dolar.py)**: Last Config (2026-01-07) | *Docstring - ROBÔ: SENTINELA FINANCEIRO FUNÇÃO: Captura cotação do dólar via API e mantém histórico em CSV. Ou seja, Integrador de API: Captura dados financeiros profissionais e gera histórico. STATUS: Operacional - Nível 2.*
- **[guru_linux.py](./Robos/guru_linux.py)**: Last Config (2026-01-07) | *Docstring - ROBÔ: GURU FUNÇÃO: Analisa logs e fornece diagnósticos preditivos sobre o status do sistema. Ou seja, Diagnóstico: Analisador de logs do sistema (Alpha). STATUS: Em desenvolvimento / Alpha - Nível 1*
- **[news_sniper.py](./Robos/news_sniper.py)**: Last Config (2026-01-07) | *Docstring - ROBÔ: Web Scraping FUNÇÃO: Procura informações específicas em sites específicos. Ou seja, Coletor de Dados: Raspagem de notícias. STATUS: Ativo e funcional - Nível 2*
- **[news_sniper_world.py](./Robos/news_sniper_world.py)**: Last Config (2026-01-07) | *Docstring - ROBÔ: Web Scraping FUNÇÃO: Procura informações específicas em toda internet. Ou seja, Coletor de Dados: Raspagem de notícias. STATUS: Ativo e funcional - Nível 2*
- **[robo_vagas.py](./Robos/robo_vagas.py)**: Last Config (2026-01-07) | *Docstring - ROBÔ: Web Scraper FUNÇÃO: Procura informações vagas de empregos em sites específicos. Ou seja, Coletor de Dados: Busca oportunidades em sites específicos. STATUS: Ativo e funcional - Nível 2*
- **[sentinela.py](./Robos/sentinela.py)**: Last Config (2026-01-07) | *Docstring - ROBÔ: SENTINELA FUNÇÃO: Monitora a conexão de rede a cada 60 segundos e evita que o log cresça demais. Ou seja, Zelador de Infra: Monitora rede e rotaciona logs para não encher o disco. STATUS: Operacional com rotação de logs - Nivel 1.*
- **[sentinela_web.py](./Robos/sentinela_web.py)**: Last Config (2026-01-07) | *DDocstring - ROBÔ: SENTINELA FUNÇÃO: Navega na Internet como um Agent. Ou seja, Agente Navegador: Navega na web como um agente autônomo. STATUS: Operacional com rotação de logs - Nível 2.*
- **[ssl_hunter.py](./Robos/ssl_hunter.py)**: Last Config (2026-01-07) | *Docstring - ROBÔ: SSL HUNTER FUNÇÃO: Faz auditoria de segurança em sites específicos. Ou seja, Auditor de Segurança: Checa certificados SSL de sites externos. STATUS: Ativo e funcional - Nível 2*
- **[teste_robo.py](./Robos/teste_robo.py)**: Last Config (2026-01-07) | *Docstring - ROBÔ: Web Scraper FUNÇÃO: acessa todas as informações de sites específicos. STATUS: Ativo e funcional - Nível 2*
- **[watchdog_sentinela.py](./Robos/watchdog_sentinela.py)**: Last Config (2026-01-07) | *Docstring - ROBÔ: SENTINELA FUNÇÃO: Vigia o status do serviço Sentinela via systemctl e avisa o Arquiteto se cair. Ou seja, Vigias dos Vigias: Garante que o Sentinela esteja rodando via systemctl STATUS: Operador Invisível - Nível 1.*

### 🖼️ /Imagens
Módulos de Processamento Visual e Manipulação de Imagens (Nível 3).

- **[corta_foto.py](./Imagens/corta_foto.py)**: Last commit (2026-01-05) | *ROBÔ: MULTIMÍDIA FUNÇÃO: Processamento automatizado Redimensionamento de Foto). STATUS: Testando integração com APIs externas.*

### 🎙️ /CloneVoz
Módulos de Processamento de Áudio e Síntese Vocal.

- **[robo_enzo.py](./CloneVoz/robo_enzo.py)**: Last commit (2026-01-05) | *ROBÔ: MULTIMÍDIA FUNÇÃO: Transforma um roteiro escrito em áudio baseado na voz sintética do roteirista. STATUS: Testando integração com APIs externas.*

### 📂 /Scripts
Utilitários de Automação de Infraestrutura e Manutenção de Sistema (Nível 1).

- **[backup_toolbox.sh](./Scripts/backup_toolbox.sh)**: Last Config (2026-01-07) | *FUNÇÃO: Automação de Infraestrutura - Backup incremental do repositório ToolBox.*

### ⚙️ /Config
Gestor de Parâmetros, Variáveis de Ambiente e Definições Globais (Nível 1).

- *Pasta organizada (aguardando módulos).*

### 🐳 /Docker
Orquestrador de Containers e Ambientes Isolados (Nível 1).

- *Pasta organizada (aguardando módulos).*

### 📚 /Docs
Repositório de Documentação Técnica e Manuais do Projeto.

- *Pasta organizada (aguardando módulos).*

### 📝 /Logs
Registro de Atividades, Históricos e Depuração de Processos.

- *Pasta organizada (aguardando módulos).*

### 🚀 /Tecnologias
- **Linguagem:** Python 3.x
- **OS:** Linux (Fedora/Debian)
- **Libs:** `requests`, `BeautifulSoup`, `Pillow` (PIL), `OpenSSL`, `logging`, `socket`
- **Conceitos:** Web Scraping, Image Processing, Daemon Processes, Logging.

---
*Mantido por [Enzo Systems](https://github.com/enzo-systems)*
