def gray_code(n):
    ans = []
    if n == 1:
        ans.append("0")
        ans.append("1")
        return ans

    prev = gray_code(n-1)

    #Generate first half
    for i in range(len(prev)):
        ans.append("0"+prev[i])

    #Generate 2nd half
    for i in range(len(prev) - 1,-1,-1):
        ans.append("1" + prev[i])

    return ans

print(gray_code(2))
print(gray_code(3))
