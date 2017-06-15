import math
class BinarySearch(list):
    """This class inherits from python's list class"""
    def __init__(self, a, b):
        
        super(BinarySearch, self).__init__()

        for number in range(1, a + 1):
            self.append(number * b)

        self.length = len(self)

    def search(self, value):
        
        count = 0             #for counting the number of iterations
        first  = 0            #Denotes the starting point
        last = len(self) - 1  #Denotes the ending point
        index = 0             #Index of the elements

        if value == self[first]:
            index = first
            return {'count': count, 'index': index}

        elif value == self[last]:
            index = last
            return {'count': count, 'index': index}
        elif value not in self:
            index = -1
            return {'count': count, 'index': index}

        while first <= last:
        #Binary search
            mid = math.floor((first + last) / 2)

            if self[mid] == value:
                index = mid
                return {'count': count, 'index': index}
            else:
                count += 1
                if value < self[mid]:
                    last = mid - 1
                else:
                    first = mid + 1

        return {'count': count, 'index': index}