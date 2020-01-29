from flipping_bits import flippingBits

def __test_flip(lhs: int, rhs: int):
    assert flippingBits(lhs) == rhs
    assert flippingBits(rhs) == lhs

def test_sample_input_0():
    __test_flip(2147483647, 2147483648) 
    __test_flip(1, 4294967294) 
    __test_flip(0, 4294967295)

def test_sample_input_1():
    __test_flip(4, 4294967291) 
    __test_flip(123456, 4294843839) 

def test_sample_input_2():
    __test_flip(0, 4294967295)
    __test_flip(802743475, 3492223820) 
    __test_flip(35601423, 4259365872) 





