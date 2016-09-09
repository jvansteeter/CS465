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
    key = "8e73b0f7da0e6452c810f32b809079e562f8ead2522c6b7b"
    try:
        m.run(data, key)
    except KeyboardInterrupt:
        pass
