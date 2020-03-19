# tworzymy tabele ktora na "pionowej" osi zawiera kolejne elementy do wziecia,
# a na poziomej osi zawiera wagi od 0 do wagi plecaka
# w (i,j) takiej tabeli bedziemy przechowywac najwieksza wartosc jaka jestesmy w stanie
# osiagnac biorac tylko elementy od indeksach 0...i -> rezultat tab[-1][-1]
# wadze 0 odpowiadaja wartosci 0 -> I kolumna to same 0
# pojedynczy przedmiot (pierwszy) bierzemy jesli jego masa nie przekracza masy plecaka -> I wiersz
# potem dla kazdej z wag 1..W_max podejmujemy decyzje czy taki przedmiot bierzemy czy tez nie
# jesli nie bierzemy to makymalna uzyskana wartosc rowna wartosci bez tego przedmiotu, o tej samej wadze
# (komóka ponad "nami")
# jesli bierzemy zaś (co moze zajsc jedynie w przypadku gdy masa rozwazanego przedmiotu nie przekracza aktualnej wagi)
# to uzyskamy wartosc taka jak dla poprzedniego zestawu przedmiotow z wagą rowna aktualnej wadze
# minus wadze rozwaznaego przedmiotu w sumie z "nasza" wartoscia
# bierzemy co sie bardziej oplaca, czyli maksimum
# tak do konca, zwaracamy calosc

def knapsack(items,W):

    num_items = len(items)
    tab = [[0 for k in range(0,W+1)] for i in range(num_items)]
    # tab(i,j) zwraca najwieksza wartosc biorac tylko itemy (0...i)
    for i in range(1,W+1):
        if items[0][0] <= i:
            tab[0][i] = items[0][1]
    for j in range(1,num_items):
        for i in range(1,W+1):
            if i >= items[j][0]:
                # decyzja czy bierzemy czy nie
                tab[j][i] = max(tab[j-1][i],tab[j-1][i-items[j][0]]+items[j][1])
            else:
                # nie mozemy wybrac
                tab[j][i] = tab[j-1][i]
    return tab[-1][-1]

it = [[5,60],[3,50],[4,70],[2,30]] # pairs (weight,value)
w = 5
print(knapsack(it,w))
