class Professor:
    def __init__(self, proId, proName, subjectsDict):
        self.proId = proId
        self.proName = proName
        self.subjectsDict = subjectsDict

class University:
    def getTotalExperience(self, proList, proNum):
        for i in proList:
            if i.proId == proNum:
                return sum(i.subjectsDict.keys())
        return 0

    def selectSeniorProfessorBySubject(self, proList, subName):
        result = -9
        for i in proList:
            if subName in i.subjectsDict:
                if i.subjectsDict[subName] > result:
                    result = i.subjectsDict[subName]
                return None
        return result

if __name__ == '__main__':
    run = int(input())
    proList = []
    for i in range(run):
        proId = int(input())
        proName = input()
        subjectsDict = {}
        subNum = int(input())
        for x in range(subNum):
            subject = input()
            exp = int(input())
            subjectsDict[subject] = exp
        proList.append(Professor(proId,proName,subjectsDict))
    
    
    uni = University()
    proNum = int(input())
    print(uni.getTotalExperience(proList, proNum))
    subName = input()
    print(uni.selectSeniorProfessorBySubject(proList,subName))
