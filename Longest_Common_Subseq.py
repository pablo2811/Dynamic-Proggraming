## https://www.techiedelight.com/longest-common-subsequence/

# tworzymy tabele, ktorej jeden wymiar stanowia znaki stringa X, drugi znaki stringa Y
# w (i,j) komorke tej tabeli wpisywac bedziemy dlugosc najdluzszego wspolnego substringa z
# X[0...i] oraz Y[0....j], odpowiedz bedzie wiec stanowic komorka tab[-1][-1] (prawy dolny rog)
# pierwszy wiersz i kolumne wypelniamy zerami ( bo nie ma czesci wspolnej pustego z czymkolwiek)

# dalej, jesli znaki sie zgadzaja to nalezy wziac wynik dla obu stringow z obcietym ostatnim znakiem
# i dodanym "samym sobą" czyli komorka [i-1][j-1] + 1

#jesli zas znaki sie NIE ZGADZAJA to zastanawiamy sie, co dawalo nam dluzszy wspolny podciag znakow
# bez "nowego znaku" w X czy bez "nowego znaku" w Y

#zgodnie z tym rozumowaniem wybieramy wiekszą z wartosci odpowiadajacych dlugoscia wspolnych
#podciagow znakow bez tych znakow ( czyli maksimum z komorki "u gory" i "na lewo")


def LCS(X,Y):

    L = len(X)+1; M = len(Y)+1
    tab = [[0 for j in range(M)] for i in range(L)]

    for u in range(L-1):
        for k in range(M-1):
            if X[u] == Y[k]:
                tab[u+1][k+1] = tab[u][k] + 1
            else:
                tab[u+1][k+1] = max(tab[u][k+1],tab[u+1][k])

    return tab[-1][-1]

print(LCS("roman","roromanx"))




