class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mp = {')': '(', ']': '[', '}': '{'}
        
        for x in s:
            if x in mp.values():
                stack.append(x)
            elif not stack or stack.pop() != mp[x]:
                return False
            
        return not stack
                