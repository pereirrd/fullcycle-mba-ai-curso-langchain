# Projeto: FullCycle MBA - Curso LangChain

Este projeto tem como objetivo ensinar os principais conceitos do framework [LangChain](https://python.langchain.com/) para desenvolvimento de aplicações com modelos de IA, utilizando Python.

## Estrutura de Pastas

- **fundamentos/**  
  Exemplos básicos de uso do LangChain:
  - [`hello-world.py`](fundamentos/hello-world.py): Primeira interação com um modelo de chat.
  - [`init-chat-model.py`](fundamentos/init-chat-model.py): Inicialização de modelo Gemini via Google GenAI.
  - [`prompt-templates.py`](fundamentos/prompt-templates.py): Uso de templates para prompts.
  - [`chat-template.py`](fundamentos/chat-template.py): Criação de prompts para chat com múltiplos papéis.

- **chains-e-processamento/**  
  Exemplos avançados de processamento e chains:
  - [`iniciando-com-chains.py`](chains-e-processamento/iniciando-com-chains.py): Encadeamento simples de prompt e modelo.
  - [`chain-com-decorators.py`](chains-e-processamento/chain-com-decorators.py): Uso de decorators para criar chains customizadas.
  - [`pipeline-de-processamento.py`](chains-e-processamento/pipeline-de-processamento.py): Pipeline de tradução e sumarização.
  - [`runnable-lambda.py`](chains-e-processamento/runnable-lambda.py): Uso de funções lambda como etapas de processamento.

## Aprendizados

- Como criar e formatar prompts usando LangChain.
- Como inicializar e utilizar diferentes modelos de IA (OpenAI, Google GenAI).
- Como encadear etapas de processamento (chains e pipelines).
- Como utilizar parsers e funções customizadas no fluxo de dados.

## Configuração do Ambiente

1. **Clone o repositório**
   ```sh
   git clone <url-do-repo>
   cd fullcycle-mba-ai-curso-langchain-aluno
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

4. **Configure variáveis de ambiente**
   - Crie um arquivo `.env` com suas chaves de API (OpenAI, Google GenAI, etc).
   ```sh
   OPENAI_API_KEY = xxxxx
   GOOGLE_API_KEY = xxxxx
   ```

5. **Execute os exemplos**
   ```sh
   python fundamentos/hello-world.py
   python chains-e-processamento/pipeline-de-processamento.py
   # ...e assim por diante
   ```

## Requisitos

- Python 3.10+
- Chaves de API para os provedores de modelos (OpenAI, Google GenAI)

---

Sinta-se à vontade para explorar os arquivos e adaptar os exemplos