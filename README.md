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

O projeto possui dois fluxos de ETL. O pipeline inicial carrega builds a
partir de CSV:

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

O pipeline de campeões consulta a versão mais recente do Riot Data Dragon,
transforma o `champion.json` e realiza carga idempotente no Oracle com `MERGE`:

```text
Data Dragon
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
LOL_CHAMPIONS
```

Execução:

```bash
python -m src.etl.champions.pipeline
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
- `lol_champions`

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
- Gera chunks a partir das seções
- Gera embeddings com a OpenAI API
- Ordena chunks por similaridade de cosseno
- Recupera informações do campeão e de guias por relevância
- Utiliza esse contexto na intenção `overview`

Os embeddings ainda são calculados em memória durante a requisição. O projeto
ainda não utiliza banco vetorial nem persistência do índice semântico.

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
|   |   `-- champions/
|   |-- observability/
|   |-- rag/
|   `-- services/
|-- tests/
|-- main.py
|-- Dockerfile
|-- docker-compose.yml
`-- requirements.txt
```

O código atual de embeddings está em `src/ai/embedding_service.py`. O
diretório `src/embeddings/` permanece reservado para uma futura camada de
indexação ou persistência.

## Configuração Local

### 1. Criar e ativar o ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Instalar as dependências

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
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

- Persistir embeddings ou adicionar um banco vetorial
- Evitar recalcular embeddings de documentos em cada requisição
- Expandir a base de campeões e guias
- Implementar novas intenções
- Melhorar a validação das respostas do LLM
- Ampliar a cobertura de testes automatizados
- Expandir o ETL para itens, runas e outras fontes oficiais

## Status

Projeto em desenvolvimento, criado para aprendizado e portfólio em AI
Engineering e Data Engineering.
