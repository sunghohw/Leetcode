class Solution(object):
    def __init__(self,s):
        print self.lengthOfLongestSubstring(s)

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        maxlen = start = 0
        for i,v in enumerate(s):
            if v in dict:
                sum = dict[v] + 1
                if sum > start:
                    start = sum
            len = i - start + 1
            maxlen = max(len,maxlen)
            dict[v] = i
        return maxlen

Solution("bvbb")
Solution("abcabcbb")
Solution("bbbbb")
Solution("pwwkew")