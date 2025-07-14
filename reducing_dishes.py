class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        memo = {}

        def find_optimal_solution(index, tempo):
            if index == n:
                return 0
            if (index, tempo) in memo:
                return memo[(index, tempo)]

            cozinha_prato = satisfaction[index] * tempo + find_optimal_solution(index + 1, tempo + 1)
            descarta_prato = find_optimal_solution(index + 1, tempo)

            memo[(index, tempo)] = max(cozinha_prato, descarta_prato)
            return memo[(index, tempo)]

        return find_optimal_solution(0, 1)
