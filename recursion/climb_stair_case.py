def generate_stair_steps(n):
    ans = []

    def rec(n,str):
        if(n == 0):
            ans.append(str)
            return
        if( n < 0):
            return

        #Take one step
        rec(n-1,str + "1")
        #Take two steps
        rec(n-2,str + "2")

    rec(n,"")
    return ans

print(generate_stair_steps(5))