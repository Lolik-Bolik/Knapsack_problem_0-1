from dataclasses import dataclass, field
from typing import List

@dataclass
class Results:
    answers: List[int] = field(default_factory=list)
    time: float = .0
    weight = 0
    profit = 0
    counter = 0
