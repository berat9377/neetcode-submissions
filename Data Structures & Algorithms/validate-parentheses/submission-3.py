class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis_map = {"]":"[", "}":"{", ")":"("}
        outList = []

        for char in s:
            if char in parenthesis_map:
                top_element = outList.pop() if outList else "_"

                if parenthesis_map[char] != top_element:
                    return False
            else:
                outList.append(char)
                
        return not outList