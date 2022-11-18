class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = [
            ('I', 1),
            ('V', 5),
            ('X', 10),
            ('L', 50),
            ('C', 100),
            ('D', 500),
            ('M', 1000),
            ('IV', 4),
            ('IX', 9),
            ('XL', 40),
            ('XC', 90),
            ('CD', 400),
            ('CM', 900),
        ]
        symbols.sort(key=lambda x: x[1], reverse=True)
        
        result = ''
        for char, val in symbols:
            count = num // val
            if count:
                result += char*count
                num %= val
            
        return result