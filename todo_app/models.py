from __future__ import annotations
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import List, Optional, Dict, Any

ISO_FMT = "%Y-%m-%dT%H:%M:%S"

@dataclass
class Task:
    id: int
    description: str
    created_at: str
    completed: bool = False
    completed_at: Optional[str] = None

    @classmethod
    def new(cls, id: int, description: str) -> "Task":
        return cls(id=id, description=description, created_at=datetime.utcnow().strftime(ISO_FMT))

    def mark_done(self) -> None:
        if not self.completed:
            self.completed = True
            self.completed_at = datetime.utcnow().strftime(ISO_FMT)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Task":
        return cls(**data)

TaskList = List[Task]
