"""
Problem: Two Sum (Novice Edition)
Description:
Given an array of integers nums and an integer target, 
return the indices of the two numbers that add up to the target.

Constraints:
You may assume that each input has exactly one solution.
You may not use the same element twice.

Input: nums = [2, 7, 11, 15], target = 9  
Output: [0, 1]  
Explanation: nums[0] + nums[1] = 2 + 7 = 9  


Hints:

Iterate through the array with two loops to check all possible pairs of indices.
Consider optimizing by using a dictionary to store previously seen values.

"""

nums = [2,8,11,15,7]
target = 9


def two_sum(nums:list[int], target:int)->list[int]:
    pointer = 0
    while True:
        n = nums[pointer]
        for num in nums:
            if n + num == target:
                return print('target found ' , n , num)
        
        pointer+=1
        
        
two_sum(nums , target)