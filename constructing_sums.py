
# given a list of weights (positive integers) decide which
# 0....sum(weights) can be constructed as a sum (each weight you can use max1)


def constructable(w):
    M = sum(w)
    tab = [[0 for i in range(M+1)] for j in range(len(w))]
    for j in range(len(w)):
        tab[j][0] = 1
    for k in range(1,M+1):
        if w[0] == k:
            tab[0][k] = 1
        else:
            tab[0][k] = 0

    for i in range(1,len(w)):
        for j in range(1,M+1):
            if j >= w[i]:
                tab[i][j] = tab[i-1][j] or tab[i-1][j-w[i]]
            else:
                tab[i][j] = tab[i-1][j]
    return tab[-1]

def main():
    w = [1,3,3,5]
    print(constructable(w))



if __name__ == "__main__":
    main()
