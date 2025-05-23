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