## https://www.techiedelight.com/increasing-subsequence-with-maximum-sum/

def longestbigest(seq):

    n = len(seq)
    sum = [0 for r in range(n)]
    sum[0] = seq[0]
    # lista sum, zawiera na i-tym elemencie najwieksza wartosc sumy rosnacego podciagu
    # ciagu seq[0:i], zwracamy wiec max(sum)
    for i in range(1,n):
        for j in range(0,i):
            if seq[j] < seq[i] and sum[j] > sum[i]:
                sum[i] = sum[j]
        sum[i] += seq[i]
    return max(sum)

a = [8,4,12,2,10,6,14,1,9,5,13,3,11]
print(longestbigest(a))
