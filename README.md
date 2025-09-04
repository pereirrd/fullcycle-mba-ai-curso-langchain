# Projeto: FullCycle MBA - Curso LangChain

Este projeto faz parte do estudo sobre **LangChain** do curso de **Inteligência Artificial** na **FullCycle MBA**. O objetivo é ensinar os principais conceitos do framework [LangChain](https://python.langchain.com/) para desenvolvimento de aplicações com modelos de IA, utilizando Python.

## Estrutura de Pastas

- **1-fundamentos/**  
  Exemplos básicos de uso do LangChain:
  - [`1-hello-world.py`](1-fundamentos/1-hello-world.py): Primeira interação com um modelo de chat.
  - [`2-init-chat-model.py`](1-fundamentos/2-init-chat-model.py): Inicialização de modelo Gemini via Google GenAI.
  - [`3-prompt-templates.py`](1-fundamentos/3-prompt-templates.py): Uso de templates para prompts.
  - [`4-chat-template.py`](1-fundamentos/4-chat-template.py): Criação de prompts para chat com múltiplos papéis.

- **2-chains-e-processamento/**  
  Exemplos avançados de processamento e chains:
  - [`1-iniciando-com-chains.py`](2-chains-e-processamento/1-iniciando-com-chains.py): Encadeamento simples de prompt e modelo.
  - [`2-chain-com-decorators.py`](2-chains-e-processamento/2-chain-com-decorators.py): Uso de decorators para criar chains customizadas.
  - [`3-runnable-lambda.py`](2-chains-e-processamento/3-runnable-lambda.py): Uso de funções lambda como etapas de processamento.
  - [`4-pipeline-de-processamento.py`](2-chains-e-processamento/4-pipeline-de-processamento.py): Pipeline de tradução e sumarização.
  - [`5-sumarizacao.py`](2-chains-e-processamento/5-sumarizacao.py): Exemplos de sumarização de texto.
  - [`6-sumarizacao-com-map-reduce.py`](2-chains-e-processamento/6-sumarizacao-com-map-reduce.py): Sumarização usando técnica Map-Reduce.
  - [`7-pipeline-de-sumarizacao.py`](2-chains-e-processamento/7-pipeline-de-sumarizacao.py): Pipeline completo de sumarização.

- **3-agente-e-tools/**  
  Exemplos de agentes e ferramentas:
  - [`1-agente-react-e-tools.py`](3-agente-e-tools/1-agente-react-e-tools.py): Implementação de agente ReAct com ferramentas.
  - [`2-agente-react-usando-prompt-hub.py`](3-agente-e-tools/2-agente-react-usando-prompt-hub.py): Agente ReAct usando Prompt Hub.

- **4-gerenciamento-de-historico/**  
  Exemplos de gerenciamento de histórico de conversas:
  - [`1-armazenamento-de-historico.py`](4-gerenciamento-de-historico/1-armazenamento-de-historico.py): Armazenamento básico de histórico.
  - [`2-historico-baseado-em-sliding-window.py`](4-gerenciamento-de-historico/2-historico-baseado-em-sliding-window.py): Histórico com janela deslizante.

- **5-loaders-e-banco-de-dados-vetoriais/**  
  Exemplos de carregamento de documentos e bancos vetoriais:
  - [`3-ingestion-pgvector.py`](5-loaders-e-banco-de-dados-vetoriais/3-ingestion-pgvector.py): Ingestão de documentos no PostgreSQL com pgvector.
  - [`4-search-vector.py`](5-loaders-e-banco-de-dados-vetoriais/4-search-vector.py): Busca vetorial no banco de dados.

## Aprendizados

- Como criar e formatar prompts usando LangChain.
- Como inicializar e utilizar diferentes modelos de IA (OpenAI, Google GenAI).
- Como encadear etapas de processamento (chains e pipelines).
- Como utilizar parsers e funções customizadas no fluxo de dados.

## Configuração do Ambiente

1. **Clone o repositório**
   ```sh
   git clone https://github.com/pereirrd/fullcycle-mba-ai-curso-langchain
   cd fullcycle-mba-ai-curso-langchain
   ```

2. **Crie e ative um ambiente virtual**
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure o banco de dados PostgreSQL (opcional)**
   Para os exemplos de banco de dados vetoriais, você pode usar o Docker Compose:
   ```sh
   docker-compose up -d
   ```

5. **Configure variáveis de ambiente**
   
   **⚠️ IMPORTANTE:** Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis. Este arquivo **NÃO é versionado** por questões de segurança, então você deve criá-lo manualmente.

   ```sh
   # Chaves de API para modelos de IA
   OPENAI_API_KEY=sk-your-openai-api-key-here
   GOOGLE_API_KEY=your-google-genai-api-key-here
   
   # Configurações do modelo OpenAI (opcional)
   OPENAI_MODEL=text-embedding-3-small
   
   # Configurações do PostgreSQL com pgvector (para exemplos de banco vetorial)
   PGVECTOR_URL=postgresql://postgres:postgres@localhost:5432/rag
   PGVECTOR_COLLECTION=documents
   ```

   **Como obter as chaves de API:**
   - **OpenAI API Key**: Acesse [OpenAI Platform](https://platform.openai.com/api-keys) e crie uma nova chave
   - **Google GenAI API Key**: Acesse [Google AI Studio](https://makersuite.google.com/app/apikey) e gere uma chave

6. **Execute os exemplos**
   ```sh
   # Exemplos básicos
   python 1-fundamentos/1-hello-world.py
   python 1-fundamentos/2-init-chat-model.py
   
   # Exemplos de chains e processamento
   python 2-chains-e-processamento/1-iniciando-com-chains.py
   python 2-chains-e-processamento/4-pipeline-de-processamento.py
   
   # Exemplos de agentes
   python 3-agente-e-tools/1-agente-react-e-tools.py
   
   # Exemplos de banco vetorial (requer PostgreSQL rodando)
   python 5-loaders-e-banco-de-dados-vetoriais/3-ingestion-pgvector.py
   ```

## Requisitos

### Software Necessário
- **Python 3.10+**
- **Docker e Docker Compose** (para exemplos de banco vetorial)
- **Git** (para clonar o repositório)

### Chaves de API
- **OpenAI API Key** - Para usar modelos GPT e embeddings
- **Google GenAI API Key** - Para usar modelos Gemini

### Dependências Python
As dependências estão listadas no arquivo `requirements.txt` e incluem:
- `langchain` - Framework principal
- `langchain-openai` - Integração com OpenAI
- `langchain-community` - Componentes da comunidade
- `python-dotenv` - Carregamento de variáveis de ambiente
- `psycopg` - Driver PostgreSQL para Python

## Sobre o Curso FullCycle MBA

Este projeto é parte integrante do **curso de Inteligência Artificial** da **FullCycle MBA**, focado no aprendizado prático do framework **LangChain**. O curso aborda desde conceitos fundamentais até implementações avançadas de sistemas de IA, incluindo:

- **Fundamentos do LangChain**: Prompts, modelos e templates
- **Chains e Processamento**: Encadeamento de operações e pipelines
- **Agentes e Ferramentas**: Criação de agentes inteligentes com capacidades de raciocínio
- **Gerenciamento de Histórico**: Persistência e controle de conversas
- **Bancos de Dados Vetoriais**: Implementação de sistemas RAG (Retrieval-Augmented Generation)

## Estrutura de Aprendizado

O projeto está organizado em módulos progressivos, permitindo que os alunos evoluam gradualmente:

1. **Fundamentos** → Conceitos básicos e primeiros passos
2. **Chains e Processamento** → Operações complexas e pipelines
3. **Agentes e Tools** → Sistemas inteligentes autônomos
4. **Gerenciamento de Histórico** → Persistência de dados
5. **Loaders e Bancos Vetoriais** → Sistemas RAG completos

---

**Desenvolvido para o curso FullCycle MBA - Inteligência Artificial**  
Sinta-se à vontade para explorar os arquivos e adaptar os exemplos conforme sua necessidade de aprendizado.