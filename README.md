# AI Build Assistant (LoL)

Projeto de Engenharia de Dados evoluindo para um sistema de IA capaz de responder perguntas sobre builds de League of Legends.

---

## Objetivo

Construir um sistema onde:

Usuário faz uma pergunta  
→ IA interpreta  
→ Decide se precisa de SQL  
→ Consulta o banco de dados  
→ Responde em linguagem natural  

---

## Estado atual

- Pipeline ETL funcional (Python + Pandas)
- Dados de LoL sendo carregados no Oracle
- Banco rodando em Docker
- API inicial com FastAPI
- Projeto versionado no GitHub
- Documentação básica criada

---

## Stack

- Python
- Pandas
- Oracle (Docker)
- FastAPI

---

## Estrutura do Projeto

```
data_pipeline/
├── data/          # arquivos CSV
├── docs/          # documentação
├── pipelines/     # fluxo ETL
├── scripts/       # execução
├── src/           # lógica do projeto
├── main.py        # API (FastAPI)
```

---

## Como executar

### 1. Ativar ambiente virtual

```bash
venv\Scripts\activate
```

### 2. Subir o Oracle

```bash
docker start oracle-free
```

### 3. Rodar o pipeline

```bash
python -m scripts.run_pipeline
```

### 4. Rodar a API

```bash
uvicorn main:app --reload
```

---

## Endpoints

- `GET /` → status da API  
- `GET /builds` → retorna builds de LoL do banco  

---

## Próximos passos

- Integração com LLM
- Implementação de RAG
- Criação de agente de decisão
- Deploy em nuvem

---

## Observações

Projeto em evolução contínua com foco em Engenharia de Dados e IA aplicada.