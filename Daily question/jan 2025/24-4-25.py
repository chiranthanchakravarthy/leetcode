from collections import defaultdict

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total_distinct = len(set(nums))
        count = defaultdict(int)
        left = res = 0

        for right in range(len(nums)):
            count[nums[right]] += 1
            while len(count) == total_distinct:
                res += len(nums) - right
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1
        return res