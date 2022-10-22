class Solution:
    def longestPalindrome(self, s: str) -> str:
        #   a b a a b b  
        # a 1 1 3  [0, 3]: check [0+1, 3-1]
        # b 0 1 1 
        # a 0   1 2   
        # a 0 ... 1 1
        # b 0       1 2
        # b 0 ... ... 1
        cache = {}  # substr: palindrome
        def find_palindrome(start, end):
            # abaabba
            if start > end: return ''
            
            index = f"{start}-{end}"
            if index in cache:
                print("Cache hit: ", index)
                return cache[index]
            
            print("Cache miss: ", index)
            
            if start == end:
                cache[index] = s[start]
                return cache[index]
            
            if s[start] == s[end]:
                if start+1 == end:
                    cache[index] = s[start:end+1]
                    return cache[index]
                else:
                    palindrome = find_palindrome(start+1, end-1)
                    if len(palindrome) == end-start-1:
                        cache[index] = s[start] + palindrome + s[end]  # Flank the result.
                        return cache[index]
            chop_first = find_palindrome(start+1, end)
            chop_last = find_palindrome(start, end-1)
            palindrome = chop_first if len(chop_first) > len(chop_last) else chop_last
            cache[index] = palindrome
            return cache[index]
        
        return find_palindrome(0, len(s)-1)
            
                    
        
        
        