class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(nums)
        res = []
        start = 0
        if not nums:
             return res
        if len(nums) == 1:
             return nums
        for i in range(1, len(nums)):
            print(f"index: {i}")
            if nums[i] != nums[i-1]:
                res.append(nums[start:i])
                start = i
            if i == len(nums)-1:
                 res.append(nums[start:i+1])
        res = sorted(res, key=len, reverse=True)
        return [x[0] for x in res][:k]