# Comandos do Projeto

Os comandos mais utilizados ficam no topo.

---

# Uso Diário

```bash
cd data_pipeline
```

Acessa a pasta raiz do projeto.

---

```bash
venv\Scripts\activate
```

Ativa o ambiente virtual Python.

O prompt deve ficar:

```text
(venv) PS C:\Users\thika\data_pipeline>
```

---

```bash
docker start oracle-free
```

Inicia o Oracle.

---

```bash
docker compose up
```

Sobe a aplicação completa via Docker.

A aplicação passa a rodar dentro de um container Docker.

---

```bash
Ctrl + C
```

Para a aplicação iniciada pelo Docker Compose.

---

```bash
git status
```

Verifica alterações do projeto.

---

# Primeira Configuração do Projeto

Utilizar apenas na primeira vez que o projeto for configurado.

---

```bash
git clone https://github.com/thigonadamala/ai-build-assistant.git
```

Clona o repositório do GitHub para a máquina local.

---

```bash
cd ai-build-assistant
```

Acessa a pasta do projeto recém clonado.

---

```bash
python -m venv venv
```

Cria um ambiente virtual Python.

O ambiente virtual isola as dependências do projeto e evita conflitos com outros projetos instalados na máquina.

---

```bash
venv\Scripts\activate
```

Ativa o ambiente virtual criado.

---

```bash
pip install -r requirements.txt
```

Instala todas as dependências listadas no arquivo requirements.txt.

---

# Docker

## Containers

```bash
docker ps
```

Lista containers em execução.

---

```bash
docker start oracle-free
```

Inicia o Oracle.

---

```bash
docker stop oracle-free
```

Para o Oracle.

---

```bash
docker exec -it oracle-free bash
```

Entra no container Oracle.

---

```bash
exit
```

Sai do container.

---

## Imagens

```bash
docker images
```

Lista imagens Docker.

---

```bash
docker build -t ai-build-assistant .
```

Lê o Dockerfile e cria uma imagem contendo Python, dependências e o código da aplicação.

---

## Docker Compose

```bash
docker compose up
```

Cria e inicia o container da aplicação utilizando as configurações do docker-compose.yml.

---

```bash
Ctrl + C
```

Para a aplicação iniciada pelo Docker Compose.

---

## Redes

```bash
docker network ls
```

Lista as redes Docker existentes.

---

```bash
docker network inspect ai-build-network
```

Mostra os containers conectados à rede do projeto.

---

Rede utilizada:

```text
ai-build-network
```

Responsável pela comunicação entre:

```text
Container API
↔
Container Oracle
```

---

# Desenvolvimento Local

Utilizar apenas quando não estiver usando Docker para a API.

```bash
uvicorn main:app --reload
```

Inicia a API localmente no Windows.

---

# Oracle (SQLPlus)

```bash
sqlplus system/Oracle123@localhost:1521/FREEPDB1
```

Abre conexão com Oracle via SQLPlus.

---

```bash
exit
```

Sai do SQLPlus.

---

# SQL Útil

```sql
SELECT * FROM lol_builds;
```

Consulta todos os registros.

---

```sql
DELETE FROM lol_builds;
```

Remove todos os registros.

---

```sql
COMMIT;
```

Confirma alterações no Oracle.

---

# Pipeline ETL

Antes de executar:

```bash
venv\Scripts\activate
```

Ativa o ambiente virtual.

---

```bash
python -m pipelines.run_pipeline
```

Executa o pipeline ETL completo.

Fluxo:

```text
CSV
↓
extract.py
↓
transform.py
↓
load.py
↓
Oracle
```

Utilizado para carregar ou recarregar dados no banco.

---

# API

```text
http://127.0.0.1:8000
```

URL base da API.

---

```text
http://127.0.0.1:8000/docs
```

Swagger da API.

---

# Endpoints

```text
GET /
```

Retorna status da API.

---

```text
GET /builds
```

Retorna builds armazenadas no Oracle.

Exemplo:

```text
/builds?champion=Ahri
```

---

```text
GET /ask
```

Recebe perguntas em linguagem natural.

Exemplo:

```text
/ask?question=me fala sobre a ahri
```

---

```text
GET /stats
```

Retorna estatísticas da aplicação.

---

# Git

```bash
git status
```

Mostra alterações do projeto.

---

```bash
git add .
```

Adiciona arquivos ao stage.

---

```bash
git commit -m "mensagem"
```

Cria commit.

---

```bash
git push
```

Envia alterações para o GitHub.

---

# Dependências Python

```bash
pip list
```

Lista pacotes instalados.

---

```bash
pip freeze
```

Lista dependências com versões exatas.

---

```bash
pip freeze > requirements.txt
```

Atualiza o requirements.txt com as versões atualmente instaladas.

---

```bash
pip install -r requirements.txt
```

Instala dependências do projeto.

---

# VS Code

```text
Ctrl + Shift + V
```

Abre a visualização formatada de arquivos Markdown.
