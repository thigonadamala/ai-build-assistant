import pandas as pd

def extract():
    df = pd.read_csv("data/funcionarios.csv")
    print("DADOS BRUTOS:")
    print(df)
    return df

def transform(df):
    df = df.dropna()
    df = df.reset_index(drop=True)
    print("\nDADOS TRATADOS:")
    print(df)
    return df

if __name__ == "__main__":
    df = extract()
    df = transform(df)

    