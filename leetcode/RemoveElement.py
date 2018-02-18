class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for i in nums:
            if(i != val):
                nums[count] = i
                count+=1
        return count

if __name__ == '__main__':
    s = Solution()
    print s.removeElement([3,2,2,3],3)
