import math
import collections
import encryption.blowfish as bf
import encryption.aes as aes
#Shannon's Entropy Formula:
#H(x) = -Σni = 1 [P(xi) * logbP(xi)] = Σni = 1 [P(xi) * logb(1 / P(xi))]
def entropyTest(msg):
    m = len(msg)
    #bases in comprised of the number of occurances of each character in msg
    bases = collections.Counter([i for i in msg])

    entropyValue = 0

    for base in bases:
        n = bases[base]

        p = n / float(m)

        entropy = p * (math.log(p,2))
        entropyValue += entropy

    return entropyValue * -1

