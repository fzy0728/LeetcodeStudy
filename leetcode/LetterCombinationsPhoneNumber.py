class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digitstochar = {"2":["a","b","c"],"3":["d","e","f"],
                        "4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],
                        "7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}

        length = len(digits)
        if(length == 1):
            return digitstochar[digits]
        if(length ==0 ):
            return []
        res = digitstochar[digits[0]]
        for i in range(length-1):
            temp = []
            for x in range(len(res)):
                for y in range(len(digitstochar[digits[i+1]])):
                    temp.append(res[x]+digitstochar[digits[i+1]][y])
            res = temp
        return res


if __name__ == "__main__":
    s = Solution()
    print s.letterCombinations("234")
    print s.letterCombinations("")