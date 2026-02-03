class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        if not nums:
            return []

        xor = nums[0]
        for num in nums[1:]:
            xor ^= num
        
        mask = (1 << maximumBit) - 1
        answers = []
        for num in reversed(nums):
            #* Anything XOR-ed with 1's is inverted
            #* k is just the inverted last maximumBits
            k = xor ^ mask 
            answers.append(k)
            #* Cancel out the last number `num` by XOR-ing with itself
            xor ^= num
        return answers
