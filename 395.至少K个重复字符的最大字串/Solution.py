import sys
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def dp(s:list):
            maxlen = sys.maxsize * -1
            ##找出当前字符串分割的字符
            key_nums = dict()
            for i in s:
                if i in key_nums.keys():
                    key_nums[i] = key_nums[i] + 1
                else:
                    key_nums[i] = 1
            isolation = []
            for key,val in key_nums.items():
                if val < k:
                    isolation.append(key)
                    
            #终止条件:当前字串没有分割字符
            if len(isolation) ==0:
                return len(s)
            #终止条件:当前字串全是分割字符
            if sorted(set(isolation)) == sorted(set(s)):
                return 0
            
            #找出子串递归
            p1,p2 = 0,0
            while p2<len(s):
                if s[p2] not in isolation:
                    p2+=1
                else:
                    maxlen = max(dp(s[p1:p2]),maxlen)
                    p1=p2+1
                    p2+=2
            maxlen = max(dp(s[p1:]),maxlen)
            return maxlen
        maxlen = dp(list(s))
        return maxlen
