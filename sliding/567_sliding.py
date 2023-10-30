class Solution:
    def checkInclusion(self, s1: str, s2: str):
        #* Example: s1 = "abo", s2 = "eidbaooo"
        """
        -- Scan from left to right
        -- If the char in s1, match the following chars of length len(s1)
        -- Turn both to sets => match char by char
        """
        from collections import Counter
        length = len(s1)
        counter1 = Counter(s1)
        i = 0
        #* Time and space: O(26 x n) == Q(1)
        while i < len(s2):
            if s2[i] in s1:
                ss = s2[i: i+length]
                #* Time and space: O(26) == Q(1)
                counter2 = Counter(ss)
                if counter1 == counter2:
                    return True
            i += 1
        return False
