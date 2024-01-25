from collections import defaultdict

def solution(N, stages):
    total = len(stages)
    challenger_count = defaultdict(int)
    fail_percent = defaultdict(float)

    for stage in stages:
        challenger_count[stage] += 1

    for stage in range(1, N+1):
        if (challenger_count[stage] == 0):
            fail_percent[stage] = 0
        else:
            fail_percent[stage] = challenger_count[stage] / total
            total -= challenger_count[stage]

    return sorted(fail_percent, key=lambda x: fail_percent[x], reverse=True)
