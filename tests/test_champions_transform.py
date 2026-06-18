import pytest

from src.etl.champions.transform import transform_champions


def test_transform_champions_maps_tags_and_optional_fields():
    payload = {
        "version": "16.12.1",
        "data": {
            "Ahri": {
                "id": "Ahri",
                "key": "103",
                "name": "Ahri",
                "title": "the Nine-Tailed Fox",
                "tags": ["Mage", "Assassin"],
                "partype": "Mana"
            },
            "Aatrox": {
                "id": "Aatrox",
                "key": "266",
                "name": "Aatrox",
                "tags": ["Fighter"]
            }
        }
    }

    result = transform_champions(payload)

    assert result[0]["primary_tag"] == "Mage"
    assert result[0]["secondary_tag"] == "Assassin"
    assert result[1]["title"] is None
    assert result[1]["secondary_tag"] is None
    assert result[1]["version"] == "16.12.1"


def test_transform_champions_rejects_missing_required_field():
    payload = {
        "version": "16.12.1",
        "data": {
            "Ahri": {
                "id": "Ahri",
                "name": "Ahri"
            }
        }
    }

    with pytest.raises(
        ValueError,
        match="key"
    ):
        transform_champions(payload)
