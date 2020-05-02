__all__ = ['KarpRabin']
from time import time

from .base import Results


class KarpRabin:
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        self.len_pat = len(pattern)
        self.len_txt = len(text)
        self.d = 256  # Num characters in alphabet
        self.q = self._next_prime(self.len_pat)
        self.h = pow(self.d, self.len_pat - 1) % self.q
        self.phash, self.thash = 0, 0

        for i in range(self.len_pat):
            self.phash = (self.d * self.phash + ord(pattern[i])) % self.q
            self.thash = (self.d * self.thash + ord(text[i])) % self.q

    def search(self, several_matches=False):
        results = Results()
        timer = time()
        for offset in range(self.len_txt - self.len_pat + 1):
            results.n_operations += 1
            if self.thash == self.phash:
                collision = False
                for j in range(self.len_pat):
                    results.n_operations += 1
                    if self.text[j + offset] != self.pattern[j]:
                        collision = True
                        break
                if not collision:
                    results.matches.append(offset)
                    if not several_matches:
                        results.time = time() - timer
                        return results
            if offset < self.len_txt - self.len_pat:
                self.thash = self.thash - ord(self.text[offset]) * self.h
                self.thash = (self.thash * self.d + ord(self.text[offset + self.len_pat])) % self.q

                if self.thash < 0:
                    self.thash += self.q

        results.time = time() - timer
        return results

    @staticmethod
    def _check_prime(value):
        if value in (0, 1):
            return False
        i = 2
        while i * i <= value:
            if value % i == 0:
                return False
            i += 1
        return True

    def _next_prime(self, value):
        while not self._check_prime(value):
            value += 1
        return value
