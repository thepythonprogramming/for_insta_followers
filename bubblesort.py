
arr = [7, 3, 9, 2, 0, 4, 8, 1, 6, 5]


def bubbleSort(theSeq):
    n = len(theSeq)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if theSeq[j] > theSeq[j + 1]:
                temp = theSeq[j]
                theSeq[j] = theSeq[j+1]
                theSeq[j + 1] = temp
    return theSeq


print(bubbleSort(arr))
