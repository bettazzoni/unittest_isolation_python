import itertools


same_key = echo_key = lambda x: str(x)
id_based_key = lambda x: id(x)
hash_based_key = lambda x: hash(x)
numeric_hash_based_key = lambda x, num: hash(x) + hash(num)

def create_numeric_hash_based_key(generator):
    return lambda x: (0x5A5A5A * hash(x) * generator) % 100000

def shuffle(inputlist, key_function):
    return sorted(inputlist, key=key_function)

Permutation = itertools.permutations

if __name__ == '__main__':
    p= Permutation("AB")
    print(next(p))
    print(next(p))
    print(next(p))
    
    

    
    
    
    
    