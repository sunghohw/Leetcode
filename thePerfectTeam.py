
def differentTeams(skills):
    teams = {'p':0,'c':0,'m':0,'b':0,'z':0}
    count = len(skills)/5
    for i in xrange(len(skills)):
        teams[skills[i]] += 1
        if skills[i] not in teams:
            While(True)

    for k,v in teams.items():
        if v < count:
            count = v
    print teams
    return v

print(differentTeams("pcmbz"))
print(differentTeams("pcmpcmbbbzz"))
print(differentTeams("pcmpppcmpcmbbbpcmcmcmcmcpppmcmcmzzpcmpcmbbbzzpcmpcmbbbzz"))