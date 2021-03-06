

class State(object):
    def __init__(self, data):
        self.array = []
        for i in range(0, len(data), 2):
            addition = data[i:i+2]
            self.array.append(int(addition, 16))

    def get(self, x, y):
        return self.array[x*4+y]

    def set(self, x, y, value):
        self.array[x*4+y] = value

    def state(self):
        result = ""
        for element in self.array:
            result += format(element, '02x')
        return result