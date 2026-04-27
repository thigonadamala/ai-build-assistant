# Comandos do Projeto

## Navegação e ambiente

```bash
cd data_pipeline
```
Acessa a pasta do projeto.

```bash
venv\Scripts\activate
```
Ativa o ambiente virtual do Python (usa as bibliotecas do projeto).

---

## Docker (Oracle)

```bash
docker start oracle-free
```
Inicia o container do Oracle.

```bash
docker ps
```
Lista containers em execução.

```bash
docker exec -it oracle-free bash
```
Entra no container Oracle.

```bash
exit
```
Sai do container.

---

## Oracle (SQLPlus)

```bash
sqlplus system/Oracle123@localhost:1521/FREEPDB1
```
Abre conexão com o banco Oracle.

```bash
exit
```
Sai do SQLPlus.

---

## Comandos SQL úteis

```sql
SELECT * FROM lol_builds;
```
Consulta todos os dados da tabela.

```sql
DELETE FROM lol_builds;
```
Remove todos os registros da tabela.

```sql
COMMIT;
```
Confirma alterações no banco.

---

## Pipeline

```bash
python -m scripts.run_pipeline
```
Executa o pipeline ETL completo (extract, transform, load).

---

## Git

```bash
git status
```
Mostra alterações no projeto.

```bash
git add .
```
Adiciona mudanças para commit.

```bash
git commit -m "mensagem"
```
Salva alterações no histórico.

```bash
git push
```
Envia alterações para o GitHub.

---

## Python

```bash
pip freeze
```
Lista pacotes instalados.

```bash
pip freeze > requirements.txt
```
Salva dependências do projeto.

---

## Variáveis de ambiente

```python
load_dotenv()
```
Carrega variáveis do arquivo .env.

```python
os.getenv("VAR")
```
Obtém valor de variável de ambiente.

---

## Dependências

```bash
pip list
```
Lista os pacotes instalados no ambiente virtual.

```bash
pip freeze
```
Lista os pacotes instalados com versões exatas.

```bash
pip freeze > requirements.txt
```
Atualiza o arquivo de dependências do projeto.

```bash
pip install -r requirements.txt
```
Instala as dependências listadas no requirements.txt.

---

## API (FastAPI)

```bash
uvicorn main:app --reload
```
Inicia a API localmente com recarregamento automático.

```text
http://127.0.0.1:8000
```
URL base da API.

```text
http://127.0.0.1:8000/docs
```
Interface interativa Swagger para testar endpoints.

```text
GET /
```
Retorna uma mensagem simples para validar se a API está funcionando.

```text
GET /builds
```
Retorna os dados de builds de LoL vindos do Oracle.

```bash
Ctrl + C
```
Para a execução da API no terminal.