string = '[3],[7,4],[2,4,6],[8,5,9,3] '
strings = string.replace('[','').split('],')
lists = [map(int, s.replace(']','').split(',')) for s in strings]

def maxPath(lists, index=-1):
    
    for i in range(len(lists[index]) - 1):
        maxSum = max(lists[index][i], lists[index][i+1])
        lists[index- 1][i] += maxSum
    return maxPath(lists, index-1)

print(maxPath(lists))


