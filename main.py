"""
CMPS 2200  Recitation 3.
See recitation-03.pdf for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

def quadratic_multiply(x, y):

    xvec = x.binary_vec
    yvec = y.binary_vec

    print(xvec, yvec)

    if x.decimal_val <= 1 and y.decimal_val <= 1:
      return BinaryNumber(x.decimal_val * y.decimal_val)

    xvec, yvec = pad(xvec, yvec)

    n = len(xvec)
  
    xLeft, xRight = split_number(xvec)
    yLeft, yRight = split_number(yvec)

    left = quadratic_multiply(xLeft, yLeft)
  
    mid_left = quadratic_multiply(xLeft, yRight)
    mid_right = quadratic_multiply(xRight, yLeft)
    mid = BinaryNumber(mid_left.decimal_val + mid_right.decimal_val)
    mid = bit_shift(mid, len(xvec)//2) 

    left = bit_shift(left, len(xvec))
  
    right = quadratic_multiply(xRight, yRight)

    return BinaryNumber(left.decimal_val + mid.decimal_val + right.decimal_val)
    pass
    ###



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(5),         BinaryNumber(6)).decimal_val == 5*6
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)).decimal_val == 2*2
    assert quadratic_multiply(BinaryNumber(4), BinaryNumber(6)).decimal_val == 4*6
    assert quadratic_multiply(BinaryNumber(7),
BinaryNumber(5)).decimal_val == 7*5
    
def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    return (time.time() - start)*1000
    
test_multiply()
    
 

