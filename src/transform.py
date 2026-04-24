def transform_funcionarios(df):
    # Remove linhas com valores nulos
    # Evita erro no banco e garante consistência dos dados
    df = df.dropna()

    # Reorganiza o índice após remoção de linhas
    # Mantém o DataFrame limpo e sequencial
    df = df.reset_index(drop=True)

    # Log dos dados após tratamento
    print("\nDADOS TRATADOS:")
    print(df)

    # Retorna os dados tratados
    return df