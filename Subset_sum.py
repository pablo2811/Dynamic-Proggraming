# https://www.techiedelight.com/subset-sum-problem/

# poziomo sumy od 0...s pionowo kolejne wyrazy ktore bierzemy pod uwage
# result w prawym dolnym

def doesitexist(l,sum):

    pion = len(l)
    poz = sum + 1
    tab = [[0 for i in range(sum+1)] for k in range(pion)]
    for w in range(poz):
        if l[0] == w :
            tab[0][w] = 1
    for j in range(1,pion):
        for k in range(1,poz):
            if l[j] <= k:
                tab[j][k] = tab[j-1][k] or tab[j-1][k-l[j]]
            else:
                tab[j][k] = tab[j-1][k]
    return tab[-1][-1]

l = [7,3,2,5,8]
s = 14

print(doesitexist(l,s))
