class Solution:
    def isPalindrome(self, s: str) -> bool:
        myArr = [char.lower() for char in s if char.isalnum()]

        for i in range(len(myArr)//2):
            if myArr[i] != myArr[len(myArr)-i-1]:
                return False
        return True