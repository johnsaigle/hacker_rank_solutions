def rearrange(arr, p):
    left_list = []
    right_list = []
    for e in arr:
        if e < p:
            left_list.append(e)
        elif e > p:
            right_list.append(e)
    return(left_list + [p] + right_list)

n = input()
arr = input().split(" ")
arr = [int(x) for x in arr]
p = arr[0]

result = rearrange(arr, p)
for e in result:
    print(str(e), end=" ")
