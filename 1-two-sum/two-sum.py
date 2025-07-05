class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for idx,i in enumerate(nums):
            if target - i in my_dict:
                return idx,my_dict[target-i]
                my_dict[i] += 1
            else:
                my_dict[i] = idx
        