# Brute force recursion
class Solution:
    def climbStairs(self, n: int) -> int:
        # 4: 1111, 121, 211, 112, 22
        def step(size, residual, counter):
            print(f"{size=}, {residual=}, {counter=}")
            residual -= size
            
            if residual < 0:
                return counter
            elif residual == 0:
                # print("return")
                return counter + 1
            # else:
            #      counter += 1
            
            _residual = residual
            counter = step(1, _residual, counter)
            _residual = residual
            counter = step(2, _residual, counter)
            
            return counter
            
        if n == 1: return 1
        if n == 2: return 2
        
        counter = 0
        # 1. Start with step size 1
        residual = n
        counter = step(1, residual, counter)
        
        print()

        # 2. Start with step size 2
        residual = n
        counter = step(2, residual, counter)     
        
        return counter 
        
            
        
