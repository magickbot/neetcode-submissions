class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        seen = defaultdict(list)
        for i in range(len(nums)):
            nums_copy = nums.copy()
            nums_copy.pop(i)
            seen[i] = nums_copy
        for x in range(len(nums)):
            product = 1
            for y in seen[x]:
                product *= y
            res.append(product)
        return res