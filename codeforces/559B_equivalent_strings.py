firstString = input()
secondString = input()

def sortedStr (word):
    if (len(word) % 2 == 1):
        return word
    mid = int(len(word)/2)
    left = sortedStr(word[mid:])
    right = sortedStr(word[:mid])
    if (left > right):
        return right + left
    else:
        return left + right

valid = sortedStr(firstString) == sortedStr(secondString)

print("YES" if valid else "NO")
