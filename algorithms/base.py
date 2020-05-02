from dataclasses import dataclass, field
from typing import List


@dataclass
class Results:
    answers: List[int] = field(default_factory=list)
    time: float = .0
    weight = -1
    profit = -1
