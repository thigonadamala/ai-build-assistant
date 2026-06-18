from src.etl.champions.extract import extract_champions
from src.etl.champions.transform import transform_champions
from src.etl.champions.load import load_champions


def run_champions_pipeline():
    data = extract_champions()
    champions = transform_champions(data)
    loaded_count = load_champions(champions)

    return {
        "version": data["version"],
        "extracted": len(champions),
        "loaded": loaded_count
    }


if __name__ == "__main__":
    run_champions_pipeline()
