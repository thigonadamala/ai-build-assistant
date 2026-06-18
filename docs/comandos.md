# Comandos do Projeto

Os comandos mais utilizados ficam no topo.

Os exemplos consideram PowerShell no Windows e a pasta:

```text
C:\Users\thika\data_pipeline
```

---

# Uso Diario

```powershell
cd C:\Users\thika\data_pipeline
```

Acessa a pasta raiz do projeto.

---

```powershell
venv\Scripts\Activate.ps1
```

Ativa o ambiente virtual Python.

O prompt deve comecar com:

```text
(venv)
```

---

```powershell
uvicorn main:app --reload
```

Executa a API diretamente no Windows com recarregamento automatico.

Use esta forma durante o desenvolvimento sem Docker:

```text
http://localhost:8000
```

Nao execute Uvicorn e Docker Compose ao mesmo tempo na porta `8000`.

---

```powershell
git status
```

Mostra arquivos modificados, novos, removidos e preparados para commit.

---

```powershell
git diff
```

Mostra as alteracoes ainda nao adicionadas ao stage.

---

```powershell
git add caminho\do\arquivo
```

Adiciona ao stage apenas o arquivo escolhido.

Antes do commit, confira:

```powershell
git diff --staged
```

---

```powershell
git commit -m "descricao objetiva da mudanca"
```

Cria um commit com as alteracoes preparadas.

---

```powershell
git push
```

Envia os commits locais para o repositorio remoto.

---

## Alternativa com Docker

Use Docker Compose quando quiser validar a aplicacao dentro do mesmo tipo de
runtime usado no deploy.

```powershell
docker compose up -d
```

Cria e inicia a API em segundo plano usando o `docker-compose.yml`.

---

```powershell
docker compose ps
```

Mostra o estado do container e a porta publicada.

---

```powershell
docker compose logs -f api
```

Acompanha os logs da API em tempo real.

Use `Ctrl + C` para sair da visualizacao. Isso nao encerra o container.

---

```powershell
docker compose down
```

Para e remove o container e a rede criados pelo Docker Compose.

A imagem Docker continua salva e pode ser usada novamente.

---

# Testes Rapidos da API

Antes dos testes, confirme que o container esta ativo:

```powershell
docker compose ps
```

## API

```powershell
curl.exe http://localhost:8000/
```

Valida Docker, Uvicorn e FastAPI.

---

## Banco de dados

```powershell
curl.exe "http://localhost:8000/builds?limit=1"
```

Valida a API, as variaveis da `.env`, a conexao TLS/TCPS com o Oracle
Autonomous Database e a consulta SQL.

---

## OpenAI e orquestracao

```powershell
curl.exe --get `
  --data-urlencode "question=Qual a build da Ahri?" `
  http://localhost:8000/ask
```

Valida o fluxo completo:

```text
FastAPI
-> LLM
-> orquestrador
-> service
-> banco
-> resposta
```

---

## Swagger

```text
http://localhost:8000/docs
```

Abre a documentacao interativa da API no navegador.

---

# Docker Compose

## Reconstruir e iniciar

```powershell
docker compose up -d --build
```

Reconstrui a imagem quando o codigo, o `Dockerfile` ou as dependencias mudaram
e inicia o container.

---

## Reconstruir sem cache

```powershell
docker compose build --no-cache
```

Reconstrui todas as camadas da imagem sem reutilizar cache.

Use quando precisar comprovar que a imagem nasce corretamente do zero.

Depois:

```powershell
docker compose up -d
```

---

## Reiniciar a API

```powershell
docker compose restart api
```

Reinicia somente o servico `api`.

Isso nao reconstrui a imagem. Se o codigo foi alterado, use `--build`.

---

## Ver configuracao interpretada

```powershell
docker compose config
```

Mostra como o Docker Compose interpretou o arquivo.

O resultado pode conter valores de variaveis. Nao compartilhe a saida sem
conferir se existem secrets.

---

# Docker

## Containers ativos

```powershell
docker ps
```

Lista todos os containers em execucao.

---

## Todos os containers

```powershell
docker ps -a
```

Inclui containers parados.

---

## Imagens locais

```powershell
docker image ls
```

Lista as imagens Docker armazenadas na maquina.

---

## Inspecionar o container

```powershell
docker inspect ai-build-assistant-api
```

Mostra configuracao, rede, mounts e estado do container.

Evite compartilhar a saida completa sem revisar variaveis sensiveis.

---

## Abrir um terminal no container

```powershell
docker exec -it ai-build-assistant-api sh
```

Abre um shell Linux dentro do container em execucao.

Para sair:

```powershell
exit
```

---

# Desenvolvimento Python Local

Use esta secao quando executar Python diretamente no Windows, fora do
container da API.

```powershell
venv\Scripts\Activate.ps1
```

Ativa o ambiente virtual.

O prompt deve comecar com:

```text
(venv)
```

---

```powershell
uvicorn main:app --reload
```

Executa a API diretamente no Windows com recarregamento automatico.

Nao execute ao mesmo tempo que o container se ambos tentarem usar a porta
`8000`.

---

```powershell
deactivate
```

Sai do ambiente virtual.

---

# Pipeline ETL

```powershell
venv\Scripts\Activate.ps1
```

Ativa o ambiente virtual Python.

---

```powershell
python -m pipelines.run_pipeline
```

Executa o pipeline ETL completo.

Fluxo:

```text
fonte de dados
-> extract
-> transform
-> load
-> Oracle Autonomous Database
```

---

# Testes Python Existentes

Use este comando como verificacao padrao do projeto:

```powershell
python -m pytest
```

Ele executa todos os testes da pasta `tests/` com saida resumida, sem chamar
OpenAI ou Oracle reais.

---

# Git

## Conferir alteracoes

```powershell
git status
```

```powershell
git diff
```

---

## Conferir arquivos preparados

```powershell
git diff --staged
```

Mostra exatamente o que entraria no proximo commit.

---

## Adicionar arquivos especificos

```powershell
git add caminho\do\arquivo
```

Prefira adicionar arquivos conscientemente em vez de usar `git add .` sem
revisar.

---

## Criar commit

```powershell
git commit -m "descricao objetiva da mudanca"
```

---

## Enviar para o GitHub

```powershell
git push
```

---

## Conferir se um arquivo esta ignorado

```powershell
git check-ignore -v caminho\do\arquivo
```

Mostra qual regra do `.gitignore` esta ignorando o arquivo.

---

## Procurar arquivos sensiveis rastreados

```powershell
git ls-files | Select-String -Pattern "\.env|wallet|\.pem|\.p12|\.key"
```

Ajuda na auditoria, mas nao substitui uma verificacao completa do conteudo e do
historico Git.

---

# Dependencias Python

```powershell
pip install -r requirements.txt
```

Instala as dependencias declaradas pelo projeto.

---

```powershell
pip list
```

Lista os pacotes instalados no ambiente ativo.

---

```powershell
pip freeze
```

Mostra pacotes e versoes instalados.

Nao sobrescreva `requirements.txt` automaticamente sem revisar dependencias
diretas e indiretas.

---

# Primeira Configuracao

Use somente ao preparar uma nova maquina.

```powershell
git clone https://github.com/thigonadamala/ai-build-assistant.git
```

---

```powershell
cd ai-build-assistant
```

---

```powershell
python -m venv venv
```

Cria o ambiente virtual Python.

---

```powershell
venv\Scripts\Activate.ps1
```

---

```powershell
pip install -r requirements.txt
```

---

# OCI CLI

Estes comandos sao especificos da Oracle Cloud. Consulte a documentacao quando
precisar; nao e necessario memoriza-los.

## Verificar instalacao

```powershell
oci --version
```

---

## Testar autenticacao

```powershell
oci iam region list
```

---

## Consultar namespace do Object Storage e OCIR

```powershell
oci os ns get
```

O namespace faz parte do endereco da imagem no Oracle Container Registry.

---

## Listar availability domains

```powershell
oci iam availability-domain list `
  --compartment-id <COMPARTMENT_OCID> `
  --query "data[].name"
```

---

## Encontrar uma subnet

```powershell
oci network subnet list `
  --compartment-id <COMPARTMENT_OCID> `
  --display-name "<NOME_DA_SUBNET>" `
  --query "data[0].id" `
  --raw-output
```

---

# Publicacao da Imagem no OCIR

## Criar uma tag para o registry

```powershell
docker tag data_pipeline-api:latest `
  gru.ocir.io/<NAMESPACE>/ai-build-assistant-api:latest
```

A tag nao cria outra imagem. Ela associa um novo nome ao mesmo conteudo local.

---

## Enviar a imagem

```powershell
docker push gru.ocir.io/<NAMESPACE>/ai-build-assistant-api:latest
```

O Docker precisa estar autenticado no OCIR.

---

## Confirmar imagens locais

```powershell
docker image ls
```

---

# Container Instance na OCI

Atualmente nao existe Container Instance ativa. Criar uma pode gerar cobranca.

Antes de executar qualquer comando desta secao:

1. revisar o JSON temporario;
2. confirmar os custos;
3. planejar os testes;
4. planejar a exclusao depois da validacao.

## Criar a partir de JSON

```powershell
oci container-instances container-instance create `
  --from-json "file://<ARQUIVO_TEMPORARIO>" `
  --wait-for-state SUCCEEDED `
  --max-wait-seconds 1200
```

O arquivo temporario pode conter secrets e deve ficar fora do projeto e ser
apagado depois do uso.

---

## Consultar logs

```powershell
oci container-instances container retrieve-logs `
  --container-id <CONTAINER_OCID> `
  --file -
```

---

## Testar uma API publicada

```powershell
curl.exe -sS --max-time 30 `
  -w "`nHTTP:%{http_code} TIME:%{time_total}`n" `
  "http://<IP_PUBLICO>:8000/builds?limit=1"
```

Confere corpo, status HTTP e tempo da requisicao.

---

## Excluir para interromper cobranca

```powershell
oci container-instances container-instance delete `
  --container-instance-id <CONTAINER_INSTANCE_OCID> `
  --force
```

Depois, confirme no Console ou pela CLI que a instancia nao esta mais ativa.

---

# URLs da API

```text
API:     http://localhost:8000
Swagger: http://localhost:8000/docs
Builds:  http://localhost:8000/builds?limit=1
Stats:   http://localhost:8000/stats
```

O endpoint `/ask` exige o parametro `question`.

---

# VS Code

```text
Ctrl + Shift + V
```

Abre a visualizacao formatada de um arquivo Markdown.
