import httpx


DATA_DRAGON_VERSIONS_URL = (
    "https://ddragon.leagueoflegends.com/api/versions.json"
)
DATA_DRAGON_CHAMPIONS_URL = (
    "https://ddragon.leagueoflegends.com/cdn/"
    "{version}/data/en_US/champion.json"
)


def get_latest_version(client):
    response = client.get(DATA_DRAGON_VERSIONS_URL)
    response.raise_for_status()

    versions = response.json()

    if not versions:
        raise RuntimeError(
            "Data Dragon nao retornou nenhuma versao."
        )

    return versions[0]


def extract_champions():
    with httpx.Client(timeout=30) as client:
        version = get_latest_version(client)
        champions_url = DATA_DRAGON_CHAMPIONS_URL.format(
            version=version
        )

        response = client.get(champions_url)
        response.raise_for_status()

        data = response.json()

    if "data" not in data:
        raise RuntimeError(
            "Resposta do Data Dragon sem dados de campeoes."
        )

    print(f"Versao Data Dragon: {version}")
    print(f"Campeoes encontrados: {len(data['data'])}")

    return data
