__all__ = ['BruteForce']
from time import time

from .base import Results


class BruteForce:
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        self.len_pat = len(pattern)
        self.len_txt = len(text)

    def search(self, several_matches=False):
        results = Results()
        timer = time()
        for offset in range(self.len_txt - self.len_pat + 1):
            results.n_operations += 1
            patt_offset = 0
            while self.text[offset + patt_offset] == self.pattern[patt_offset]:
                results.n_operations += 1
                if patt_offset + 1 == self.len_pat:
                    results.matches.append(offset)
                    if not several_matches:
                        results.time = time() - timer
                        return results
                    break
                patt_offset += 1
        results.time = time() - timer
        return results
