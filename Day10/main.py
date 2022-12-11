f = open("input.txt","r")
lines = f.readlines()
lines = map(lambda a: a.replace("\n",""),lines)
x = 1
cycle = 0

values = []
values.append((cycle,x,x))

for line in lines:
    if line.startswith("noop"):
        cycle += 1
        values.append((cycle,x,x))
    else:
        command, amount = line.split(" ")
        if command == "addx":
            cycle += 1
            values.append((cycle,x,x))
            cycle += 1
            before = x
            x += int(amount)
            after = x
            values.append((cycle, before,after))



print(values)
print(values[20])
print(values[60])
print(values[100])
print(values[140])
print(values[180])
print(values[220])

def get_strength(t):
    return t[0]*t[1]

strenghts = [get_strength(values[20]),get_strength(values[60]),get_strength(values[100]),get_strength(values[140]),get_strength(values[180]),get_strength(values[220])]
print(strenghts)
print(sum(strenghts))
current_line = ""
for cycle_number,before_register_value,after_register_value in values[1:]:
    if cycle_number % 40 == 0:
        print(current_line)
        current_line = ""
    else:
        if (cycle_number % 40) in [before_register_value,before_register_value+1,before_register_value+2]:
            current_line += "#"
        else:
            current_line += "."
