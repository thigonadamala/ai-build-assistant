# Comandos do Projeto

---

```bash
Ctrl + Shift + V
```

Abre a visualização formatada do arquivo `.md` no VS Code.

---

# Navegação e Ambiente

```bash
cd data_pipeline
```

Acessa a pasta raiz do projeto.

---

```bash
venv\Scripts\activate
```

Ativa o ambiente virtual Python.

---

# Docker (Oracle)

```bash
docker start oracle-free
```

Inicia o container Oracle.

---

```bash
docker stop oracle-free
```

Para o container Oracle.

---

```bash
docker ps
```

Lista containers em execução.

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

Consulta todos os dados.

---

```sql
DELETE FROM lol_builds;
```

Remove registros da tabela.

---

```sql
COMMIT;
```

Confirma alterações no Oracle.

---

# Pipeline ETL

```bash
python -m scripts.run_pipeline
```

Executa o pipeline ETL completo.

Fluxo:

```text
extract
↓
transform
↓
load
```

---

# Scripts Auxiliares

```bash
python -m scripts.create_table
```

Cria tabelas Oracle.

---

```bash
python -m scripts.select_data
```

Executa consultas manuais no banco.

---

```bash
python -m scripts.test_connection
```

Testa conexão com Oracle.

---

# API (FastAPI)

```bash
uvicorn main:app --reload
```

Inicia a API localmente.

---

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

Retorna builds do Oracle.

Exemplo:

```text
/builds?limit=2
```

---

```text
GET /ask
```

Recebe perguntas em linguagem natural.

Exemplo:

```text
/ask?question=qual a build da ahri
```

---

```bash
Ctrl + C
```

Para execução da API.

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

Envia alterações para GitHub.

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

Atualiza requirements.txt.

---

```bash
pip install -r requirements.txt
```

Instala dependências do projeto.

---

# Variáveis de Ambiente

```python
load_dotenv()
```

Carrega variáveis do arquivo `.env`.

---

```python
os.getenv("VAR")
```

Obtém valor de variável de ambiente.