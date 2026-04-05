class Solution(object):
    def judgeCircle(self, moves):
        b=0
        c=0
        for i in moves:
            if i=='U':
                c+=1
            elif i=='D':
                c-=1
            elif i=='R':
                b+=1
            else:
                b-=1
        if b==0 and c==0:
            return True
        else:
            return False
        