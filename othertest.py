__b58chars = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
__b58base = len(__b58chars)

def b58encode(v):
    a = [reverseBytes(v[i:i+16]) for i in range(0, len(v)-16, 16)]
    rr = -2*((len(v) /2 )% 16)

    res = ''
    for b in a:
        bb = hexToInt(b)
        result = ''
        while bb >= __b58base:
            div, mod = divmod(bb, __b58base)
            result = __b58chars[mod] + result
            bb = div
        result = __b58chars[bb] + result
        res += result
    result = ''
    if rr < 0:
        bf =  hexToInt(reverseBytes(v[rr:])) #since we only reversed the ones in the array..
        result = ''
        while bf >= __b58base:
            div, mod = divmod(bf, __b58base)
            result = __b58chars[mod] + result
            bf = div
        result = __b58chars[bf] + result
    res += result
    return res

def reverseBytes(a): #input is byte string, it reverse the endianness
    b = [a[i:i+2] for i in range(0, len(a)-1, 2)]
    return ''.join(b[::-1])