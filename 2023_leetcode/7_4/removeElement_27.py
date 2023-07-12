class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        if end < 0:
            return 0
        
        while start < end:
            if nums[start] == val:
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1
                continue
            start += 1
        return start + 1 if nums[start] != val else start
    
res = [4, 5]
val = 5
s = Solution()
print(s.removeElement(res, val))
print(res)
