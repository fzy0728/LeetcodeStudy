class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        target_list = set()
        candidates.sort()

        def combination(candidates, index,target, sum_list):
            if target == 0:
                target_list.add(tuple(sum_list))
            elif target > 0:
                for i in xrange(index,len(candidates)):
                    num = candidates[i]
                    if num>target:
                        return
                    if index == 0 and i > 0 and candidates[i - 1] == num:
                        continue
                    combination(candidates,i+1, target - num, sum_list + [num])
        combination(candidates,0, target, [])
        return list(target_list)

if __name__ == '__main__':
    s = Solution()

    print s.combinationSum2([2, 3, 6, 7],7)
    print s.combinationSum2([10, 1, 2, 7, 6, 1, 5],8)
    print s.combinationSum2([13,23,25,11,7,26,14,11,27,27,26,12,8,20,22,34,27,17,5,26,31,11,16,27,13,20,29,18,7,14,13,15,25,25,21,27,16,22,33,8,15,25,16,18,10,25,9,24,7,32,15,26,30,19]
,25)