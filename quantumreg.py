from __future__ import annotations
import numpy as np

class QuantumRegister:

    # Constructors
    def __init__(self, q: int):
        self.n = 1
        self.bits = np.array([[0],[0]])
        if q == 0:
            self.bits = np.array([[1],[0]])
        elif q == 1:
            self.bits = np.array([[0],[1]]) 
        else:
            raise Exception("Bits can only be initialized as 0 or 1")    
        
    # def __init__(self, bits: np.array):
    
    
    
    # Visualization
    def __getitem__(self, key):
        return self.bits[key]
    
    def __str__(self):
        return np.array2string(self.bits)
    
    
    # Operations
    def tensor(self, b: QuantumRegister):
        self.n += b.n
        self.bits = np.kron(self.bits, b.bits)
    
    # Static methods
    @staticmethod
    def one() -> QuantumRegister:
        return QuantumRegister(1)
    
    @staticmethod
    def zero() -> QuantumRegister:
        return QuantumRegister(0)
