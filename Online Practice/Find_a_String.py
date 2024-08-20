def count_total_occurrence(string, sub_string):
    """count1 = 0
    pos = -1

    while pos < len(string):
        z = string.find(sub_string, pos + 1, len(string))
        if z == -1:
            break
        count1 += 1
        pos = z
    return count1"""

    count1 = 0
    sub_len = len(sub_string)
    for i in range(len(string)):
        z = string[i: i + sub_len]
        if z == sub_string:
            count1 += 1
    return count1


count = count_total_occurrence("ABCDCDC", "CDC")
print("Total occurrence of substring is", count)
