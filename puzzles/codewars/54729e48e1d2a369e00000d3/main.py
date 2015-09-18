def decode(msg, contents):
    ret = []
    for i in range(26):
        s = ""
        for c in msg:
            d = ord(c) + i
            if d > ord('z'):
                d = d - ord('z') + ord('a') - 1 
            s = s + chr(d)
        if contents in s:
            ret.append(s)
    return ret
