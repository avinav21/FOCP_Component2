import sys

class Team:
    
    def __init__(self,team):

        self.getteam(team)
        self.getP(0)
        self.getW(0)
        self.getD(0)
        self.getL(0)
        self.getF(0)
        self.getA(0)
        self.getDiff(0)
        self.getPts(0)

    def getteam(self,team):
        self.team=team

    def getP(self,P):
        self.P=P

    def getW(self,W):
        self.W=W

    def getD(self,D):
        self.D=D
    
    def getL(self,L):
        self.L=L

    def getF(self,F):
        self.F=F

    def getA(self,A):
        self.A=A

    def getDiff(self,Diff):
        self.Diff=Diff

    def getPts(self,Pts):
        self.Pts=Pts

    def setteam(self):
        return self.team

    def setP(self):
        return self.P

    def setW(self):
        return self.W

    def setD(self):
        return self.D

    def setL(self):
        return self.L

    def setF(self):
        return self.F

    def setA(self):
        return self.A

    def setDiff(self):
        return self.Diff

    def setPts(self):
        return self.Pts

    def getscore(self,F,A):
        """
        This function gets the scores and set the values of other attributes similarly.
        Parameters: self, F , A
        Returntype: None
        """
        self.getF(self.setF()+F)
        self.getA(self.setA()+A)
        self.getP(self.setP()+1)
        self.getDiff(self.setDiff()+(F-A)) 

        if F > A:
            self.getW(self.setW()+1)
            self.getPts(self.setPts()+3)

        elif F>A:
            self.getL(self.setL()+1)

        else:
            self.getD(self.setD()+1)
            self.getPts(self.setPts()+1)


          
teams=[]
lst=[]
title=sys.argv

file=open("team.csv","r")

for i in file:
    team =  Team(i.replace("\n",""))
    teams.append(team)

file = open("result.csv","r")

for i in file:
    lst=i.replace("\n","").split(",")

    for j in teams:
        if j.setteam()==lst[0]:
            j.getscore(int(lst[1]),int(lst[3]))

        elif j.setteam()==lst[2]:
            j.getscore(int(lst[3]),int(lst[1]))

teams.sort(reverse=True, key=lambda e: (e.setPts(), e.setDiff()))

if len(title)>1:
    print(title[1])
    print("="*len(title[1]))

print(f"{'':>10}{'P':>6}{'W':>6}{'D':>6}{'L':>6}{'F':>6}{'A':>6}{'Diff':>6}{'Pts':>6}")
for i in teams:
    print(f"{i.setteam():>10}{i.setP():>6}{i.setW():>6}{i.setD():>6}{i.setL():>6}{i.setF():>6}{i.setA():>6}{i.setDiff():>6}{i.setPts():>6}")