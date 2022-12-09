tail = 0,0
head = 0, 0
play_field = set()
def move_tail(command):
    global tail
    if head == tail:
        # head over tail
        return
    if (abs(head[0] - tail[0]) == 1 and abs(head[1] - tail[1]) == 1) or \
        (abs(head[0] - tail[0]) == 1 and abs(head[1] - tail[1]) == 0) or \
        (abs(head[0] - tail[0]) == 0 and abs(head[1] - tail[1]) == 1):
        # adjacent
        return

    if command == "L":
        tail = head[0] + 1, head[1]

    if command == "R":
        tail = head[0] - 1, head[1]

    if command == "U":
        tail = head[0], head[1] - 1

    if command == "D":
        tail = head[0], head[1] + 1
    print(f"Tail pos: {tail}")
    play_field.add(tail)

def move(line: str):
    global head
    command, amount = line.split(" ")
    amount = int(amount)
    if command == "L":
         for i in range(0, amount):
            head = head[0] - 1, head[1]
            move_tail(command)
    if command == "R":
        for i in range(0, amount):
            head = head[0] + 1, head[1]
            move_tail(command)

    if command == "U":
        for i in range(0, amount):
            head = head[0], head[1] + 1
            move_tail(command)

    if command == "D":
        for i in range(0, amount):
            head = head[0], head[1] - 1
            move_tail(command)



if __name__ == '__main__':
    f = open("input.txt", "r")
    play_field.add(head)
    print(tail)
    for line in f.readlines():
        line = line.replace("\n","")
        move(line)

    print(len(play_field))
