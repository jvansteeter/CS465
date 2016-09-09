

class Key(object):
    def __init__(self, data):
        self.array = []
        for i in range(0, len(data), 2):
            addition = int(data[i:i+2], 16)
            self.array.append(addition)

    def get(self, x, y):
        return self.array[x*4+y]