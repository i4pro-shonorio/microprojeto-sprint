from __future__ import annotations
import json
from pathlib import Path
from typing import List
from .models import Task

DEFAULT_FILE = Path("tasks.json")

class Storage:
    def __init__(self, path: Path = DEFAULT_FILE):
        self.path = path

    def load(self) -> List[Task]:
        if not self.path.exists():
            return []
        try:
            with self.path.open("r", encoding="utf-8") as f:
                data = json.load(f)
            return [Task.from_dict(item) for item in data]
        except json.JSONDecodeError:
            raise RuntimeError("Arquivo JSON corrompido.")

    def save(self, tasks: List[Task]) -> None:
        with self.path.open("w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in tasks], f, ensure_ascii=False, indent=2)
