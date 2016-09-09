

class Key(object):
    def __init__(self, data):
        if data is not None:
            self.array = []
            for i in range(0, len(data), 2):
                addition = data[i:i+2]
                self.array.append(int(addition, 16))

    def get(self, x, y):
        return self.array[x*4+y]