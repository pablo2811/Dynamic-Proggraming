# https://www.techiedelight.com/rot-cutting/

def maximize(prices,rod):

    tab = [[0 for i in range(rod+1)] for j in range(rod)]
    # base_case
    for w in range(1,rod+1):
        tab[0][w] = w*prices[0]

    for j in range(1,rod):
        for i in range(1,rod+1):
            if j+1>i:
                tab[j][i] = tab[j-1][i]
            else:
                tab[j][i] = max(tab[j-1][i],tab[j-1][i-(j+1)]+prices[j],tab[j][i-(j+1)]+prices[j])

    return tab[-1][-1]

prices = [1,5,8,9,10,17,17,20]
rod = 4
print(maximize(prices,rod))



