# Compilado do Projeto - AI Build Assistant (LoL)

Este projeto e um sistema em Python que comecou como um pipeline de Engenharia de Dados e esta evoluindo para uma API com IA capaz de responder perguntas sobre League of Legends usando dados estruturados, interpretacao de linguagem natural e futuramente RAG.

## Objetivo geral

Construir um assistente que funcione assim:

```text
Usuario faz uma pergunta em linguagem natural
-> sistema interpreta intent e entidades
-> consulta dados estruturados no Oracle
-> gera uma resposta em linguagem natural
-> retorna JSON pela API
```

Exemplo desejado:

```text
Pergunta: "qual a build da ahri mid?"
Interpretacao: intent=build, champion=Ahri, role=mid, limit=1
Consulta: busca a melhor build da Ahri mid no banco
Resposta: "A melhor build encontrada para Ahri na rota mid usa Luden, com winrate de 52.3%."
```

## Stack atual

- Python
- FastAPI
- Pandas
- Oracle Free 23ai via Docker
- python-oracledb
- python-dotenv
- OpenAI API
- Uvicorn

## Estado atual

O projeto ja tem:

- Pipeline ETL funcional lendo CSV, tratando dados e carregando no Oracle.
- Banco Oracle local em Docker.
- Tabela principal `lol_builds` com dados de builds de LoL.
- API FastAPI com endpoints `/`, `/builds` e `/ask`.
- Consulta de builds com filtros dinamicos por campeao, rota e limite.
- Integracao com LLM no endpoint `/ask` para interpretar perguntas.
- Gerador simples de resposta natural.
- Parser manual antigo em `src/interpretation.py`, mas atualmente o `/ask` usa `src/llm_service.py`.

## Estrutura do projeto

```text
data_pipeline/
├── data/
│   ├── funcionarios.csv
│   └── lol_builds.csv
├── docs/
│   ├── arquitetura.md
│   ├── comandos.md
│   ├── setup.md
│   └── compilado_projeto.md
├── pipelines/
│   └── etl_pipeline.py
├── scripts/
│   ├── create_table.py
│   ├── run_pipeline.py
│   ├── select_data.py
│   └── test_connection.py
├── src/
│   ├── build_service.py
│   ├── db.py
│   ├── extract.py
│   ├── interpretation.py
│   ├── llm_service.py
│   ├── load.py
│   ├── response_generator.py
│   └── transform.py
├── main.py
├── requirements.txt
├── test_llm.py
└── .env
```

## Dados atuais

Arquivo `data/lol_builds.csv`:

```csv
champion,role,item,winrate
Ahri,mid,Luden,52.3
Zed,mid,Duskblade,49.8
Jinx,adc,Kraken,51.2
Thresh,support,Locket,50.1
```

Tabela principal esperada no Oracle:

```sql
CREATE TABLE lol_builds (
    champion VARCHAR2(50),
    role VARCHAR2(20),
    item VARCHAR2(50),
    winrate NUMBER
);
```

## Fluxo ETL

O pipeline fica em `pipelines/etl_pipeline.py` e roda:

```text
extract_csv("data/lol_builds.csv")
-> transform_lol(df)
-> load_lol(df)
```

Arquivos envolvidos:

- `src/extract.py`: le o CSV com Pandas.
- `src/transform.py`: remove linhas nulas e reseta indice.
- `src/load.py`: insere no Oracle usando `executemany`.
- `src/db.py`: centraliza conexao com Oracle usando variaveis do `.env`.
- `scripts/run_pipeline.py`: executa o ETL completo.

Comando:

```bash
python -m scripts.run_pipeline
```

## API atual

Arquivo principal: `main.py`

Endpoints:

```text
GET /
GET /builds
GET /ask
```

### GET /

Retorna status simples:

```json
{"message": "API LoL funcionando"}
```

### GET /builds

Consulta builds direto no Oracle.

Parametros opcionais:

- `champion`
- `role`
- `limit`

Exemplos:

```text
/builds
/builds?limit=2
/builds?champion=Ahri&role=mid&limit=1
```

### GET /ask

Recebe uma pergunta em linguagem natural.

Exemplo:

```text
/ask?question=qual a build da ahri mid
```

Fluxo atual do `/ask`:

```text
question
-> ask_llm(question)
-> retorna filtros JSON: intent, champion, role, limit
-> se intent == build, chama get_builds()
-> gera resposta com generate_answer()
-> retorna question, interpreted_filters, answer e data
```

Intents implementadas de fato:

- `build`: consulta o banco e gera resposta.

Intents reconhecidas ou previstas, mas ainda nao implementadas de ponta a ponta:

- `runes`
- `counters`
- `matchup`
- `winrate`
- `skills`
- `synergies`
- `power_spike`
- `general`

No `main.py`, `runes`, `counters` e `matchup` retornam mensagens dizendo que ainda nao foram implementados.

## LLM

Arquivo: `src/llm_service.py`

Funcao principal:

```python
ask_llm(question: str)
```

Ela usa:

```python
client.responses.create(
    model="gpt-4.1-mini",
    input="..."
)
```

O prompt pede para o modelo retornar somente JSON valido com:

```json
{
  "intent": "build",
  "champion": "Ahri",
  "role": "mid",
  "limit": 1
}
```

Se o JSON vier invalido, o codigo retorna fallback:

```json
{
  "intent": "general",
  "champion": null,
  "role": null,
  "limit": 1,
  "error": "Resposta invalida do LLM",
  "raw_response": "..."
}
```

## Camada de dados

Arquivo: `src/build_service.py`

Funcoes:

```python
get_available_champions()
get_builds(champion=None, role=None, limit=None)
```

`get_builds` monta SQL dinamico:

- filtra por campeao com `LOWER(champion) = LOWER(:champion)`
- filtra por rota com `LOWER(role) = LOWER(:role)`
- ordena por `winrate DESC`
- aplica limite com subquery e `ROWNUM <= :limit`
- retorna JSON com `total`, `filters` e `data`

## Geracao de resposta

Arquivo: `src/response_generator.py`

Funcao:

```python
generate_answer(intent, best_build)
```

Para `build`, retorna algo como:

```text
A melhor build encontrada para Ahri na rota mid usa Luden, com winrate de 52.3%.
```

Para `winrate`, tambem existe texto preparado, mas o endpoint `/ask` ainda nao roteia `winrate` para consulta.

## Parser manual antigo

Arquivo: `src/interpretation.py`

Existe uma funcao `interpret_question(question, available_champions)` que detecta manualmente:

- `intent`
- `champion`
- `role`
- `limit`

Ela procura palavras como `build`, `item`, `winrate`, `taxa de vitoria`, `mid`, `adc`, `support`.

Importante: atualmente o endpoint `/ask` nao usa esse parser. Ele usa o LLM em `src/llm_service.py`.

## Comandos principais

Ativar ambiente:

```bash
venv\Scripts\activate
```

Subir Oracle:

```bash
docker start oracle-free
```

Rodar ETL:

```bash
python -m scripts.run_pipeline
```

Rodar API:

```bash
uvicorn main:app --reload
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

Testar LLM isolado:

```bash
python test_llm.py
```

## Observacoes importantes

- O `.env` existe e deve conter `OPENAI_API_KEY`, `DB_USER`, `DB_PASSWORD` e `DB_DSN`.
- Nao compartilhar valores reais do `.env` em chat.
- A documentacao atual ainda fala bastante do `interpretation.py`, mas o codigo atual do `/ask` ja migrou para LLM.
- Alguns arquivos/documentos parecem estar com problema de encoding nos acentos, aparecendo caracteres como `Ã£`, `Ã©`, etc.
- Os scripts `create_table.py` e `select_data.py` ainda estao voltados para a tabela antiga `funcionarios`, nao para `lol_builds`.
- O projeto esta com `git status` limpo no momento deste compilado.

## Proximos passos provaveis

- Corrigir encoding dos arquivos/documentos para UTF-8.
- Atualizar `scripts/create_table.py` para criar `lol_builds` em vez de `funcionarios`, ou criar script separado.
- Atualizar `scripts/select_data.py` para consultar `lol_builds`.
- Melhorar robustez do `llm_service.py` usando schema/JSON mode se disponivel.
- Roteiar `winrate` no `/ask`, pois o `response_generator.py` ja tem resposta para isso.
- Implementar intents futuras: runas, counters, matchups, skills, sinergias e power spikes.
- Expandir a fonte de dados alem do CSV pequeno atual.
- Futuramente adicionar RAG ou integracao com APIs/fontes externas de League of Legends.
