'''
9用栈实现两个队列,主要的是初始化部分。
'''
class Solution:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        # return xx
        if self.stack2:
            return self.stack2.pop()
        elif self.stack1:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        