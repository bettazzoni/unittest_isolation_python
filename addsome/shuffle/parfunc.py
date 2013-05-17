
def cy(generator):
    return lambda x: x + generator

def cs(generator):
    return lambda x: (0x5A5A5A5A * hash(x) * generator) % 1000000 

if __name__ == '__main__':
    pass