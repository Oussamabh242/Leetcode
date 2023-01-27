class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        tot = 0
        for i in nums : 
            if i-1 not in s : 
                length = 0
                while i+length in s : 
                    length+=1
                
                tot = max(tot , length)
        return tot
