f = open("calories_file.txt", "r")
elves = []
current = 0
currentIndex=0
for line in f.readlines():
    if line == "\n":
        elves.append(current)
        current = 0
    else:
        current += int(line)
elves.sort()
elves.reverse()
print(f"Most calories: {elves[0]}")
print(f"Average of top 3: {(elves[0] + elves[1] + elves[2])}")