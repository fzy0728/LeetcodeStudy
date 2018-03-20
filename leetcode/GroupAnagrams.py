#coding:utf-8
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # 排序后的值放入哈希表
        dics = {}
        for i in xrange(len(strs)):
            sortstrs = ''.join(sorted(strs[i]))
            if dics.has_key(sortstrs):
                dics[sortstrs].append(strs[i])
            else:
                dics[sortstrs] = []
                dics[sortstrs].append(strs[i])
        return dics.values()

if __name__ == '__main__':
    s = Solution()
    s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])