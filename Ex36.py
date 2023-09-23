def minchange(change,coins):
    min = [0]
    for num in range(1,change+1):
        min.append(num)
        for coin in coins:
            if num >= coin:
                x=min[num-coin]+1
                if x<min[num]:
                    min[num]=x
    return min[change]

if __name__ == "__main__":
    change = 41
    coins = [ 1, 5, 10,20,25,50]
    print(minchange(change,coins))