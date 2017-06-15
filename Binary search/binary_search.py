class BinarySearch(list):
    def __init__(self, a, b):
        for num in range(b, (a * b) + b, b):
            self.append(num)
        self.length = len(self)

    def search(self, number):
        count = 0
        index = -1
        data = {}
        first = 0
        last = self.length - 1
        found = False
        while first <= last and not found:
            middle = (first + last) // 2
            count += 1
            if self[middle] == number:
                index = middle
                found = True
            else:
                if number <= self[middle]:
                    last = middle - 1
                else:
                    first = middle + 1

        data["count"] = count
        data["index"] = index
        return data
