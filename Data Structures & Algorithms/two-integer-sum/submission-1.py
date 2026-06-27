class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # store the integer and it's index as the k,v

        for i, num in enumerate(nums):

            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []