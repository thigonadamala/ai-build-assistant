import json
from datetime import datetime
from pathlib import Path


LOG_DIR = Path("logs")
LOG_FILE = LOG_DIR / "app_logs.jsonl"


def write_log(event: dict):
    LOG_DIR.mkdir(
        exist_ok=True
    )

    log_entry = {
        "timestamp": datetime.now().isoformat(),
        **event
    }

    with LOG_FILE.open(
        "a",
        encoding="utf-8"
    ) as file:
        file.write(
            json.dumps(
                log_entry,
                ensure_ascii=False
            )
            + "\n"
        )