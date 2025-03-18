class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n, ans, B, l=len(nums), 0, 0, 0
        for r, x in enumerate(nums):
            while l<r and (B& x)!=0:
                B^=nums[l]
                l+=1
            B|=x
            ans=max(ans, r-l+1)
        return ans
        