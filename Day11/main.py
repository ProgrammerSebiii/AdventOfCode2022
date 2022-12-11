import operator
from enum import Enum
import math
f = open("input.txt","r")

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod,
    '^' : operator.xor,
}

def convert_items_to_list(items_string):
    items = []
    for item in items_string:
        items.append(int(item))
    return items

def convert_operation_to_lambda(first_operand,operation,second_operand):
    if first_operand == "old":
        if second_operand == "old":
            return lambda a: ops[operation](a,a)
        else:
            return lambda a: ops[operation](a,int(second_operand))
    else:
        if second_operand == "old":
            return lambda a: ops[operation](int(first_operand), a)
        else:
            return lambda a: ops[operation](int(first_operand), int(second_operand))

class Entries(Enum):
    items = "items"
    inspections = "inspections"
    operation = "operation"
    test = "test"
    true_monkey = "true_monkey"
    false_monkey = "false_monkey"

def create_monkey_dict(items, operation, test, true_monkey, false_monkey):
    dictionary = {
        Entries.items: items,
        Entries.inspections: 0,
        Entries.operation: operation,
        Entries.test: test,
        Entries.true_monkey: true_monkey,
        Entries.false_monkey: false_monkey
    }
    return dictionary

monkey_list = []

while True:
    first = f.readline()
    if first == "\n":
        continue
    *_, Monkey = first.replace("\n","").split(" ")
    if Monkey == "":
        break
    _,_,_,_,*items = Starting = f.readline().replace("\n","").split(" ")
    items = list(map(lambda val: val.replace(",",""),items))
    items = list(map(lambda a: int(a), items))
    *_,first_operand,operation,second_operand = f.readline().replace("\n","").split(" ")
    function_to_do = convert_operation_to_lambda(first_operand, operation, second_operand)
    *_,divisible_by = f.readline().replace("\n", "").split(" ")
    *_,true_target_monkey = f.readline().replace("\n","").split(" ")
    *_,false_target_monkey = f.readline().replace("\n","").split(" ")

    monkey_list.append(create_monkey_dict(items, function_to_do, int(divisible_by), int(true_target_monkey), int(false_target_monkey)))

supermod = 1
for monkey in monkey_list:
    supermod *= monkey[Entries.test]



# 20 rounds
for i in range(0,10000):
    for monkey in monkey_list:
        if len(monkey[Entries.items]) == 0:
            continue
        for item in monkey[Entries.items]:
            new_worry_level_after_inspection = monkey[Entries.operation](item)
            new_worry_level = int(math.floor(new_worry_level_after_inspection % supermod))
            if new_worry_level % monkey[Entries.test] == 0:
                monkey_list[monkey[Entries.true_monkey]][Entries.items].append(new_worry_level)
            else:
                monkey_list[monkey[Entries.false_monkey]][Entries.items].append(new_worry_level)
            monkey[Entries.inspections] += 1
        monkey[Entries.items] = []

most = list(map(lambda a: a[Entries.inspections], monkey_list))
first_max = max(most)
most.remove(max(most))
second_max = max(most)
print(first_max*second_max)