class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_len = 0
        seen = {}

        for end in range(len(s)):
            if s[end] in seen:
                start = max(start, seen[s[end]]+1)
            seen[s[end]] = end
            max_len = max(max_len, end-start+1)
        return max_len