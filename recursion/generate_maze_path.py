class Maze_Path:

    def genPath(self,n,m):
        ans = []
        def rec(i,j,str):
            if i == n or j == m:
                return
            if i == n-1 and j == m-1:
                ans.append(str)
                return

            #Go down
            rec(i+1,j,str + "D")
            #Go right
            rec(i,j+1,str + "R")

        rec(0,0,"")
        return ans

obj = Maze_Path()
print(obj.genPath(2,3))