'''
一次上1个或2个阶梯
对于n来说，最后一次可以上1个阶梯，也可以上两个阶梯
因此对于n来说他的种类数应该是：n-1阶阶梯的方法数+n-2阶阶梯的方法数
这就是一个斐波拉契数列
即F(n)=F(n-1)+F(n-2)
'''

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        if n==2:
            return 2
        one=1
        second=2
        for i in range(3,n+1):
            three=one+second
            one=second
            second=three
        return second