# AI Build Assistant (LoL)

Projeto de Engenharia de Dados, Backend e IA Generativa focado na construção de um assistente capaz de responder perguntas sobre League of Legends utilizando dados estruturados, LLMs e RAG.

---

# Objetivo

Construir um sistema capaz de:

```text
Usuário faz uma pergunta

↓

Sistema interpreta intenção e entidades

↓

Consulta dados estruturados

↓

Recupera contexto adicional (RAG)

↓

Gera resposta em linguagem natural

↓

Retorna resposta pela API
```

Exemplo:

```text
Pergunta:
"me fala sobre a Ahri"

↓

Intent:
overview

↓

Campeão:
Ahri

↓

Consulta banco + conhecimento contextual

↓

Resposta natural gerada pela aplicação
```

---

# Estado Atual

## ETL

Pipeline funcional para carga de dados.

Fluxo:

```text
CSV
↓
Extract
↓
Transform
↓
Load
↓
Oracle
```

Capacidades atuais:

* Leitura de CSV com Pandas
* Tratamento de dados
* Inserção automatizada no Oracle
* Estrutura modularizada

---

## Banco de Dados

Banco utilizado:

```text
Oracle Free 23ai
```

Executado em container Docker.

Atualmente contém:

* Builds
* Counters
* Runas
* Dados utilizados pela API

---

## API

Construída com:

```text
FastAPI
```

Endpoints atuais:

```text
GET /
GET /builds
GET /ask
GET /stats
```

---

## LLM

A aplicação utiliza LLM para interpretar perguntas do usuário.

Exemplo:

```text
"qual a build da ahri mid?"
```

↓

```json
{
  "intent": "build",
  "champion": "Ahri",
  "role": "mid",
  "limit": 1
}
```

Isso elimina grande parte da lógica manual de parsing.

---

## RAG

Primeira versão funcional já implementada.

Estrutura atual:

```text
knowledge/

├── champions/
└── guides/
```

O sistema recupera conhecimento contextual para enriquecer respostas utilizando arquivos Markdown especializados.

Exemplo:

```text
Pergunta
↓
LLM interpreta
↓
Oracle retorna dados estruturados
↓
RAG recupera contexto
↓
Resposta final
```

---

# Stack

```text
Python
FastAPI
Oracle Database
Docker
Docker Compose
Pandas
OpenAI API
python-oracledb
python-dotenv
Git
GitHub
```

---

# Arquitetura Atual

```text
Usuário

↓

FastAPI

↓

Orchestrator

↓

LLM

↓

Serviços da aplicação

↓

Oracle + RAG

↓

Resposta natural

↓

JSON
```

---

# Estrutura do Projeto

```text
data_pipeline/

├── data/
│   ├── funcionarios.csv
│   └── lol_builds.csv
│
├── docs/
│   ├── comandos.md
│   └── contexto_codex.md
│
├── knowledge/
│   ├── champions/
│   └── guides/
│
├── pipelines/
│   ├── etl_pipeline.py
│   └── run_pipeline.py
│
├── scripts/
│   └── database/
│
├── src/
│   ├── ai/
│   ├── core/
│   ├── database/
│   ├── embeddings/
│   ├── etl/
│   ├── observability/
│   ├── rag/
│   └── services/
│
├── tests/
│
├── Dockerfile
├── docker-compose.yml
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

## 2. Iniciar Oracle

```bash
docker start oracle-free
```

---

## 3. Executar ETL

```bash
python -m pipelines.run_pipeline
```

---

## 4. Executar API localmente

```bash
uvicorn main:app --reload
```

---

## 5. Executar aplicação via Docker

```bash
docker compose up
```

---

# Endpoints

## GET /

Status da aplicação.

Exemplo:

```json
{
  "message": "API LoL funcionando"
}
```

---

## GET /builds

Consulta builds armazenadas no Oracle.

Exemplo:

```text
/builds?champion=Ahri
```

---

## GET /ask

Recebe perguntas em linguagem natural.

Exemplo:

```text
/ask?question=me fala sobre a ahri
```

Fluxo:

```text
Pergunta
↓
LLM
↓
Filtros estruturados
↓
Banco + RAG
↓
Resposta natural
```

---

## GET /stats

Retorna estatísticas da aplicação.

Exemplo:

```json
{
  "total_requests": 0,
  "success_requests": 0,
  "error_requests": 0
}
```

---

# Swagger

```text
http://127.0.0.1:8000/docs
```

---

# Visão de Longo Prazo

Transformar o AI Build Assistant em um sistema completo de AI Engineering capaz de:

```text
Interpretar perguntas complexas

Consultar múltiplas fontes de dados

Utilizar RAG especializado

Implementar busca semântica por embeddings

Utilizar agentes para tomada de decisão

Combinar banco de dados, documentos e APIs externas

Gerar respostas contextualizadas e explicáveis

Operar como um assistente especializado de League of Legends
```

---

# Observações

Este projeto tem foco educacional e prático para estudo de:

```text
Engenharia de Dados

Backend

LLMs

RAG

AI Engineering

Arquitetura de Sistemas
```
