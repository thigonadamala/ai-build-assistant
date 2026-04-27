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