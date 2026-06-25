class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # keep a list of seen nums

        # track the index and the value
        for i, num in enumerate(nums):

            # checks if we have the complement of the number we're looking at
            # that adds up to target number
            complement = target - num
            if complement in seen:

                # return the index of the previous number, and the current number
                return [seen[complement], i]

            # store the number, and index as the key, value pair
            # this is for future checks of complement
            seen[num] = i
        
        # none found
        return []