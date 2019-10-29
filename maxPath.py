string = '[3],[7,4],[2,4,6],[8,5,9,3] '
strs = string.replace('[','').split('],')
lists = [map(int, s.replace(']','').split(',')) for s in strs]

def maxPath(lists, index=-1):
    if index == - len(lists):
        return lists[0][0]
    for i in range(len(lists[index]) - 1):
        maximum = max(lists[index][i], lists[index][i+1])
        lists[index- 1][i] += maximum
    return maxPath(lists, index-1)

print(maxPath(lists))


