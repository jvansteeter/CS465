

class Main:

    def run(self, data, key):
        self.cipher(data, key)

    def cipher(self, block, key):
        binaryString = format(block, '08b')
        print binaryString


if __name__ == "__main__":
    m = Main()
    data = 19
    key = ""
    try:
        m.run(data, key)
    except KeyboardInterrupt:
        pass
