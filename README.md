# AI Build Assistant (LoL)

Projeto de Engenharia de Dados, Backend e IA Generativa que implementa um
assistente especializado em League of Legends.

A aplicação interpreta perguntas em linguagem natural, consulta dados
estruturados no Oracle e combina essas informações com conhecimento armazenado
em documentos Markdown.

## Objetivo

Explorar, de forma prática, conceitos de:

- Engenharia de Dados
- Desenvolvimento Backend
- Integração com LLMs
- Prompt Engineering
- RAG
- Bancos de dados em nuvem
- Arquitetura de aplicações de IA

## Fluxo da Aplicação

```text
Pergunta do usuário
        |
        v
FastAPI
        |
        v
LLM interpreta intenção e entidades
        |
        v
Orchestrator seleciona o serviço
        |
        v
Oracle Cloud + contexto Markdown
        |
        v
Geração da resposta
        |
        v
Resposta JSON
```

Exemplo de pergunta:

```text
Qual a build da Ahri mid?
```

Interpretação produzida pelo LLM:

```json
{
  "intent": "build",
  "champion": "Ahri",
  "role": "mid",
  "limit": 1
}
```

## Funcionalidades Atuais

A aplicação possui suporte para:

- Consulta de builds e winrate
- Consulta de counters
- Consulta de runas
- Visão geral de um campeão
- Interpretação de perguntas com LLM
- Limites padrão e máximos por intenção
- Registro local de eventos
- Estatísticas de utilização

As intenções `skills`, `synergies`, `matchup` e `power_spike` estão previstas,
mas ainda não possuem implementação completa.

## ETL

O pipeline carrega dados de builds para o banco Oracle:

```text
CSV
 |
 v
Extract
 |
 v
Transform
 |
 v
Load
 |
 v
Oracle Autonomous Database
```

Execução:

```bash
python -m pipelines.run_pipeline
```

## Banco de Dados

O banco principal é o Oracle Autonomous Database, hospedado na Oracle Cloud.

A conexão padrão utiliza TLS/TCPS sem Oracle Wallet e está centralizada em:

```text
src/database/db.py
```

Tabelas utilizadas:

- `lol_builds`
- `lol_counters`
- `lol_runes`

## LLM

A OpenAI API é utilizada em dois momentos:

1. Interpretação da pergunta em filtros estruturados.
2. Geração da resposta natural para a visão geral de campeões.

O modelo recebe instruções para retornar uma intenção válida, campeão, rota e
limite de resultados.

## RAG

A primeira versão do mecanismo de recuperação utiliza arquivos Markdown em:

```text
knowledge/
|-- champions/
`-- guides/
```

Atualmente, o sistema:

- Localiza documentos por nome
- Separa o conteúdo por seções
- Recupera informações do campeão e de guias
- Utiliza esse contexto na intenção `overview`

Esta versão ainda não utiliza embeddings, banco vetorial ou busca semântica.
Esses recursos fazem parte da evolução planejada.

## API

A API foi construída com FastAPI.

| Método | Endpoint | Descrição |
|---|---|---|
| `GET` | `/` | Verifica o status da API |
| `GET` | `/builds` | Consulta builds diretamente |
| `GET` | `/ask` | Recebe perguntas em linguagem natural |
| `GET` | `/stats` | Retorna estatísticas de utilização |

Exemplos:

```text
GET /builds?champion=Ahri&role=mid&limit=1
```

```text
GET /ask?question=me fala sobre a Ahri
```

Documentação Swagger:

```text
http://127.0.0.1:8000/docs
```

## Stack

- Python
- FastAPI
- Pandas
- OpenAI API
- Oracle Autonomous Database
- python-oracledb
- TLS/TCPS
- Docker
- Docker Compose
- python-dotenv
- Git e GitHub

## Estrutura Principal

```text
data_pipeline/
|-- data/
|-- docs/
|-- infra/
|-- knowledge/
|   |-- champions/
|   `-- guides/
|-- pipelines/
|-- scripts/
|   `-- database/
|-- src/
|   |-- ai/
|   |-- config/
|   |-- core/
|   |-- database/
|   |-- embeddings/
|   |-- etl/
|   |-- observability/
|   |-- rag/
|   `-- services/
|-- tests/
|-- main.py
|-- Dockerfile
|-- docker-compose.yml
`-- requirements.txt
```

O diretório `src/embeddings/` está reservado para a futura implementação de
busca semântica.

## Configuração Local

### 1. Criar e ativar o ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 3. Configurar as variáveis de ambiente

Crie um arquivo `.env` na raiz:

```env
OPENAI_API_KEY=

DB_USER=
DB_PASSWORD=
DB_DSN=(description=(address=(protocol=tcps)(port=1522)(host=HOST_DO_BANCO))(connect_data=(service_name=SERVICE_NAME))(security=(ssl_server_dn_match=yes)))
```

O arquivo `.env` não deve ser enviado ao repositório.

### 4. Executar a API

```bash
uvicorn main:app --reload
```

## Observabilidade

Cada chamada processada pelo endpoint `/ask` gera um evento local no formato
JSON Lines.

O endpoint `/stats` retorna:

```json
{
  "total_requests": 0,
  "success_requests": 0,
  "error_requests": 0,
  "top_intents": [],
  "top_champions": []
}
```

## Docker

O projeto possui `Dockerfile` e configuração do Docker Compose para a API.

O `docker-compose.yml` carrega as variáveis da `.env`. A conexão com o Oracle
Autonomous Database usa o DSN TLS/TCPS e não exige volume de Wallet.

## Próximos Passos

- Implementar busca semântica com embeddings
- Adicionar um banco vetorial
- Expandir a base de campeões e guias
- Implementar novas intenções
- Melhorar a validação das respostas do LLM
- Ampliar a cobertura de testes automatizados
- Integrar fontes externas de dados

## Status

Projeto em desenvolvimento, criado para aprendizado e portfólio em AI
Engineering e Data Engineering.
