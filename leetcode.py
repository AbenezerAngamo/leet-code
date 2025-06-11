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
    
    def reverse(self, x: int) -> int:
        # Implementation 1
        
        # _x = abs(x)
        # _rev = int(str(_x)[::-1])

        # if _rev > (2**31):
        #     return 0
        # if x <0:               
        #     return -_rev 
        # else:            
        #     return _rev
        
        # Implementation 2
        mul = 0
        sign = True if x<0 else False
        x = abs(x)
        while x >0:           
            if x == 1:
                mul *=10
                mul += 1    
                break
            mul *=10
            mul += x%10
            x //=10      
        if (mul > (2**31)-1) or (mul < -(2**31)):
            return 0
        if sign:
            return -1*mul
        return mul
    
    def restoreString(self, s: str, indices: list[int]) -> str:
        dictstr = {}
        
        sortedstr = ""
        j=0
        
        for i in indices:
            
            dictstr[i] = s[j]           
            j=j+1
                        
        for h in sorted(dictstr):
            
            sortedstr = sortedstr + dictstr[h]
        
        return sortedstr  

    def strStr(self, haystack: str, needle: str) -> int:
        
        j = 0
        if len(haystack) <len(needle):
            return -1
        while len(needle)<=len(haystack[j:]):
            if needle == haystack[j:(j+len(needle))]:
                return j
            j +=1
            
        return -1
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        if len(s) == 1:
            return 1

        i,j=0,0        
        _max = 0
        _dict = {}
        while j<(len(s)):
           if s[j] in _dict:
              i = max(i, _dict[s[j]] + 1)
            
           _dict[s[j]] = j  
           if _max <(j-i + 1):
                _max = j-i +1
           j +=1                        

        return _max

    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        if (n<=2) :
            return n        

        j = 2
        for i in range(2,n):
            if(nums[i] != nums[j-2]):
                nums[j] = nums[i]
                j+=1
            
        
        return j
    
    def search(self, nums: list[int], target: int) -> int:
        mid = len(nums)//2
        if target not in nums:
            return -1
        else:
            return nums.index(target)
    
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if target not in nums:
            return [-1,-1]
        else:
            inv = nums[::-1]
            return [nums.index(target), len(nums) -inv.index(target)-1]
          
        
    def removeElement(self, nums: list[int], val: int) -> int:
        if not nums:
            return 0        
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j+=1               
        return j


    def searchInsert(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid+1
        return l