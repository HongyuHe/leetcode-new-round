class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {0: 1, 1: 1, 2: 2, 3: 3}  # residual -> steps
        # 4: 1111, 121, 211, 112, 22
        
        def step(size, residual, counter):
            # print(f"{size=}, {residual=}, {counter=}")
            residual -= size
            
            if residual < 0:
                return 0
            
            if residual in cache:
                return cache[residual]
            
            _residual = residual
            counter += step(1, _residual, counter)
            
            _residual = residual
            counter += step(2, _residual, counter)
            
            cache[residual] = counter
            
            return counter
        
        counter = 0
        # 1. Start with step size 1
        residual = n
        counter += step(1, residual, counter)
        
        # print()

        # 2. Start with step size 2
        residual = n
        counter += step(2, residual, counter)     
        
        return counter 
        
            
        