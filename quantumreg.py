from __future__ import annotations
import numpy as np
import copy 
import random

class QuantumRegister:

    # Constructors
    def __init__(self, **kwargs):
        bits = kwargs.get("bits", None)
        if bits != None:
            self.bits = np.array([[1]])
            self.n = 0
            for i in bits:
                if i == 0:
                    self.bits = np.kron(self.bits, np.array([[1],[0]]))
                elif i == 1:
                    self.bits = np.kron(self.bits, np.array([[0],[1]]))
                else:
                    raise Exception("bits can only be 0 or 1")
                self.n += 1
        else:
            self.n = 1
            self.bits = np.array([[1],[0]])      
    
    
    # Visualization
    def __getitem__(self, key):
        return self.bits[key]
    
    def __str__(self):
        return np.array2string(self.bits)
    
    
    # Operations
    def tensor(self, b: QuantumRegister) -> QuantumRegister:
        self.n += b.n
        self.bits = np.kron(self.bits, b.bits)
        return self

    def __mul__(self, other: QuantumRegister):
        new = copy.deepcopy(self)
        return new.tensor(other)
    
    def measure(self):
        acc = 0
        target = random.random()
        for i,d in enumerate(self.bits):
            p = d * np.conjugate(d)
            acc += p
            if target < acc:
                return i
    

    # Static methods
    @staticmethod
    def one() -> QuantumRegister:
        new = QuantumRegister()
        new.bits = np.array([[0],[1]])
        return new
    
    @staticmethod
    def zero() -> QuantumRegister:
        new = QuantumRegister()
        new.bits = np.array([[1],[0]])
        return new


class QuantumGate:
    def __init__(self, mat: np.array):
        self.mat = mat

    def __str__(self):
        return np.array2string(self.mat)
    
    def __getitem__(self, key):
        return self.mat[key]
    
    def __mul__(self, other):
        if isinstance(other, QuantumGate):
            return QuantumGate(np.kron(self.mat, other.mat))
        elif isinstance(other, QuantumRegister):
            new = QuantumRegister()
            new.bits = np.matmul(self.mat, other.bits)
            return new
        else:
            raise Exception("unsupported type")
        
    def __pow__(self, other):
        new = copy.deepcopy(self)
        for i in range(other-1):
            new = new*self
        return new