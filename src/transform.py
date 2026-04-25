def transform_lol(df):
    # Remove linhas com valores nulos para evitar dados incompletos no banco
    df = df.dropna()

    # Reorganiza o índice após possíveis remoções
    df = df.reset_index(drop=True)

    # Exibe os dados após o tratamento
    print("\nDADOS TRATADOS (LoL):")
    print(df)

    # Retorna o DataFrame tratado para a etapa de carga
    return df