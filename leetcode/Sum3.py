class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        numlist = []
        for x in range(length-2):
            for y in range(x+1,length-1):
                for z in range(x+2,length):
                    if(nums[x]+nums[y]+nums[z] == 0):
                        numlist.append([nums[x],nums[y],nums[z]])
        return numlist
if __name__ == '__main__':
    s = Solution()
    print s.threeSum([-1, 0, 1, 2, -1, -4])