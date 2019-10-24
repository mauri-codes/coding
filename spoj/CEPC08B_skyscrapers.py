from bisect import bisect_left
height = 0
def findSky (st, fin):
    if (fin - st < 2):
        if (sortedSky[st]["height"] == height):
            return st
        else:
            return -1
    mid = st + ((fin - st) // 2)
    if (sortedSky[mid]["height"] == height):
        return mid
    first = findSky(st, mid)
    if (first != -1):
        return first
    second = findSky(mid + 1, fin)
    if (second != -1):
        return second
    return -1

def findFirstSky (h, n):
    global height
    height = h
    pos = findSky (0, n)
    while(True):
        if (pos == 0):
            break
        if(sortedSky[pos]["height"] != sortedSky[pos -1]["height"]):
            break
        pos -= 1
    return pos


tests = int(input())
results = [0]*tests
for test in range(tests):
    n_sky, n_days = [int(x) for x in input().split()]
    skyscrapers = [{"height": int(sky), "pos": ind} for ind, sky in enumerate(input().split(), start=0)]
    sortedSky = sorted(skyscrapers, key=lambda sky:sky["height"])

    days = [findFirstSky(int(day), n_sky) for day in input().split()]
    
    print(days)
    # skyCopy = [-1]*(n_sky+1)
    # print(sortedSky)

    # for sky in sortedSky:
    #     skyCopy[sky["pos"]+1] = 1

    # print(skyCopy)
    # groups = 0
    # for ind in range(1, n_sky):
    #     if skyCopy(ind) != -1 and skyCopy(ind-1) == -1:
    #         groups += 1
    # results[test] = groups
# print(results)

