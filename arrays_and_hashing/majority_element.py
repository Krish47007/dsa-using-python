
def get_majority(list):
    n = len(list)
    me,count = 0,0

    for i in range(n):
        if count == 0:
            me = list[i]
            count = 1
        else:
            if me != list[i]:
                count -=1
            else:
                count += 1
    return me

print(get_majority([2,3,1,1,1,4,1]))
