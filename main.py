from leetcode import LeetCode

if __name__ == "__main__":
	leetobj = LeetCode()

	# Given an integer x, return true if x is a palindrome, and false otherwise
	print(leetobj.isPalindrome(121))
	print(leetobj.isPalindrome(-121))
	print(leetobj.isPalindrome(10))

	# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target
	print(leetobj.twoSum([2,7,11,15],9))
	print(leetobj.twoSum([3,2,4],6))
	print(leetobj.twoSum([3,3],6))

	# Convert a decimal place value into a Roman numeral
	print(leetobj.intToRoman(3749)=="MMMDCCXLIX")
	print(leetobj.intToRoman(58)=="LVIII")
	print(leetobj.intToRoman(1994)=="MCMXCIV")

	# converts a string to a 32-bit signed integer
	print(leetobj.myAtoi("42"))
	print(leetobj.myAtoi("   -42"))
	print(leetobj.myAtoi("4193 with words"))
	print(leetobj.myAtoi("words and 987"))
	print(leetobj.myAtoi("-91283472332"))
	print(leetobj.myAtoi("2147483648"))	


	# remove the duplicates in-place such that each element appears only once and returns the new length
	print(leetobj.removeDuplicates([1, 1, 2]))
	print(leetobj.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
	print(leetobj.removeDuplicates([1, 2, 3, 4, 5]))
	print(leetobj.removeDuplicates([]))
	print(leetobj.removeDuplicates([1, 1, 1, 1, 1]))
	print(leetobj.removeDuplicates([1, 2, 2, 3, 4, 4, 5, 5, 6]))	

	# reverse the digits of an integer
	# Note: The reverse function should handle overflow cases
	print(leetobj.reverse(123))
	print(leetobj.reverse(-123))
	print(leetobj.reverse(120))
	print(leetobj.reverse(0))
	print(leetobj.reverse(1534236469))  # This should return 0 due to overflow
	print(leetobj.reverse(1463847412))  # This should return 2147483641 due to overflow

	# restore the string by returning the original string after rearranging the characters at the indices given by the indices array
	print(leetobj.restoreString("abc", [0, 1, 2]))
	print(leetobj.restoreString("codeleet", [4,5,6,7,0,2,1,3]))
	print(leetobj.restoreString("aiohn", [3,1,4,2,0]))
	
	# find the first occurrence of a substring in a string
	print(leetobj.strStr("hello", "ll"))
	print(leetobj.strStr("aaaaa", "bba"))
	print(leetobj.strStr("", "a"))
	print(leetobj.strStr("haystack", "needle"))
	print(leetobj.strStr("mississippi", "issip"))
	print(leetobj.strStr("abcde", "cde"))
	print(leetobj.strStr("abcde", "f"))


	# find the length of the longest substring without repeating characters
	print(leetobj.lengthOfLongestSubstring("abcabcbb"))
	print(leetobj.lengthOfLongestSubstring("bbbbb"))
	print(leetobj.lengthOfLongestSubstring("pwwkew"))
	print(leetobj.lengthOfLongestSubstring(""))
	print(leetobj.lengthOfLongestSubstring("a"))
	print(leetobj.lengthOfLongestSubstring("dvdf"))
	print(leetobj.lengthOfLongestSubstring("tmmzuxt"))
	print(leetobj.lengthOfLongestSubstring("aab"))