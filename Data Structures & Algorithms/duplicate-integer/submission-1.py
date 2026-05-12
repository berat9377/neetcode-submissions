class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = set()

        for num in nums:
            b = len(a)
            a.add(num)
            if b == len(a):
                return True

        return False