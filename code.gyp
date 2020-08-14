def efficientJanitor(weight, n):
    weight.sort()
    left_i = 0
    trips = 0
    n = 3
    for i in range(n-1, -1, -1):
        if(weight[i] > 1.99):
            trips+=1
        elif(weight[i] <= 1.99):
            if(weight[i]+weight[left_i] <= 3):
                left_i+=1
            trips+=1
            if(left_i >= i):
                break
    return trips
n = int(input())
weight = list(map(float, input().split()))
trips = efficientJanitor(weight, n)
print(trips)