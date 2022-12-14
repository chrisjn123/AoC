#with open('test.txt', 'r') as fh:
with open('input.txt', 'r') as fh:
    data = [line.strip() for line in fh.readlines()]

visible = 2 * len(data[0]) + 2*(len(data) - 2)
print(f'Starting visible: {visible}')
ending_row_idx = len(data) - 2      # 2nd to last row
ending_col_idx = len(data[0]) - 2   # 2nd to last col

def visible_in_col(row, col) -> bool:
    ret = False
    column = [val[col] for val in data]

    left = column[:row + 1]
    right = column[row:]
    right = right[::-1]

    # simple check of left and right if its the same or smaller than the neighbors
    if column[row - 1] >= column[row] and column[row + 1] >= column[row]:
        ret = False
    
    #elif column.index(max(column)) == row
    elif left.index(max(left)) == row or right.index(max(right)) == len(right) - 1:
        ret = True
    
    return ret

def visible_in_row(row, col):
    ret = False
    r = data[row]

    left = r[:col + 1]
    right = r[col:]
    right = right[::-1]

    if r[col - 1] >= r[col] and r[col + 1] >= r[col]:
        pass
    elif left.index(max(left)) == col or right.index(max(right)) == len(right) - 1:
        ret = True
    
    return ret

for i in range(1, len(data) - 1):
    for j in range(1, len(data[0]) -1):
        if visible_in_col(i, j) or visible_in_row(i, j):
            #print(f'Row: {i}\tCol: {j}')
            visible+=1

print(f"Visible: {visible}")

def up(i, j):
    tmp = i - 1
    local_score = 0
    if data[tmp][j] == data[i][j]:
        return 1
    while(data[tmp][j] <= data[i][j]):
        local_score += 1
        tmp -= 1
        if tmp < 0 or data[tmp][j] == data[i][j]:
            break
        if data[tmp+1][j] == data[i][j]:
            break
    return local_score

def down(i, j):
    tmp = i + 1
    local_score = 0
    if data[tmp][j] == data[i][j]:
        return 1
    while(data[tmp][j] <= data[i][j]):
        local_score += 1
        tmp += 1
        if tmp > len(data) -1:
            break
        if data[tmp-1][j] == data[i][j]:
            break
    return local_score

def left(i, j):
    tmp = j - 1
    local_score = 0
    if data[i][tmp] == data[i][j]:
        return 1
    while(data[i][tmp] <= data[i][j]):
        local_score += 1
        tmp -= 1
        if tmp < 0:
            break
        if data[i][tmp+1] == data[i][j]:
            break
    return local_score

def right(i, j):
    tmp = j + 1
    local_score = 0
    
    if data[i][tmp] == data[i][j]:
        return 1
    while(data[i][tmp] <= data[i][j]):
        local_score += 1
        tmp += 1
        if tmp > len(data[0]) - 1:
            break
        if data[i][tmp-1] == data[i][j]:
            break
    return local_score

scores = []
for i in range(1, len(data) - 1):
    for j in range(1, len(data[0]) - 1):
        score = []
        score.append(left(i,j))
        score.append(right(i,j))
        score.append(up(i,j))
        score.append(down(i,j))
        a = score[0] * score[1] * score[2] * score[3]
        scores.append(a)

print(f'Scenic: {max(scores)}')