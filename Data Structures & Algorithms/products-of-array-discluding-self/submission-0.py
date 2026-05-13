class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        multNum = 1
        zeroCount = 0
        zeroIndex: int
        for i, num in enumerate(nums):
            if num == 0:
                zeroCount += 1
                zeroIndex = i
            else:
                multNum *= num
                
        if zeroCount >= 2:
            return [0] * len(nums)

        if zeroCount == 1:
            outArr = [0] * len(nums)
            outArr[zeroIndex] = multNum
            return outArr

        outArr = [multNum] * len(nums)
        for i, num in enumerate(nums):
            outArr[i] = outArr[i] // num

        return outArr