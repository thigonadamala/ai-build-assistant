from pipelines.etl_pipeline import run_etl

# Esse bloco garante que o código só execute quando rodado diretamente
# Evita execução automática se esse arquivo for importado em outro lugar
if __name__ == "__main__":
    run_etl()