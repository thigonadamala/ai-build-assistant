from src.extract import extract_csv
from src.transform import transform_funcionarios
from src.load import load_funcionarios

def run_etl():
    # Etapa 1: extrair dados do CSV
    df = extract_csv("data/funcionarios.csv")

    # Etapa 2: tratar e limpar os dados
    df = transform_funcionarios(df)

    # Etapa 3: carregar os dados no banco
    load_funcionarios(df)