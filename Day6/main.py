test_1 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
test_2 = "nppdvjthqldpwncqszvftbrmjlhg"
test_3 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
test_4 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

def get_first_occurence_in_sequence(seqeuence: str, num_of_distinct_characters: int):
    seq_list = list(seqeuence)
    for i in range(num_of_distinct_characters, len(seq_list)):
        if len(set(seq_list[i-num_of_distinct_characters:i])) == num_of_distinct_characters:
            return i
    return -1

print(get_first_occurence_in_sequence(test_1, 4))
print(get_first_occurence_in_sequence(test_2, 4))
print(get_first_occurence_in_sequence(test_3, 4))
print(get_first_occurence_in_sequence(test_4, 4))

f = open("input.txt","r")
for line in f.readlines():
    line = line.replace("\n","")
    print(get_first_occurence_in_sequence(line, 4))

print(get_first_occurence_in_sequence(test_1, 14))
print(get_first_occurence_in_sequence(test_2, 14))
print(get_first_occurence_in_sequence(test_3, 14))
print(get_first_occurence_in_sequence(test_4, 14))

f = open("input.txt","r")
for line in f.readlines():
    line = line.replace("\n","")
    print(get_first_occurence_in_sequence(line, 14))
