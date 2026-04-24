# AI Build Assistant (LoL)

Projeto em construção focado em Engenharia de Dados + IA.

## Objetivo

Criar um sistema onde:

Usuário faz uma pergunta  
→ IA interpreta  
→ Gera SQL (quando necessário)  
→ Consulta o banco  
→ Responde em linguagem natural  

## Stack

- Python
- Pandas
- Oracle (Docker)
- VS Code

## Estrutura do Projeto

data_pipeline/

src/ → lógica do ETL  
extract.py → leitura de dados  
transform.py → tratamento  
load.py → inserção no banco  
db.py → conexão com Oracle  

pipelines/ → fluxo do ETL  
etl_pipeline.py  

scripts/ → execução  
run_pipeline.py  

data/ → arquivos de entrada  

## Como executar

1. Ativar ambiente virtual:

```bash
venv\Scripts\activate