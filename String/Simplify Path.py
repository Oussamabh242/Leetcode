class Solution:
    def simplifyPath(self, path: str) -> str:
        
        s = path
        
        a = []

        def ispoint(s) :
            for i in s :
                if i !="." :
                    return False
            return True

        s+="/"
        i = 0
        while i<len(s) :
            sbstring = ""
            while s[i] != "/" :
                sbstring +=s[i]
                i+=1
            if len(sbstring)>0 :
                if ispoint(sbstring) :
                    if len(sbstring)==2 and len(a)>0:
                        a.pop()
                    elif len(sbstring)>2 :
                        a.append(sbstring)
                else :
                    a.append(sbstring)
            else :
                i+=1
        ss = "/"
        if len(a)>0 :
            for i in range(len(a)-1) :
                ss+=a[i]
                ss+="/"
            ss+=a[len(a)-1]
        return ss
