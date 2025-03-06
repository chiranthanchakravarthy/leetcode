class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n: int = len(grid)
        size: int = n * n
        freq: List[int] = [0] * (size + 1)
        repeated: int = -1
        missing: int = -1

        for row in grid:
            for num in row:
                freq[num] += 1

        for num in range(1, size + 1):
            if freq[num] == 2:
                repeated = num
            if freq[num] == 0:
                missing = num

        return [repeated, missing]