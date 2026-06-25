class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        longest = 1
        start = 0
        sorted_n = sorted(set(nums))
        curr = 1
        for i, num in enumerate(sorted_n):
            if i == start:
                 continue
            if (num - sorted_n[i-1] == 1):
                 curr += 1
                 longest = max(longest, curr)
            if (num - sorted_n[i-1] != 1):
                 curr = 1
                 start = i
                 longest = max(longest, curr)
        return longest
