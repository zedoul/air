nums = [
"",
"one",
"two",
"three",
"four",
"five",
"six",
"seven",
"eight",
"nine"]

teens = [
"ten",
"eleven",
"twelve",
"thirteen",
"fourteen",
"fifteen",
"sixteen",
"seventeen",
"eighteen",
"nineteen",]

tenth = [
"",
"ten",
"twenty",
"thirty",
"forty",
"fifty",
"sixty",
"seventy",
"eighty",
"ninety",
"hundred"]

def numberLetterCounts(fr,to):
    assert (to < 1000 and to >= 0)
    assert (fr < to and fr >= 0)

    ret = 0
    for i in xrange(fr, to+1):
        letters = ""
        h = i / 100
        m = (i % 100) / 10
        s = (i % 10)
        if h > 0:
            letters += nums[h] + " hundred"
            if m > 0 or s > 0:
                letters += " and "
        if m == 1:
            letters += teens[s]
        else :
            if m > 0:
                letters += tenth[m]
            if s > 0:
                letters += nums[s]
        print str(i) + "-"+str(h)+":"+str(m)+":"+str(s) + " = " + letters
        ret += len(letters.replace(" ",""))
    return ret
print numberLetterCounts(1,999) + 11
