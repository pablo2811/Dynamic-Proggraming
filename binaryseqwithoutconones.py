# https://www.techiedelight.com/find-n-digit-binary-strings-without-consecutive-1s/

#simple dynamic

def count(n):

    c = [[1,1] for i in range(n)]
    for i in range(1,n):
        c[i][0] = c[i-1][0] + c[i-1][1]
        c[i][1] = c[i-1][0]
    return c[-1][0] + c[-1][1]

print(count(5))
