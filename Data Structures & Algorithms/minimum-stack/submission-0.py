class MinStack:
    def __init__(self):
        self._list = list()
        self._mins = [float("inf")]
    def push(self, val: int) -> None:
        if val <= self._mins[-1]:
            self._mins.append(val)
        self._list.append(val)
    def pop(self) -> None:
        if self._mins[-1] == self._list.pop():
            self._mins.pop()
    def top(self) -> int:
            return self._list[-1]
    def getMin(self) -> int:
        return self._mins[-1]
