class Solution:
    
    def trap(self, height: List[int]) -> int:
        l = len(height)
        if len(height) == 0:
            return 0
        left_max, right_max = [0]*l, [0]*l
        left_max[0] = height[0]
        right_max[l - 1] = height[l - 1]
        for i in range(1, l):
            left_max[i] = max(left_max[i - 1], height[i])
        for j in range(l - 2, -1, -1):
            right_max[j] = max(right_max[j + 1], height[j])
        total = 0
        for k in range(l):
            total += min(left_max[k], right_max[k]) - height[k]
        return total
