class Solution:
    def isValid(self, s: str) -> bool:
        outList = []
        for char in s:
            match char:
                case "{" | "[" | "(":
                    outList.append(char)
                case "}":
                    if outList:
                        if not outList.pop() == "{":
                            return False
                    else:
                        return False
                case "]":
                    if outList:
                        if not outList.pop() == "[":
                            return False
                    else:
                        return False
                case ")":
                    if outList:
                        if not outList.pop() == "(":
                            return False
                    else:
                        return False
                case _:
                    return False

        if not outList:
            return True
        else:
            return False