class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def reverse(s:str):
            if len(s)==1 or len(s)==0:
                return True
            p1,p2 = 0,-1
            while p1<len(s):
                if s[p1] == s[p2]:
                    p1+=1
                    p2-=1
                else:
                    return False
            return True
        
        res = []
        def dp(s:str,temp:list):
            #终止条件
            if not s:
                res.append(temp)
            p=1
            while p<=len(s):
                #判断第一子串是否回文
                is_reverse = reverse(s[:p])
                if is_reverse:
                    #加入
                    dp(s[p:],temp+[s[:p]])
                p+=1
        
        dp(s,[])
        return res
