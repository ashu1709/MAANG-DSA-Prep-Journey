Problem 27: Remove Element: 

Classic The Remove Element problem on LeetCode (Problem 27) is a classic "in-place" array manipulation challenge. The goal is to remove all occurrences of a specific value val from an integer array nums without allocating extra space for another array.


Please find the solution below: 

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0 

        for i in range (len(nums)): 
            if nums[i] != val: 
                nums[k] = nums[i]
                k += 1
        return k        
Time Complexity = O(n)
Space Complexity = O(1)
