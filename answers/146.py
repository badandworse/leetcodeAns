class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap=capacity
        self.valueDict=collections.OrderedDict()
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.valueDict:
            value=self.valueDict.pop(key)
            self.valueDict[key]=value
            return value
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.valueDict:
            self.valueDict.pop(key)
        elif len(self.valueDict)==self.cap:
            self.valueDict.popitem(last=False)
        self.valueDict[key]=value

            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)