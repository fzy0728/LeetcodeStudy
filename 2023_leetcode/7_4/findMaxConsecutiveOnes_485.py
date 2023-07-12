class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_len = temp = 0
        for i in nums:
            if i == 1:
                max_len += 1
                if max_len > temp:
                    temp = max_len
            else:
                max_len = 0
        return temp
    
res = [1,1,0,1,1,1]
s = Solution()
s = s.findMaxConsecutiveOnes(res)
print(s)

