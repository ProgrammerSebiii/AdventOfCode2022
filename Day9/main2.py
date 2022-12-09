tail = [(0, 0),(0, 0),(0, 0),(0, 0),(0, 0),(0, 0),(0, 0),(0, 0),(0,0)]
head = 0, 0
play_field = set()
def move_tail(command, tail_index):
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

    if command == "L":
        tail[tail_index] = local_head[0] + 1, local_head[1]

    if command == "R":
        tail[tail_index] = local_head[0] - 1, local_head[1]

    if command == "U":
        tail[tail_index] = local_head[0], local_head[1] - 1

    if command == "D":
        tail[tail_index] = local_head[0], local_head[1] + 1

    print(f"Tail pos: {tail[8]}")
    play_field.add(tail[len(tail) - 1])

def move(line: str):
    global head
    command, amount = line.split(" ")
    amount = int(amount)
    if command == "L":
         for i in range(0, amount):
            head = head[0] - 1, head[1]
            for i in range(0,9):
                move_tail(command, i)
    if command == "R":
        for i in range(0, amount):
            head = head[0] + 1, head[1]
            for i in range(0,9):
                move_tail(command, i)
    if command == "U":
        for i in range(0, amount):
            head = head[0], head[1] + 1
            for i in range(0,9):
                move_tail(command, i)
    if command == "D":
        for i in range(0, amount):
            head = head[0], head[1] - 1
            for i in range(0, 9):
                move_tail(command, i)



if __name__ == '__main__':
    f = open("test.txt", "r")
    play_field.add(head)
    print(tail)
    for line in f.readlines():
        line = line.replace("\n","")
        move(line)

    print(len(play_field))
