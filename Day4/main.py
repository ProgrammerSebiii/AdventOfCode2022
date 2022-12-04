def isContainedInOther(line: str):

    pair1, pair2 = line.replace("\n", "").split(",")
    pair1_lower, pair1_upper = pair1.split("-")
    pair2_lower, pair2_upper = pair2.split("-")
    pair1_lower = int(pair1_lower)
    pair1_upper = int(pair1_upper)
    pair2_lower = int(pair2_lower)
    pair2_upper = int(pair2_upper)
    if (pair1_lower >= pair2_lower and pair1_upper <= pair2_upper) or (
            pair2_lower >= pair1_lower and pair2_upper <= pair1_upper):
        return True
    else:
        return False


def overlaps(line: str):

    pair1, pair2 = line.replace("\n", "").split(",")
    pair1_lower, pair1_upper = pair1.split("-")
    pair2_lower, pair2_upper = pair2.split("-")
    pair1_lower = int(pair1_lower)
    pair1_upper = int(pair1_upper)
    pair2_lower = int(pair2_lower)
    pair2_upper = int(pair2_upper)
    if (pair1_lower >= pair2_lower and pair1_upper <= pair2_upper) or (
            pair2_lower >= pair1_lower and pair2_upper <= pair1_upper):
        return True

    elif (pair1_lower >= pair2_lower and pair1_lower <= pair2_upper) or \
            (pair1_upper >= pair2_lower and pair1_upper <= pair2_upper) or \
            (pair2_lower >= pair1_lower and pair2_lower <= pair1_upper) or \
            (pair2_upper >= pair1_lower and pair2_upper <= pair1_upper):
        return True

    else:
        return False


if __name__ == '__main__':
    f = open("pairs.txt", "r")
    counter_contained = 0
    counter_overlap = 0
    for line in f.readlines():
        if isContainedInOther(line):
            counter_contained += 1
        if overlaps(line):
            counter_overlap += 1
    print(counter_contained)
    print(counter_overlap)


