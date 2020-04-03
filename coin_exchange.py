# simple, but elegant solution

def k_max(c_i,j):
    u = 0
    while u*c_i <= j:
        u += 1
    return u - 1

def coins(c,n):

    tab = [[0 for i in range(n+1)] for g in range(len(c))]
    for w in range(1,n+1):
        if w % c[0] == 0:
            tab[0][w] = w/c[0]
        else:
            tab[0][w] = -100000 # to denote it's just impossible
    for i in range(1,len(c)):
        for j in range(1,n+1):
            km = k_max(c[i],j)
            best = float("Inf")
            for w in range(km+1):
                best = min(best,tab[i-1][j-w*c[i]]+w)
            tab[i][j] = best

    return tab[-1][-1]


def main():

    c = [1,3,4]
    n = 10
    print(coins(c,n))

if __name__ == "__main__":
    main()