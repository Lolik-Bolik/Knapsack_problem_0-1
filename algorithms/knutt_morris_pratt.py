__all__ = ['KnuttMorrisPratt']
from time import time

from .base import Results


class KnuttMorrisPratt:
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        self.len_pat = len(pattern)
        self.len_txt = len(text)

    def _compute_prefix_function(self):
        result = [-1] * self.len_pat
        k = -1
        n_operations = 0
        for i in range(1, self.len_pat):
            n_operations += 1
            while k > -1 and self.pattern[k + 1] != self.pattern[i]:
                k = result[k]
            if self.pattern[k + 1] == self.pattern[i]:
                k += 1
                result[i] = k
            i += 1
        return result, n_operations

    def search(self, several_matches=False):
        results = Results()
        pref, results.n_operations = self._compute_prefix_function()
        timer = time()
        tail = -1
        for offset in range(self.len_txt):
            results.n_operations += 1
            while tail > -1 and self.pattern[tail + 1] != self.text[offset]:
                results.n_operations += 1
                tail = pref[tail]
            if self.pattern[tail + 1] == self.text[offset]:
                results.n_operations += 1
                tail += 1
            if tail == self.len_pat - 1:
                results.n_operations += 1
                results.matches.append(offset - tail)
                if not several_matches:
                    results.time = time() - timer
                    return results
                tail = pref[tail]
            offset += 1
        results.time = time() - timer
        return results
