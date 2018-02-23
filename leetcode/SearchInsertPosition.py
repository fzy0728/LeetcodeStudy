class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        position = 0
        if len(nums)==0:return 0
        for i in range(len(nums)):
            if nums[i]<target :
                position = i+1
            else:
                break
        return position
if __name__ == '__main__':
    s = Solution()
    print s.searchInsert([1,3,5,6], 5)
    print s.searchInsert([1,3,5,6], 2)
    print s.searchInsert([1,3,5,6], 7)
    print s.searchInsert([1,3,5,6], 0)