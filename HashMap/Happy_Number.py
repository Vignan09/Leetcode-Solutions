class Solution(object):
    def isHappy(self, n):
        dict={}
        sum=0
        if n==1:
            return True
        while n not in dict:
            dict[n]=1
            while n>0:
                temp=n%10
                n=n/10
                sum+=temp*temp
            if sum==1:
                return True
            n=sum
            sum=0 
        return False