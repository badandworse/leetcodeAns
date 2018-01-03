'''
递归的思想:
最终结果必是左括号n个，右括号n个
定义left和right表示已加入的左右括号数量
如果右括号大于左括号则是错误的，直接返回
如果left和right都为n，则说明此时生成的字符串已经有n个左括号和n个右括号，且合法
存入结果并返回
'''
class Solution(object):
    def generateParenthesis(self, N):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans


m=Solution()
print(m.generateParenthesis(3))