class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}
        for k,v in enumerate(nums):
            if v in sum_dict:
                return sum_dict[v],k
            sum_dict[target-v]=k
            