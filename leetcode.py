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
        # Implementation 1
        
        # x_str = str(x)       
        # if x_str == x_str[::-1]:
        #     return True
        # else:
        #     return False
    
        # Implementation 2
        if x < 0:
               return False

        reverse = 0
        x_original = x

        while x > 0:
            reverse = (reverse * 10) + (x % 10)
            x //= 10
        
        return reverse == x_original
    
    def intToRoman(self, num: int) -> str:
        
        one = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
        ten = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        hundred = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        thousand = ["","M","MM","MMM"]       
        return thousand[(num//1000)] + hundred[((num%1000)//100)] + ten[((num%100)//10)] + one[(num%10)]