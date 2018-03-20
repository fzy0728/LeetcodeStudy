#coding:utf-8
class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return 1.0 / self.myPow(x, -n)
        v = self.myPow(x, n / 2)
        if n % 2 == 1:
            return x * v * v
        else:
            return v * v

