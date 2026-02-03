A = [
    [4, 5, 10, 20,],
    [5, 3, 30, 21,],
    [1, 1, 1,  1, ], 
]

def get_length_longest_increasing_path(m):
    rows = len(m)
    cols = len(m[0])
    
    cache = {}
    dirs = [(i, j) for i in [-1, 1] for j in [-1, 1]]
    
    def check_boundary(pos):
        
    def dfs(pos):
        if pos in cache:
            return cache[pos]
        #* Base case
        if pos[0] < 0 or pos[0] >= rows or pos[1] < 0 or pos[1] >= cols:
             return 0
        
        
        i, j = pos
        longest = -1
        for d in dirs:
            new_pos = i + d[0], j + d[1]
            dist = dfs(new_pos) + 1
            longest = max(longest, dist)
        
        cache[pos] = longest
    
    dfs((0,0), 0)
    return max(cache.values())
    # returns the length of the longest increasing path within matrix m
    # at any position, you can move towards all 8 directions: up-left, up, ..., left
    
print(get_length_longest_increasing_path(A))  # 8