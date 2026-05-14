class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if target % 2 == 0:
            mid = target//2
            if numbers.count(mid) >=2:
                ind = numbers.index(mid)
                return [ind+1, ind+2]
            
            
        numSet = dict.fromkeys(numbers)

        for num in numSet:
            if target - num in numSet:
                return [numbers.index(num) + 1, numbers.index(target-num) + 1]