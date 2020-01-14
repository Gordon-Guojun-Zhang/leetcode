class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_l = 0
        max_str = ""
        n = len(s)
        for i in range(n):   # ints
            # expand around
            k = j = i
            cur_l = 1
            cur_str = s[k: j + 1]
            while k >= 0 and j < len(s):
                if k == j:
                    k -= 1
                    j += 1
                    continue
                if s[k] == s[j]:
                    cur_l += 2
                else:
                    break               
                k -= 1
                j += 1
            if cur_l > max_l:
                max_l = cur_l
                max_str = '%s' % s[k + 1: j]
                
        for i in range(n):      # halves
            # expand around
            k = i - 1
            j = i
            cur_l = 0
            cur_str = ""
            if k < 0 or s[k] != s[j]:
                continue
            while k >= 0 and j < len(s):
                if s[k] == s[j]:
                    cur_l += 2
                else:
                    break                
                k -= 1
                j += 1
            if cur_l > max_l:
                max_l = cur_l
                max_str = '%s' % s[k + 1: j]
        
        return max_str
                
