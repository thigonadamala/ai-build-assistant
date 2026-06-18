def transform_champions(data):
    if not isinstance(data, dict):
        raise ValueError(
            "Payload de campeoes deve ser um dicionario."
        )

    version = data.get("version")
    raw_champions = data.get("data")

    if not version:
        raise ValueError(
            "Payload de campeoes sem versao."
        )

    if not isinstance(raw_champions, dict):
        raise ValueError(
            "Payload de campeoes sem campo data valido."
        )

    champions = []

    for champion in raw_champions.values():
        required_fields = ("id", "key", "name")
        missing_fields = [
            field
            for field in required_fields
            if not champion.get(field)
        ]

        if missing_fields:
            raise ValueError(
                "Campeao sem campos obrigatorios: "
                f"{', '.join(missing_fields)}"
            )

        tags = champion.get("tags", [])

        champions.append({
            "riot_id": champion["id"],
            "champion_key": champion["key"],
            "name": champion["name"],
            "title": champion.get("title"),
            "primary_tag": tags[0] if len(tags) > 0 else None,
            "secondary_tag": tags[1] if len(tags) > 1 else None,
            "partype": champion.get("partype"),
            "version": version
        })

    print(
        f"Campeões transformados: {len(champions)}"
    )

    return champions
