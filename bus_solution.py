from collections import deque
def stuff_passengers(size, groups):
    tmp_groups = deque(groups) # convert our list of ints into a queue so we can use pop
    current_capacity = 0
    if len(tmp_groups) == 0:
        # we have no passengers remaining -- success!
        return True
    while True:
        if len(tmp_groups) > 0:
            try:
                current_capacity += tmp_groups.popleft()
            except IndexError:
                # if the bus is not full, and we are out of groups, this is a bad fit
                return False
            if current_capacity < size:  
                continue
            elif current_capacity == size:
                # we have a perfect fit of groups in the current iteration
                return stuff_passengers(size, tmp_groups)
            else:
                # if the passengers in our bus configuration exceed its size, return false
                return False
        else:
            if current_capacity != size:
                return False
          

# set up data
def main():
    num_groups = int(input())
    groups = input() # this will be a space-separated string
    print(groups)
    groups = groups.split(" ")
    print(groups)
    groups = list(map(int, groups))
    print(groups)

    max_group = max(groups)
    group_sum = sum(groups)
    solution_set = []
    solution_set.append(group_sum) # this is always a solution

    for bus_size in range(max_group, group_sum):
        if bus_size < max_group:
            # the bus is too small
            continue
        
        if group_sum % bus_size != 0:
            # we cannot use buses of this size, or they will be fractional
            continue
    
        if stuff_passengers(bus_size, groups):
            solution_set.append(bus_size)       

    for s in sorted(solution_set):
        print (s, end=" ")

if __name__ == '__main__':
    main()
