# Arquitetura do Projeto

## Visão Geral

Este projeto implementa um pipeline de dados (ETL) integrado com uma API construída em FastAPI.

O objetivo final é evoluir para um sistema com IA capaz de responder perguntas sobre League of Legends utilizando dados estruturados, interpretação de linguagem natural e futuramente LLM + RAG.

---

# Arquitetura Atual

## Fluxo Geral

Usuário faz pergunta

↓

FastAPI recebe a requisição

↓

interpretation.py interpreta intenção e entidades

↓

build_service.py consulta dados no Oracle

↓

response_generator.py gera resposta em linguagem natural

↓

API retorna JSON final

---

# Estrutura do Projeto

```text
data_pipeline/

├── data/
│   └── lol_builds.csv

├── docs/
│   ├── arquitetura.md
│   ├── comandos.md
│   └── setup.md

├── src/
│   ├── db.py
│   ├── build_service.py
│   ├── interpretation.py
│   └── response_generator.py

├── pipelines/
│   └── etl_pipeline.py

├── scripts/
│   └── run_pipeline.py

├── main.py
├── requirements.txt
└── .env
```

---

# Responsabilidade dos Arquivos

## main.py

Responsável pelas rotas da API FastAPI.

Endpoints atuais:

```text
/
/builds
/ask
```

---

## build_service.py

Responsável pela camada de dados.

Funções:

```text
get_builds()
get_available_champions()
```

Realiza:

```text
consultas SQL
filtros
ordenação
limite de resultados
```

---

## interpretation.py

Responsável por interpretar perguntas do usuário.

Detecta:

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

## response_generator.py

Responsável por gerar respostas em linguagem natural.

Exemplo:

```text
"A melhor build encontrada para Ahri..."
```

---

## db.py

Responsável pela conexão com Oracle.

Utiliza:

```text
oracledb
dotenv
variáveis de ambiente
```

---

# Banco de Dados

Banco utilizado:

```text
Oracle Free 23ai
```

Executado localmente via Docker.

Tabela principal atual:

```sql
CREATE TABLE lol_builds (
    champion VARCHAR2(50),
    role VARCHAR2(20),
    item VARCHAR2(50),
    winrate NUMBER
);
```

---

# API

Framework:

```text
FastAPI
```

Inicialização:

```bash
uvicorn main:app --reload
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

---

# Objetivo Futuro

Evoluir o sistema para:

```text
LLM
RAG
busca contextual
múltiplas fontes de dados
agente de IA
deploy em cloud
```