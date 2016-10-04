from Crypto.Util import number


def modExp(value, exponent, mod):
    exponent = int(exponent)
    if (exponent == 0):
        return 1
    z = modExp(value, exponent / 2, mod)
    if (exponent % 2 == 0):
        result = ((z * z) % mod)
        return result
    else:
        result = ((value % mod) * ((z * z) % mod) % mod)
        return result

class Main:
    def run(self):
        g = 5
        p = number.getStrongPrime(512)
        s = number.getRandomInteger(512)
        public = modExp(g, s, p)
        print "p= " + str(p)
        print "s= " + str(s)
        print "public= " + str(public)
        gtp = int(raw_input("g^t mod p: "))
        key = modExp(gtp, s, p)
        print "key= " + str(key)

if __name__ == "__main__":
    m = Main()
    m.run()