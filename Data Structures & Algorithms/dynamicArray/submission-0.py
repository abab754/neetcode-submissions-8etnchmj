class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [0] * capacity
        self.size = capacity
        self.length = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.size:
            self.resize()
        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        if self.length == 0:
            return
        self.length -= 1
        return self.arr[self.length]

    def resize(self) -> None:
        newArr = [0] * (self.size * 2)
        for i in range(self.length):
            newArr[i] = self.arr[i]
        self.arr = newArr
        self.size = self.size * 2

    def getSize(self) -> int:
        return self.length
        
    def getCapacity(self) -> int:
        return self.size
