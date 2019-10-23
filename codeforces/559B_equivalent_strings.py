firstString = input()
secondString = input()

def equivalent(first, second):
    if (first == second):
        return True
    if (len(first)%2 != 0  or len(second)%2 != 0):
        return False
    strMid = int(len(first)/2)
    firstLeft = first[:strMid]
    firstRight = first[strMid:]
    secondLeft = second[:strMid]
    secondRight = second[strMid:]

    return equivalent(firstLeft, secondRight) and equivalent(firstRight, secondLeft)

valid = equivalent(firstString, secondString)

print("YES" if valid else "NO")
