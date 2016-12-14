import binascii
__b58chars = b'123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
__b58base = len(__b58chars)

b = 256
q = 2**255 - 19
l = 2**252 + 27742317777372353535851937790883648493


def bit(h, i):
    return (int(h[i//8]) >> (i%8)) & 1

def encodeint(y):
    bits = [(y >> i) & 1 for i in range(b)]
    return b''.join([bytes(sum([bits[i * 8 + j] << j for j in range(8)])) for i in range(b//8)])

def hexToInt(h):
    '''
    You might be tempted to just turn this hex into an integer using builtins
    such as `int(h, 16)`, or whatever. This wont work because it is a nonstandard
    hexToInt system.
    '''
    s = binascii.unhexlify(h) #does hex to bytes
    bb = len(h) * 4 #I guess 8 bits / b
    return sum(2**i * bit(s,i) for i in range(0,bb)) #does to int


def reverseBytes(a): #input is byte string, it reverse the endianness
    b = [a[i:i+2] for i in range(0, len(a)-1, 2)]
    return b''.join(b[::-1])

def b58encode(v):
    '''
    This is a different base58 than the one bitcoin uses. It is not compatible.
    '''
    a = [reverseBytes(v[i:i+16]) for i in range(0, len(v)-16, 16)]
    rr = int(-2*((len(v) // 2 )% 16))
    res = b''
    for b in a:
        bb = hexToInt(b)
        result = b''
        while bb >= __b58base:
            div, mod = divmod(bb, __b58base)
            result = __b58chars[mod].to_bytes(1, byteorder='little') + result
            bb = div
        result = __b58chars[bb].to_bytes(1, byteorder='little') + result
        res += result
    result = b''
    if rr < 0:
        bf =  hexToInt(reverseBytes(v[rr:])) #since we only reversed the ones in the array..
        result = b''
        while bf >= __b58base:
            div, mod = divmod(bf, __b58base)
            result = __b58chars[mod].to_bytes(1, byteorder='little') + result
            bf = div
        result = __b58chars[bf].to_bytes(1, byteorder='little') + result
    res += result
    return res

def sc_reduce32(n):
    n = int.from_bytes(n, byteorder='little')
    l = (2**252 + 27742317777372353535851937790883648493)
    reduced = n % l
    newbytes = reduced.to_bytes(32, 'little')
    return newbytes