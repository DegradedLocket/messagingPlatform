import math
import collections
#Shannon's Entropy Formula:
#H(x) = -Σni = 1 [P(xi) * logbP(xi)] = Σni = 1 [P(xi) * logb(1 / P(xi))]
msg = "blah blah blah"

m = len(msg)
#bases in comprised of the number of occurances of each character in msg
bases = collections.Counter([i for i in msg])

entropyValue = 0

for base in bases:
    n = bases[base]

    p = n / float(m)

    entropy = p * (math.log(p,2))
    entropyValue += entropy

def estimate_shannon_entropy(dna_sequence):
    m = len(dna_sequence)
    bases = collections.Counter([tmp_base for tmp_base in dna_sequence])

    shannon_entropy_value = 0
    for base in bases:
        # number of residues
        n_i = bases[base]
        # n_i (# residues type i) / M (# residues in column)
        p_i = n_i / float(m)
        entropy_i = p_i * (math.log(p_i, 2))
        shannon_entropy_value += entropy_i

    return shannon_entropy_value * -1
