import numpy as np

class QuantumRegister:

    def __init__(self, n: int, bits: np.array):
        self.n = n
        self.bits = bits

    # def __init__(self, state: np.array):


    def __getitem__(self, key):
        return self.bits[key]
    
    def print(self):
        print(self.bits)
