from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n1 = len(s)
        n2 = len(p)

        @lru_cache(None)
        def memoriza(i, j):

            if i < 0 and j < 0:
                return True
            if j < 0 and i >= 0:
                return False
            if i < 0 and j >= 0:
                for k in range(j + 1):
                    if p[k] != '*':
                        return False
                return True

            if s[i] == p[j] or p[j] == '?':
                return memoriza(i - 1, j - 1)

            if p[j] == '*':
                return memoriza(i - 1, j) or solve(i, j - 1)

            return False

        return memoriza(n1 - 1, n2 - 1)
