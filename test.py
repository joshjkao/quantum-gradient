import numpy as np
from quantumreg import QuantumRegister as qr

a = qr(bits = [0,0,1])

print(a.measure())