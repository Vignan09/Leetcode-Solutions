class Solution(object):
    def isAnagram(self, s, t):
        a={}
        for i in s:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        for i in t:
            if i in a and a[i]==1:
                del a[i]
            elif i in a:
                a[i]-=1
            else:
                return False
        if len(a)==0:
            return True
        else:
            return False   
        