from collections import Counter
string1 = str(input())
string2 = str(input())

c1 = Counter(string1)
c2 = Counter(string2)

deletions = 0
for e in c1:
    if e in c2:
        deletions += abs(c1[e] - c2[e])
    else:
        deletions += c1[e]
for e in c2:
    # we only need to check elements not in e1, or else we'd be counting twice
    if not e in c1:
        deletions += c2[e]    
print(deletions)