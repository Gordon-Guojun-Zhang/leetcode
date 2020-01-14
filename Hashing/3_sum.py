class Solution:  
    def pre_pros(self, nums: List[int]):     # remove duplicates if some elements appears more than 3 times
        cout = {}
        new_nums = []
        for a in nums:
            if a not in cout:
                cout[a] = 1
            else:
                cout[a] += 1
            if cout[a] <= 3:
                new_nums.append(a)
        return new_nums
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = self.pre_pros(nums)
        triplet = set()
        dic = {}
        for i in range(len(nums)):   # hash table
            dic[nums[i]] = i
        for i in range(len(nums)):
            for k in range(i):
                t = -nums[i] - nums[k]
                if t in dic and dic[t] != i and dic[t] != k:
                    a = [nums[k] , nums[i], t]
                    a.sort()
                    triplet.add(tuple(a))
        return list(triplet)
