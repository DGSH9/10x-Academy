def maximum_value(input_numbers):
    x=max(input_numbers)
    return x
def minimum_value(input_numbers):
    y=min(input_numbers)
    return y
def get_numbers_in_range(input_numbers, m1, m2):
    list4 = []
    x,y = m1,m2
    m1 = min(x,y)
    m2 = max(x,y)
    for i in input_numbers:
        if(i>=m1 and i<=m2):
            list4.append(i)
    if len(list4)>0:
        return list4
    return [-1]
if __name__ == "__main__":
    list1 = [int(i) for i in input().split(' ')]
    list2 = [int(i) for i in input().split(' ')]
    list3 = [int(i) for i in input().split(' ')]
    m1 = minimum_value(list1)
    m2 = maximum_value(list2)
    min_max_range = get_numbers_in_range(list3, m1, m2)
    [print(i) for i in min_max_range]