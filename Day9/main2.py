tail = [(0, 0),(0, 0),(0, 0),(0, 0),(0, 0),(0, 0),(0, 0),(0, 0),(0,0)]
head = 0, 0
play_field = set()


def adjacent_move_needed(local_head, tail_part):
    return (abs(local_head[0]-tail_part[0]) == 2 and local_head[1] != tail_part[1]) or (abs(local_head[1]-tail_part[1]) == 2 and local_head[0] != tail_part[0])


def diagonal_move_needed(local_head, tail_part):
    if abs(local_head[0]-tail_part[0]) == 2 and local_head[1] == tail_part[1]:
        return True, True # horizontal

    if abs(local_head[1]-tail_part[1]) == 2 and local_head[0] == tail_part[0]:
        return True, False # vertical

    return False, False



def move_tail(command, tail_index, adjacent_move: bool = False, before_move_tail = None):
    global tail

    if tail_index == 0:
        local_head = head
    else:
        local_head = tail[tail_index - 1]
    if local_head == tail[tail_index]:
        # head over tail
        return

    if (abs(local_head[0] - tail[tail_index][0]) == 1 and abs(local_head[1] - tail[tail_index][1]) == 1) or \
        (abs(local_head[0] - tail[tail_index][0]) == 1 and abs(local_head[1] - tail[tail_index][1]) == 0) or \
        (abs(local_head[0] - tail[tail_index][0]) == 0 and abs(local_head[1] - tail[tail_index][1]) == 1):
        # adjacent
        return



    if tail_index > 0 and adjacent_move_needed(local_head, tail[tail_index]):
        if local_head[0] > tail[tail_index][0]:
            a = list(tail[tail_index])
            a[0] = tail[tail_index][0] + 1
            tail[tail_index] = tuple(a)
        else:
            a = list(tail[tail_index])
            a[0] = tail[tail_index][0] - 1
            tail[tail_index] = tuple(a)
        if local_head[1] > tail[tail_index][1]:
            a = list(tail[tail_index])
            a[1] = tail[tail_index][1] + 1
            tail[tail_index] = tuple(a)
        else:
            a = list(tail[tail_index])
            a[1] = tail[tail_index][1] - 1
            tail[tail_index] = tuple(a)
        play_field.add(tail[len(tail) - 1])
        return

    needed, direction = diagonal_move_needed(local_head, tail[tail_index])
    if tail_index > 0 and needed:
        if direction:  # horizontal
            amount = local_head[0] - tail[tail_index][0]
            if amount > 0:
                a = list(tail[tail_index])
                a[0] = tail[tail_index][0] + 1
                tail[tail_index] = tuple(a)
            else:
                a = list(tail[tail_index])
                a[0] = tail[tail_index][0] - 1
                tail[tail_index] = tuple(a)
        else:  # vertical
            amount = local_head[1] - tail[tail_index][1]
            if amount > 0:
                a = list(tail[tail_index])
                a[1] = tail[tail_index][1] + 1
                tail[tail_index] = tuple(a)
            else:
                a = list(tail[tail_index])
                a[1] = tail[tail_index][1] - 1
                tail[tail_index] = tuple(a)
        play_field.add(tail[len(tail) - 1])
        return

    if command == "L":
        tail[tail_index] = local_head[0] + 1, local_head[1]

    elif command == "R":
        tail[tail_index] = local_head[0] - 1, local_head[1]

    elif command == "U":
        tail[tail_index] = local_head[0], local_head[1] - 1

    else: # Down
        tail[tail_index] = local_head[0], local_head[1] + 1

    print(f"Tail {tail}")
    play_field.add(tail[len(tail) - 1])

def do_same_move(tail_index, movement):
    row, column = tail[tail_index]
    row_move, col_move = movement
    tail[tail_index] = row + row_move, column + col_move

def print_play_field():
    """tail_to_use = list(map(lambda a: tuple([a[0] + 12, a[1] + 16]), tail))
    head_to_use = head[0] + 12, head[1] + 16
    for i in range(0, 40):
        line = []
        for j in range(0, 40):
            if (j,i) == (12,16):
                line.append("S")
            elif (j, i) == head_to_use:
                line.append("H")
            else:
                try:
                    index = tail_to_use.index((j, i))
                    line.append(str(index))
                except:
                    line.append(".")
        print("".join(line))"""
    return

def print_play_field_tail():
    tail_to_use = list(map(lambda a: tuple([a[0]+12, a[1]+16]),play_field))
    for i in range(0,40):
        line = []
        for j in range(0,40):
            if (j,i) == (12,16):
                line.append("S")
                continue
            try:
                index = tail_to_use.index((j,i))
                line.append("#")
            except:
                line.append(".")
        print("".join(line))
def move(line: str):
    global head
    command, amount = line.split(" ")
    amount = int(amount)
    if command == "L":
         for i in range(0, amount):
            head = head[0] - 1, head[1]
            for j in range(0,9):
                move_tail(command, j)
                print_play_field()
    if command == "R":
        for i in range(0, amount):
            head = head[0] + 1, head[1]
            for j in range(0, 9):
                move_tail(command, j)
                print_play_field()
    if command == "U":
        for i in range(0, amount):
            head = head[0], head[1] + 1
            for j in range(0, 9):
                move_tail(command, j)
                print_play_field()
    if command == "D":
        for i in range(0, amount):
            head = head[0], head[1] - 1
            for j in range(0, 9):
                move_tail(command, j)
                print_play_field()



if __name__ == '__main__':
    f = open("input.txt", "r")
    play_field.add(head)
    print(tail)
    for line in f.readlines():
        line = line.replace("\n","")
        move(line)
    print(len(play_field))
    print_play_field_tail()
