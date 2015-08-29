largest = 0 
for i in reversed(range(1000)):
    for j in reversed(range(1000)):
        s = i*j
        if largest > s:
            break
        t = str(s)
        if t[:len(t)/2][::-1] == t[len(t)/2:]:
            largest = int(t)
print largest
