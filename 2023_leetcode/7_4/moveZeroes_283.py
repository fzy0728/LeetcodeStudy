class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        temp = length = 0
        n = len(nums)
        for index, i in enumerate(nums):
            if i == 0:
                if nums[temp] != 0:
                    temp = index
                length += 1
            if i != 0 and nums[temp] == 0:
                nums[index], nums[temp] = nums[temp], nums[index]
                temp += 1
        return nums



res = [0, 1, 1, 2, 0, 1,2,0]
s = Solution()
s.moveZeroes(res)
print(res)


            