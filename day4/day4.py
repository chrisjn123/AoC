with open('input.txt', 'r') as fh:
    data = [line.strip() for line in fh.readlines()]

def range_subset(range1, range2):
    """Whether range1 is a subset of range2."""
    if not range1:
        return True  # empty range is subset of anything
    if not range2:
        return False  # non-empty range can't be subset of empty range
    if len(range1) > 1 and range1.step % range2.step:
        return False  # must have a single value or integer multiple step
    return range1.start in range2 and range1[-1] in range2

count = 0
for line in data:
    left, right = line.split(',')

    leftStart = int(left.split('-')[0])
    leftEnd = int(left.split('-')[1])
    
    rightStart = int(right.split('-')[0])
    rightEnd = int(right.split('-')[1])
    
    leftRange = range(leftStart, leftEnd + 1)
    rightRange = range(rightStart, rightEnd + 1)

    if range_subset(rightRange, leftRange) or range_subset(leftRange, rightRange):
        count += 1
        continue
    if rightEnd == leftStart or leftEnd == rightStart \
        or rightEnd == leftEnd or rightStart == leftStart:
        print('{}\t\t{}'.format(left, right))
        count+=1
        continue
    if leftEnd in rightRange or rightEnd in leftRange:
        count+=1

print(count)