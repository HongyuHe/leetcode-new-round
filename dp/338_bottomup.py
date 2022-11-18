class Solution:
    def countBits(self, n: int) -> List[int]:
        # 0 -->   0
        # 1 -->  01
        # 2 -->  10
        # 3 -->  11
        # 4 --> 100
        # 5 --> 101
        # 6     110
        # 7     111
        # 8    1000
        # 9    1001
        # 10   1010 = cache[prev_power2] + cache[10-prev_power2]
        ans = [0]*(n+1)
        nxt_power = 1
        for i in range(1, n+1):
            if i == nxt_power:
                nxt_power = i*2
                ans[i] = 1
            
            ans[i] = ans[nxt_power//2] + ans[i - nxt_power//2]
        return ans
        
        
        
        