
add = lambda a,b: (a+b)

_sum_total = 0
def summatory(x):
    _sum_total += x
    return _sum_total
 

class Adder(object):

    def __init__(self, sum_start = 0):
        self.sum = sum_start
    
    def add(self, value):
        self.sum += value
        return self.sum
    