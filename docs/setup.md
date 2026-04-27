# Setup do Projeto

## 1. Clonar o repositório

```bash
git clone https://github.com/thigonadamala/ai-build-assistant.git
cd ai-build-assistant
```

---

## 2. Criar e ativar ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 4. Subir o Oracle no Docker

```bash
docker start oracle-free
```

---

## 5. Rodar o pipeline

```bash
python -m scripts.run_pipeline
```

---

## Observações

- Certifique-se que o Docker está rodando
- Configure o arquivo `.env` com usuário, senha e DSN do Oracle