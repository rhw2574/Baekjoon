input = list(map(int,input().split()))
n = input[0]
m = input[1]

def div(a , b):
    if a>b:
        return (b-1)+b*(a-1)
    else:
        return (a-1)+a*(b-1)

sum = div(n,m)
print(sum)