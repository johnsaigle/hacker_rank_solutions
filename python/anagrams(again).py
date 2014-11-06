from collections import Counter
n = int(input())

def get_deletions(string1, string2):
    deletions = 0
    c1 = Counter(string1)
    c2 = Counter(string2)
    for e in c1:
        if e in c2:
            deletions += abs(c1[e] - c2[e])
        else:
            deletions += c1[e]
    for e in c2:
        # we only need to check elements not in e1, or else we'd be counting twice
        if not e in c1:
            deletions += c2[e]
    return int((deletions)/2) # we are doing this because this code calculates the total difference, which is double what we want for the scope of this question
     # it's not plagiarism; it's code reuse

for i in range(n):
    string = str(input())
    if len(string)%2 ==0:
        a, b = string[:len(string)//2], string[len(string)//2:]
        print (get_deletions(a,b))
    else:
        print (str(-1))
