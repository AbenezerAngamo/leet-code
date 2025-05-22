"""
leetcode.py 
"""

class LeetCode:
    
    def twoSum(self, nums: list[int], target: int) -> list[int]:        
        i,j=0,len(nums)-1       
        hash = {}

        for i in range(len(nums)):
            if (target-nums[i]) in hash:
                return i, hash[(target-nums[i])]
            hash[nums[i]] = i            

    def isPalindrome(self, x: int) -> bool:                
        x_str = str(x)       
        if x_str == x_str[::-1]:
            return True
        else:
            return False