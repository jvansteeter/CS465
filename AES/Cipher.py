from State import State
from key import *


class Cipher(object):
    def __init__(self, state, key):
        self.state = state
        self.key = key
        self.sBox = [[0]*16 for i in range(16)]
        self.invSBox = [[0]*16 for i in range(16)]
        self.defineSBox()
        self.rcon = [
            0x01000000, 0x02000000, 0x04000000, 0x08000000,
            0x10000000, 0x20000000, 0x40000000, 0x80000000,
            0x1B000000, 0x36000000, 0x6C000000, 0xD8000000,
            0xAB000000, 0x4D000000, 0x9A000000, 0x2F000000,
            0x5E000000, 0xBC000000, 0x63000000, 0xC6000000,
            0x97000000, 0x35000000, 0x6A000000, 0xD4000000,
            0xB3000000, 0x7D000000, 0xFA000000, 0xEF000000,
            0xC5000000, 0x91000000, 0x39000000, 0x72000000,
            0xE4000000, 0xD3000000, 0xBD000000, 0x61000000,
            0xC2000000, 0x9F000000, 0x25000000, 0x4A000000,
            0x94000000, 0x33000000, 0x66000000, 0xCC000000,
            0x83000000, 0x1D000000, 0x3A000000, 0x74000000,
            0xE8000000, 0xCB000000, 0x8D000000
        ]

    def defineSBox(self):
        invStringBox = [
            ['52', '09', '6a', 'd5', '30', '36', 'a5', '38', 'bf', '40', 'a3', '9e', '81', 'f3', 'd7', 'fb'],
            ['7c', 'e3', '39', '82', '9b', '2f', 'ff', '87', '34', '8e', '43', '44', 'c4', 'de', 'e9', 'cb'],
            ['54', '7b', '94', '32', 'a6', 'c2', '23', '3d', 'ee', '4c', '95', '0b', '42', 'fa', 'c3', '4e'],
            ['08', '2e', 'a1', '66', '28', 'd9', '24', 'b2', '76', '5b', 'a2', '49', '6d', '8b', 'd1', '25'],
            ['72', 'f8', 'f6', '64', '86', '68', '98', '16', 'd4', 'a4', '5c', 'cc', '5d', '65', 'b6', '92'],
            ['6c', '70', '48', '50', 'fd', 'ed', 'b9', 'da', '5e', '15', '46', '57', 'a7', '8d', '9d', '84'],
            ['90', 'd8', 'ab', '00', '8c', 'bc', 'd3', '0a', 'f7', 'e4', '58', '05', 'b8', 'b3', '45', '06'],
            ['d0', '2c', '1e', '8f', 'ca', '3f', '0f', '02', 'c1', 'af', 'bd', '03', '01', '13', '8a', '6b'],
            ['3a', '91', '11', '41', '4f', '67', 'dc', 'ea', '97', 'f2', 'cf', 'ce', 'f0', 'b4', 'e6', '73'],
            ['96', 'ac', '74', '22', 'e7', 'ad', '35', '85', 'e2', 'f9', '37', 'e8', '1c', '75', 'df', '6e'],
            ['47', 'f1', '1a', '71', '1d', '29', 'c5', '89', '6f', 'b7', '62', '0e', 'aa', '18', 'be', '1b'],
            ['fc', '56', '3e', '4b', 'c6', 'd2', '79', '20', '9a', 'db', 'c0', 'fe', '78', 'cd', '5a', 'f4'],
            ['1f', 'dd', 'a8', '33', '88', '07', 'c7', '31', 'b1', '12', '10', '59', '27', '80', 'ec', '5f'],
            ['60', '51', '7f', 'a9', '19', 'b5', '4a', '0d', '2d', 'e5', '7a', '9f', '93', 'c9', '9c', 'ef'],
            ['a0', 'e0', '3b', '4d', 'ae', '2a', 'f5', 'b0', 'c8', 'eb', 'bb', '3c', '83', '53', '99', '61'],
            ['17', '2b', '04', '7e', 'ba', '77', 'd6', '26', 'e1', '69', '14', '63', '55', '21', '0c', '7d']
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

        for i in range(0, len(stringBox)):
            for j in range(0, len(stringBox[i])):
                self.sBox[i][j] = int(stringBox[i][j], 16)
                self.invSBox[i][j] = int(invStringBox[i][j], 16)

    def encrypt(self):
        print "key schedule"
        self.keySchedule()
        print "start"
        self.printState()
        self.subBytes()
        print "sub bytes"
        self.printState()
        self.shiftRows()
        print "shift rows"
        self.printState()
        self.mixColumns()
        print "mix columns"
        self.printState()
        return self.state

    def subBytes(self):
        i = 0
        for element in self.state.array:
            hex = format(element, '02x')
            x = int(hex[0], 16)
            y = int(hex[1], 16)
            self.state.array[i] = self.sBox[x][y]
            i += 1

    def shiftRows(self):
        newOrder = [0, 5, 10, 15, 4, 9, 14, 3, 8, 13, 2, 7, 12, 1, 6, 11]
        self.state.array = [self.state.array[i] for i in newOrder]

    def mixColumns(self):
        for i in range(0, 4):
            one = self.tt_multiply(self.state.get(i, 0), 2) ^ self.tt_multiply(self.state.get(i, 1), 3) ^ self.state.get(i, 2) ^ self.state.get(i, 3)
            two = self.state.get(i, 0) ^ self.tt_multiply(self.state.get(i, 1), 2) ^ self.tt_multiply(self.state.get(i, 2), 3) ^ self.state.get(i, 3)
            three = self.state.get(i, 0) ^ self.state.get(i, 1) ^ self.tt_multiply(self.state.get(i, 2), 2) ^ self.tt_multiply(self.state.get(i, 3), 3)
            four = self.tt_multiply(self.state.get(i, 0), 3) ^ self.state.get(i, 1) ^ self.state.get(i, 2) ^ self.tt_multiply(self.state.get(i, 3), 2)
            self.state.set(i, 0, one)
            self.state.set(i, 1, two)
            self.state.set(i, 2, three)
            self.state.set(i, 3, four)

    def xtime(self, number):
        number <<= 1
        if format(number, '09b')[0] is "1":
            number ^= 0x011b
        return number

    def tt_multiply(self, first, second):
        print "multiply"
        multiples = []
        multiples.append(first)
        print str(0) + " " + str(multiples[0]) + " " + format(multiples[0], '08b')

        for i in range(1, 8):
            multiples.append(self.xtime(multiples[i - 1]))
            print str(i) + " " + str(multiples[i]) + " " + format(multiples[i], '08b')

        print "first= " + str(first) + " " + format(first, '08b')
        print "second= " + str(second) + " " + format(second, '08b')
        secondBinary = format(second, '08b')
        reverseSecondBinary = secondBinary[::-1]
        total = 0
        for i in range(0, len(secondBinary)):
            if reverseSecondBinary[i] is '1':
                print "adding " + str(i)
                total ^= multiples[i]
        print "total " + format(total, '08b')
        return total

    def keySchedule(self):
        pass

    def printState(self):
        for i in range(0, 4):
            print format(self.state.array[i*4], '02x') + " " + format(self.state.array[i*4+1], '02x') + " " + format(self.state.array[i*4+2], '02x') + " " + format(self.state.array[i*4+3], '02x')
