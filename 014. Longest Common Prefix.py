'''

Write a function to find the longest common prefix string amongst an array of strings


'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pre = ''
        try:
            first = strs[0]
        except:
            return pre
        for n in range(len(first)):
            letter = first[n]
            for item in strs[1:]:
                try:
                    temp = item[n]
                except IndexError:
                    return pre
                if temp != letter:
                    return pre
            pre +=letter 
        return pre
