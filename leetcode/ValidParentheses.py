class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp = []
        for i in s:
            if(i == '('):
                temp.append('(')
            elif(i == '['):
                temp.append('[')
            elif(i == '{'):
                temp.append('{')
            elif(i == ')' and len(temp)!=0):
                if(temp[len(temp)-1]=='('):
                    temp.pop()
                else:
                    return False
            elif(i == '}' and len(temp)!=0):
                if(temp[len(temp)-1]=='{'):
                    temp.pop()
                else:
                    return False
            elif(i == ']' and len(temp)!=0):
                if(temp[len(temp)-1]=='['):
                    temp.pop()
                else:
                    return False
            else:
                return False
        if (len(temp) == 0):
            return True
        else:
            return False