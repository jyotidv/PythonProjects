import random


def binarySort(trees, first, last, item):
    if last >= first:
        mid = int((last + first) / 2)
        if trees[mid] == item:
            print("Item found at place:" + str(mid) + " value is:"+ str(trees[mid]))
            return mid
        elif trees[mid] > item:
            return binarySort(trees, first, mid - 1, item)
        elif trees[mid] < item:
            return binarySort(trees, mid + 1, last, item)

    return -1


list = []

for i in range(1, 100, 2):
    list.append(i)

print(list)
print("Searchh..."+str(binarySort(list, 0, len(list), 73)))
