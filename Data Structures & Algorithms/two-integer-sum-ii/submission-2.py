class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        print(f"target: {target}")
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            print(f"{numbers[left]} + {numbers[right]}")
            print(f"curr_sum = {curr_sum}")
            if curr_sum > target:
                right -= 1
            if curr_sum < target:
                left += 1
            if curr_sum == target:
                return [left+1, right+1]
        return []