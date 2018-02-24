class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        num1_list = [ord(i)-ord('0') for i in list(num1)]
        num2_list = [ord(i)-ord('0') for i in list(num2)]
        num = [0 for i in range(200)]
        for i in xrange(len(num2_list),0,-1):
            for j in xrange(len(num1_list)):
                # print num1_list[j],num2_list[i-1]
                temp = (num2_list[i-1]*num1_list[j])/10
                if temp!=0:
                    if j == 0:
                        num[len(num2_list)-i+len(num1_list)-j] = temp
                    else:
                        num[len(num2_list)-i+len(num1_list)-j] += temp
                num[len(num2_list)-i+len(num1_list)-j-1] += ((num2_list[i-1]*num1_list[j])%10)
        for i in range(len(num1_list)+len(num2_list)):
            if num[i]>=10:
                temp = num[i]/10
                num[i]%=10
                num[i+1] += temp

        return ''.join(str(i) for i in num).rstrip('0')[::-1]

if __name__ == '__main__':
    s = Solution()
    print s.multiply("5234","456")
    print s.multiply("1000000","10000000")
    print s.multiply("1000000","0")
