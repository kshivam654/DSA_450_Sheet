from collections import defaultdict
from matplotlib import collections


def sort012(array):
    d = defaultdict(lambda: 0)
    for ele in array:
        d[ele] += 1
    ans = []
    ans.extend(   [   int(ele) for ele in '0'*d[0]    ]    )
    ans.extend(   [   int(ele) for ele in '1'*d[1]    ]    )
    ans.extend(   [   int(ele) for ele in '2'*d[2]    ]    )
    return ans
print(sort012([2,2,2,2,0]))