from State import *
from key import Key
from Cipher import Cipher


class Main:

    def run(self, data, _key):
        state = State(data)
        key = Key(_key)
        cipher = Cipher(state, key)
        cipher.encrypt()
        cipher.decrypt()

if __name__ == "__main__":
    m = Main()
    # data = "193de3bea0f4e22b9ac68d2ae9f84808"
    # data = "3243f6a8885a308d313198a2e0370734"
    # key = "2b7e151628aed2a6abf7158809cf4f3c"
    data = "00112233445566778899aabbccddeeff"
    # key = "000102030405060708090a0b0c0d0e0f"
    # key = "000102030405060708090a0b0c0d0e0f1011121314151617"
    key = "000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f"
    # key = "603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4"
    try:
        m.run(data, key)
    except KeyboardInterrupt:
        pass
