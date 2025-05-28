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

    def myAtoi(self, s: str) -> int:
        num,i = 0,0
        s = s.strip()
        if len(s) == 0:
            return 0
        if len(s) > 200:
            s = s[:200]
        neg = False
        if s[0] == "-": 
           neg = True
           s = s[1:]
        elif s[0] == "+":
            s = s[1:]
        else:
            pass
        while i<len(s) and (ord(s[i]) in range(48,58)):
               num*=10
               num += int((s[i]))
               i +=1

        if neg:
            num *= -1 
        if num>(2**31)-1:
           return 2**31 - 1
        elif num<(-2**31):     
            return -2**31
        else:
            return num
        
    def removeDuplicates(self, nums: list[int]) -> int:                
        j = 0
        for i in range(len(nums)):           
            if nums[i] != nums[j]:
                j+=1
                nums[j]=nums[i]
        return j+1