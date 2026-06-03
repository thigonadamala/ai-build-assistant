import json
from collections import Counter
from pathlib import Path


LOG_FILE = Path("logs/app_logs.jsonl")


def read_logs():
    if not LOG_FILE.exists():
        return []

    logs = []

    with LOG_FILE.open(
        "r",
        encoding="utf-8"
    ) as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            try:
                logs.append(
                    json.loads(line)
                )

            except json.JSONDecodeError:
                continue

    return logs


def get_stats():
    logs = read_logs()

    total_requests = len(logs)

    success_requests = sum(
        1
        for log in logs
        if log.get("event") == "request_success"
    )

    error_requests = sum(
        1
        for log in logs
        if log.get("event") == "request_error"
    )

    intents = Counter(
        log.get("intent")
        for log in logs
        if log.get("intent")
    )

    champions = Counter(
        log.get("champion")
        for log in logs
        if log.get("champion")
    )

    return {
        "total_requests": total_requests,
        "success_requests": success_requests,
        "error_requests": error_requests,
        "top_intents": intents.most_common(5),
        "top_champions": champions.most_common(5)
    }