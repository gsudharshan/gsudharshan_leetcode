class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_dict = {}
        n = len(nums)
        for i in range(n):
            num = nums[i]
            complement = target - num
            if complement in new_dict:
                return [new_dict[complement], i]
            else:
                new_dict[num] = i