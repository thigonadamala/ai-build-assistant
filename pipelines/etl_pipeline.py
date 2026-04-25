from src.extract import extract_csv
from src.transform import transform_lol
from src.load import load_lol

def run_etl():
    # Etapa 1: lê os dados de builds de LoL do CSV
    df = extract_csv("data/lol_builds.csv")

    # Etapa 2: limpa e prepara os dados
    df = transform_lol(df)

    # Etapa 3: insere os dados tratados no Oracle
    load_lol(df)