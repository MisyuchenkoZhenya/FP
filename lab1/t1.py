# 1.1

def pascalTriangle(n = 0):
    a=[]

    for i in range(n):
        a.append([])
        a[i].append(1)

        for j in range(1,i):
            a[i].append(a[i-1][j-1]+a[i-1][j])
        if(n!=0):
            a[i].append(1)

    for i in range(n):
        print("   "*(n-i),end=" ",sep=" ")
        for j in range(0,i+1):
            print('{0:6}'.format(a[i][j]),end=" ",sep=" ")
        print()


pascalTriangle(12)


# 1.2

coins = [1, 2, 3, 4, 5, 6, 7]

def getWays(money, indexOfCoin):
    if money < 0 or indexOfCoin < 0:
        return 0
    
    if money == 0 or indexOfCoin == 0:
        return 1    

    return getWays(money, indexOfCoin - 1) + getWays(money - coins[indexOfCoin], indexOfCoin)


print(getWays(6, len(coins)-1))
