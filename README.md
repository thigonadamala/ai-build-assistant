# AI Build Assistant (LoL)

Projeto de Engenharia de Dados evoluindo para um sistema de IA capaz de responder perguntas sobre League of Legends utilizando dados estruturados, interpretação de linguagem natural e futuramente LLM + RAG.

---

# Objetivo

Construir um sistema onde:

Usuário faz uma pergunta

↓

Sistema interpreta intenção e entidades

↓

Consulta dados estruturados

↓

Responde em linguagem natural

---

# Estado Atual

## ETL

- Pipeline ETL funcional
- Extração de CSV
- Transformação e validação de dados
- Carga automatizada no Oracle

---

## Banco de Dados

- Oracle Free 23ai
- Executando via Docker
- Tabela `lol_builds` criada e populada

---

## API

- API construída com FastAPI
- Endpoint `/builds`
- Endpoint `/ask`
- Filtros dinâmicos
- Resposta em JSON

---

## Interpretação

O sistema já possui uma camada inicial de interpretação capaz de detectar:

```text
intent
champion
role
```

Exemplo:

```text
"qual a build da ahri"
↓
intent = build
champion = Ahri
```

---

## Resposta Natural

A API já gera respostas em linguagem natural.

Exemplo:

```text
"A melhor build encontrada para Ahri..."
```

---

# Stack

```text
Python
Pandas
Oracle
Docker
FastAPI
GitHub
```

---

# Arquitetura Atual

```text
Usuário
↓
FastAPI
↓
interpretation.py
↓
build_service.py
↓
Oracle
↓
response_generator.py
↓
Resposta final
```

---

# Estrutura do Projeto

```text
data_pipeline/

├── data/
│   ├── funcionarios.csv
│   └── lol_builds.csv

├── docs/
│   ├── arquitetura.md
│   ├── comandos.md
│   └── setup.md

├── src/
│   ├── build_service.py
│   ├── db.py
│   ├── extract.py
│   ├── interpretation.py
│   ├── load.py
│   ├── response_generator.py
│   └── transform.py

├── pipelines/
│   └── etl_pipeline.py

├── scripts/
│   ├── create_table.py
│   ├── run_pipeline.py
│   ├── select_data.py
│   └── test_connection.py

├── main.py
├── requirements.txt
└── .env
```

---

# Como Executar

## 1. Ativar ambiente virtual

```bash
venv\Scripts\activate
```

---

## 2. Subir Oracle no Docker

```bash
docker start oracle-free
```

---

## 3. Executar pipeline ETL

```bash
python -m scripts.run_pipeline
```

---

## 4. Executar API

```bash
uvicorn main:app --reload
```

---

# Endpoints

## GET /

Status da API.

---

## GET /builds

Retorna builds armazenadas no Oracle.

Exemplo:

```text
/builds?limit=2
```

---

## GET /ask

Recebe perguntas em linguagem natural.

Exemplo:

```text
/ask?question=qual a build da ahri
```

---

# Swagger

```text
http://127.0.0.1:8000/docs
```

---

# Próximos Passos

```text
LLM
RAG
múltiplas fontes de dados
busca contextual
agente de IA
deploy cloud
```

---

# Objetivo Final

Evoluir o projeto para um sistema de IA capaz de:

```text
interpretar perguntas
buscar dados em tempo real
consultar múltiplas fontes
gerar respostas contextualizadas
```

---

# Observações

Projeto em evolução contínua com foco em:

```text
Engenharia de Dados
Backend
IA Generativa
Arquitetura de Sistemas
```