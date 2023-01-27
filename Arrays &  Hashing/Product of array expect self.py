class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix =[]
        suffix = []
        tot = 1
        tot2 = 1
        for i in range(len(nums)):
            tot *= nums[i]
            tot2 *= nums[len(nums)-1-i]
            prefix.append(tot)
            suffix.append(tot2)
        nums[0] = suffix[len(nums)-2]
        nums[len(nums)-1] = prefix[len(nums)-2]
        for i in range(1,len(nums)-1) :
            nums[i] = prefix[i-1] * suffix[len(nums)-2-i]
        return nums
