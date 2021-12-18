def maxFrequency(changed):
        changed.sort()
        print(changed)
        if len(changed)%2 != 0:
            return []
        else:
            for i in changed:
                if (i*2) in changed:
                    changed.remove(i*2)
                else:
                    return []
            return changed

changed = [1,2,3,4,5]
print(maxFrequency(changed))
        