def pattern(n):
    ptn = [str(x) for x in range(0,10)]
    
    ret = ""
    for i in reversed(range(1,n+1)):
        b10n = i % 10
        s = ""
        for x in range(0, n-i):
            s += ptn[(n - x) % 10]
        for _ in range(0, i):
            s += ptn[b10n]
        s += "\n"
        ret += s
    ret = ret[:-1]
    return ret

print pattern(13)
