class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box  = {}
        hor ,ver , dis = 0,0 , 3
        while 1 :
            if hor >=9  :
                hor = 0
                ver += 3
            if ver == 9 : 
                break

            for i in range(hor , hor+dis) :
                for j in range(ver , ver+dis) :
                    x = board[i][j]
                    if x >= "0" and x<="9" :
                        if x in box : 
                            return False
                        else : 
                            box[x]=1
                    
            box = {}
            hor += 3
        print("pass")
        hor = {}
        for i in board :
            hor = {}
            for j in i :
                if j>="0" and j <= "9" :
                    if j in hor :
                        return False
                    else :
                        hor[j] = 1
        print("pass")
        ver = {}
        for i in range(len(board)):
            ver = {}
            for j in range(len(board)) :
                x = board[j][i]
                if x >='0' and x<='9' :
                    if x in ver :
                        print(i,j ,x)
                        return False
                    else :
                        ver[x] = 1

        return True
    
