class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        result = 0
        charset = set()
        for i in range(len(s)):
            while s[i] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[i])
            result = max(result, i-l+1)
        return result

            