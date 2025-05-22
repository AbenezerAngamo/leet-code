"""
leetcode.py 
"""

class LeetCode:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        i,j=0,len(nums)-1       
        hash = {}

        for i in range(len(nums)):
            if (target-nums[i]) in hash:
                return i, hash[(target-nums[i])]
            hash[nums[i]] = i        