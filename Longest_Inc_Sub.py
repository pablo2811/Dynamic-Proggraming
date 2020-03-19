## https://www.techiedelight.com/longest-increasing-subsequence-using-dynamic-programming/

def longest_inc_sub(seq):

    how_many = [0 for i in range(len(seq))]  # jakiej jest dlugosci najdluzszy podciag do i-tego elementu
    how_many[0] = 1 # dlugosc ciagu rosnacego jednoelementowego zawsze 1
    for i in range(1,len(seq)):
        for j in range(0,i):
            # szukamy maximum wsrod tych dlugosci podciagow, ktorym odpowaidajacy element jest
            # mniejszy od rozwazanego (zeby stanowily razem c. rosnacy)
            if seq[j]<seq[i] and how_many[j] > how_many[i]:
                how_many[i] = how_many[j]
        how_many[i]+=1 #dodajemy siebie

    return max(how_many)

a = [8,4,12,2,10,6,14,1,9,5,13,3,11]
print(longest_inc_sub(a))