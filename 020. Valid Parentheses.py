'''

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


'''

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
                
