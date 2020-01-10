class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            dicti = {}
            for i, num in enumerate(nums):
                dicti[num] = i
            for i, num in enumerate(nums):
                compl = target - num
                if (compl in dicti and dicti[compl] != i):
                    return [i, dicti[compl]]
