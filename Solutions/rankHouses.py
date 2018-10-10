# RealtorID HouseID Score ZipCode 
def rankHouses(scores):
    RealtorLst = []
    maxScore = 0
    maxScore_i = 0
    result = []
    while len(scores) > 0:
        for i in xrange(len(scores)):
            if scores[i][0] in RealtorLst: continue
            if scores[i][2] > maxScore:
                maxScore = scores[i][2]
                maxScore_i = i
        # print RealtorLst
        if maxScore !=0: 
            RealtorLst.append(scores[maxScore_i][0])
            if len(RealtorLst) > 4: RealtorLst = []
            result.append(scores.pop(maxScore_i))
            maxScore = 0
        else:
            RealtorLst = []
    return result



a = [[2,180,497,60632],
[4, 121, 485, 60615],
[3, 133,477,60610],
[2, 74,457,60611],
[5, 118,377,60609],
[5, 186,369,60611],
[3, 187,314,60615],
[6, 45,227,60609],
[6, 152,226,60609],
[4, 82,173,60615]]

b = [[2, 180, 497, 60632],
[4, 121, 485, 60615],
[3, 133, 477, 60610],
[2, 74, 457, 60611],
[5, 118, 377, 60609],
[5, 186, 369, 60611],
[3, 187, 314, 60615],
[6, 45, 227, 60609],
[6, 152, 226, 60609],
[4, 82, 173, 60615]]
print rankHouses(a)
print
print rankHouses(b)
print 
