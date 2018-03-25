class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if not people:
            return []
        people.sort(key=lambda x:(x[0],-x[1]),reverse=True)
        results=[]
        for j in people:
            results.insert(j[1],j)
        return results