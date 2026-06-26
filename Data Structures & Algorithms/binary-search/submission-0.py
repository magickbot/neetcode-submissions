class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # initialize pointers
        l, r = 0, len(nums)-1

        # while loop, l < r because at some point it goes l and r goes past each other
        while l <= r:
            # calculate mid point with floor division
            m = (l + r) // 2

            # if the midpoint is bigger than target,
            # then the target is at the left side of the array
            # move right pointer to before midpoint
            if nums[m] > target:
                r = m - 1

            # if the midpoint is smaller than the target,
            # then the target is at the right side of the array 
            # move left pointer after the midpoint
            elif nums[m] < target:
                l = m + 1

            # the l <= r condition of while loop allows us to get to this point
            # the previous conditionals "fail" (l < r) and (l > r)
            # then it must be l = r
            # this is the only way we get to this point
            # so we must have found the target
            else:
                return m
        
        # while loop is done and didn't find it
        # then it must not be in the array
        return -1
