# https://www.techiedelight.com/find-minimum-cost-reach-last-cell-matrix-first-cell/

# we 'clone' initial matrix in order to (i,j) cell represent lowest sum until (i,j) cell in initial
# res is tab[-1][-1]
# main body is picking whether "we" want to come from left or above, based on lowest values

def lowest_cost(M):
    pion = len(M)
    poz = len(M[0])
    tab = [[0 for i in range(poz)] for j in range(pion)]
    tab[0][0] = M[0][0]
    # base_case
    for j in range(1,poz):
        tab[0][j] = tab[0][j-1] + M[0][j]
    for k in range(1,pion):
        tab[k][0] = tab[k-1][0] + M[k][0]
    #main
    for j in range(1,pion):
        for w in range(1,poz):
            tab[j][w] = min(tab[j-1][w],tab[j][w-1])+M[j][w]

    return tab[-1][-1]


cost = [[ 4, 7, 8, 6, 4 ],[ 6, 7, 3, 9, 2 ],[ 3, 8, 1, 2, 4 ],[ 7, 1, 7, 3, 7 ],[ 2, 9, 8, 9, 3 ]]
print(lowest_cost(cost))


