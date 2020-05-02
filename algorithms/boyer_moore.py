__all__ = ['BoyerMoore']
from .base import Results
from time import time
from _collections import defaultdict


class BoyerMoore:
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern

        self.m = len(pattern)
        self.n = len(text)
        self.badMatchTable = defaultdict(lambda: -1)
        for i in range(self.m): self.badMatchTable[ord(pattern[i])] = i

    def search(self, **kwargs):
        results = Results
        results.n_operations = 0
        start = time()
        shift = 0
        while (shift <= self.n - self.m):
            j = self.m - 1
            results.n_operations += 1
            while j >= 0 and self.pattern[j] == self.text[shift + j]:
                j -= 1
                results.n_operations += 1
            if j < 0:
                shift += (self.m - self.badMatchTable[ord(self.text[shift + self.m])]
                          if shift + self.m < self.n else 1)
            else:
                shift += max(1, j - self.badMatchTable[ord(self.text[shift + j])])
        finish = time()
        results.time = finish - start
        return results
