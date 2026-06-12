import pandas as pd
import pytest

from src.etl import load


def failing_connection():
    raise RuntimeError("database unavailable")


def test_load_lol_propagates_database_error(monkeypatch):
    monkeypatch.setattr(
        load,
        "get_connection",
        failing_connection
    )

    dataframe = pd.DataFrame()

    with pytest.raises(RuntimeError, match="database unavailable"):
        load.load_lol(dataframe)
