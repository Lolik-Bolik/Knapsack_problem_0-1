from dataclasses import dataclass, field
from typing import List


@dataclass
class Results:
    answers: List[int] = field(default_factory=list)
    n_operations: int = 0
    time: float = .0
