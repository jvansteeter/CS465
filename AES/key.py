

class Key(object):
    def __init__(self, data):
        self.keys = []
        self.reverseKeys = []
        if data is not None:
            self.array = []
            for i in range(0, len(data), 2):
                addition = data[i:i+2]
                self.array.append(int(addition, 16))
        if self.size() is 128:
            self.numRounds = 10
        elif self.size() is 192:
            self.numRounds = 12
        elif self.size() is 256:
            self.numRounds = 14
        self.numWords = 4
        self.numKeyWords = self.size() / 32
        self.rcon = [
            0x01, 0x02, 0x04, 0x08,
            0x10, 0x20, 0x40, 0x80,
            0x1B, 0x36, 0x6C, 0xD8,
            0xAB, 0x4D, 0x9A, 0x2F,
            0x5E, 0xBC, 0x63, 0xC6,
            0x97, 0x35, 0x6A, 0xD4,
            0xB3, 0x7D, 0xFA, 0xEF,
            0xC5, 0x91, 0x39, 0x72,
            0xE4, 0xD3, 0xBD, 0x61,
            0xC2, 0x9F, 0x25, 0x4A,
            0x94, 0x33, 0x66, 0xCC,
            0x83, 0x1D, 0x3A, 0x74,
            0xE8, 0xCB, 0x8D
        ]
        stringBox = [
            ['63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76'],
            ['ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0', 'ad', 'd4', 'a2', 'af', '9c', 'a4', '72', 'c0'],
            ['b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc', '34', 'a5', 'e5', 'f1', '71', 'd8', '31', '15'],
            ['04', 'c7', '23', 'c3', '18', '96', '05', '9a', '07', '12', '80', 'e2', 'eb', '27', 'b2', '75'],
            ['09', '83', '2c', '1a', '1b', '6e', '5a', 'a0', '52', '3b', 'd6', 'b3', '29', 'e3', '2f', '84'],
            ['53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b', '6a', 'cb', 'be', '39', '4a', '4c', '58', 'cf'],
            ['d0', 'ef', 'aa', 'fb', '43', '4d', '33', '85', '45', 'f9', '02', '7f', '50', '3c', '9f', 'a8'],
            ['51', 'a3', '40', '8f', '92', '9d', '38', 'f5', 'bc', 'b6', 'da', '21', '10', 'ff', 'f3', 'd2'],
            ['cd', '0c', '13', 'ec', '5f', '97', '44', '17', 'c4', 'a7', '7e', '3d', '64', '5d', '19', '73'],
            ['60', '81', '4f', 'dc', '22', '2a', '90', '88', '46', 'ee', 'b8', '14', 'de', '5e', '0b', 'db'],
            ['e0', '32', '3a', '0a', '49', '06', '24', '5c', 'c2', 'd3', 'ac', '62', '91', '95', 'e4', '79'],
            ['e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9', '6c', '56', 'f4', 'ea', '65', '7a', 'ae', '08'],
            ['ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6', 'e8', 'dd', '74', '1f', '4b', 'bd', '8b', '8a'],
            ['70', '3e', 'b5', '66', '48', '03', 'f6', '0e', '61', '35', '57', 'b9', '86', 'c1', '1d', '9e'],
            ['e1', 'f8', '98', '11', '69', 'd9', '8e', '94', '9b', '1e', '87', 'e9', 'ce', '55', '28', 'df'],
            ['8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68', '41', '99', '2d', '0f', 'b0', '54', 'bb', '16']
        ]

        self.sBox = [[0] * 16 for i in range(16)]
        for i in range(0, len(stringBox)):
            for j in range(0, len(stringBox[i])):
                self.sBox[i][j] = int(stringBox[i][j], 16)
        self.keySchedule()

    def get(self, x, y):
        return self.array[x*4+y]

    def size(self):
        return len(self.array) * 8

    def keySchedule(self):
        i = 0
        self.keys = self.array[:]

        i = self.numKeyWords
        while i < (self.numWords * (self.numRounds + 1)):
            temp = self.keys[len(self.keys) - 4:len(self.keys)]
            if i % self.numKeyWords is 0:
                temp = self.rotWord(temp)
                temp = self.subColBytes(temp)
                temp[0] ^= self.rcon[i / self.numKeyWords - 1]
            elif self.numKeyWords > 6 and i % self.numKeyWords is 4:
                temp = self.subColBytes(temp)
            xorWord = self.keys[(i - self.numKeyWords) * 4:(i - self.numKeyWords) * 4 + 4]
            for j in range(0, len(temp)):
                temp[j] ^= xorWord[j]
                self.keys.append(temp[j])
            i += 1
        for j in range(0, len(self.keys), 16):
            chunk = self.keys[j:j + 16]
            for k in range(0, 16):
                self.reverseKeys.insert(k, chunk[k])

    def rotWord(self, word):
        newOrder = [1, 2, 3, 0]
        result = [word[i] for i in newOrder]
        return result

    def subColBytes(self, firstCol):
        i = 0
        for element in firstCol:
            hex = format(element, '02x')
            x = int(hex[0], 16)
            y = int(hex[1], 16)
            firstCol[i] = self.sBox[x][y]
            i += 1
        return firstCol
