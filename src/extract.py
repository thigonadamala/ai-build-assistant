import pandas as pd

def extract_csv(file_path):
    # Lê o CSV e transforma em DataFrame (estrutura padrão do pandas)
    df = pd.read_csv(file_path)

    # Log simples para visualizar os dados de entrada
    print("DADOS BRUTOS:")
    print(df)

    # Retorna os dados para o próximo passo do pipeline
    return df