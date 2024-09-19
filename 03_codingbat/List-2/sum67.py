def sum67(nums):
    isT = True
    sum = 0
    for i in nums:
        if i == 6:
            isT = False
        if isT:
            sum += i
            continue
        if i == 7:
            isT = True
    return sum
