def topKFrequent(nums, k: int):
    counter = {}
    ans = []
    for i in nums:
        if i not in counter:
            counter[i] = 1
        else:
            counter[i] += 1
    counter = dict(sorted(counter.items(), key=lambda item: item[1]))
    key = list(counter.keys())
    return key[-k:]
