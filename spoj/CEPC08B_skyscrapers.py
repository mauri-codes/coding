from bisect import bisect_left
height = 0
def findSky (st, fin):
    if (fin - st < 2):
        return st
    mid = st + ((fin - st) // 2)
    if (sortedSky[mid]["height"] == height):
        return mid
    elif (sortedSky[mid]["height"] < height):
        return findSky(mid + 1, fin)
    return findSky(st, mid)

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
    newLand = [False]*n_sky
    groupList = [0]*n_days
    groups = 0

    skyscrapers = [{"height": int(sky), "pos": ind} for ind, sky in enumerate(input().split(), start=0)]
    days = [{"height": -int(day), "pos": ind} for ind, day in enumerate(input().split(), start=0)]

    sortedSky = sorted(skyscrapers, key=lambda sky:sky["height"])
    sortedDays = sorted(days, key=lambda sky:sky["height"])

    lastSky = n_sky

    for day in sortedDays:
        if ((-day["height"]) < lastSky):
            pos = findFirstSky((-day["height"])+1, lastSky)
            for sky in range(pos, lastSky):
                sky_pos = sortedSky[sky]["pos"]
                adjacent = 0
                newLand[sky_pos] = True
                if ( sky_pos != 0):
                    if (newLand[sky_pos-1]):
                        adjacent += 1
                if ( sky_pos != n_sky -1):
                    if (newLand[sky_pos+1]):
                        adjacent += 1
                if (adjacent == 0):
                    groups += 1
                elif (adjacent  == 2):
                    groups -= 1
            lastSky = pos

        groupList[day["pos"]] = str(groups)
    print(" ".join(groupList))
    

