from State import *
from key import Key
from Cipher import Cipher


class Main:

    def run(self, data, _key):
        state = State(data)
        key = Key(data)
        cipher = Cipher(state, key)
        cipher.encrypt()

if __name__ == "__main__":
    m = Main()
    data = "193de3bea0f4e22b9ac68d2ae9f84808"
    key = "2b7e151628aed2a6abf7158809cf4f3c"
    try:
        m.run(data, key)
    except KeyboardInterrupt:
        pass
