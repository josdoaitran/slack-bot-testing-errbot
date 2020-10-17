import random
import string


class RamdomUtil:

    def randN(N):
        min = pow(10, N-1)
        max = pow(10, N) - 1
        return random.randint(min, max)

    def randomStr(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))
