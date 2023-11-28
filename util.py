def binaryArray2Int(x):
    y = 0
    for i,j in enumerate(reversed(x)):
        y += j<<i
    return y

def int2BinaryArray(x, length):
    ret = [int(b) for b in bin(x)[2:]]
    while len(ret) < length:
        ret.insert(0, 0)
    return ret