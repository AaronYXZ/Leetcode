'''

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
'''

class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        v = 'aeiouAEIOU'
        vs = ""
        index = []
        for i, letter in enumerate(s):
            if letter in v:
                vs = vs+letter
                index.append(i)

        vs = vs[::-1]
        result = ""
        pos = 0        
        for j in s:
            if j in v:
                result = result+vs[pos]
                pos+=1
            else:
                result = result+j
                
        return result