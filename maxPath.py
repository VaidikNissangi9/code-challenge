string = '''3
7 4
2 4 6
8 5 9 3'''
strings = string.split('\n')
lists=[map(int,w.split(' ')) for w in strings ]
def maxPath(lists, index=-1):  
    if index==-len(lists) :
        return lists[0][0]
    for i in range(len(lists[index]) - 1):
        maxSum = max(lists[index][i], lists[index][i+1])
        lists[index- 1][i] += maxSum
    return maxPath(lists, index-1)

print(maxPath(lists))


