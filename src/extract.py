import pandas as pd

def extract_csv(file_path):
    # Lê o CSV e retorna como DataFrame
    df = pd.read_csv(file_path)

    print("DADOS BRUTOS:")
    print(df)

    return df