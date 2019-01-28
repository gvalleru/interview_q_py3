def merge_sorted_lists(l1, l2):
    l1_current = l2_current = 0
    new_list = []
    for i in range(len(l1) + len(l2)):
        if l1_current == len(l1):
            new_list += l2[l2_current:]
            return new_list
        elif l2_current == len(l2):
            new_list += l1[l1_current:]
            return new_list
        elif l1_current < len(l1) and l1[l1_current] <= l2[l2_current]:
            if l1_current < len(l1) - 1:
                new_list.append(l1[l1_current])
                l1_current += 1
        elif l2_current < len(l2) and l2[l2_current] <= l1[l1_current]:
            if l2_current < len(l2):
                new_list.append(l2[l2_current])
                l2_current += 1
    return new_list


if __name__ == "__main__":
    list1 = [[2, 7, 8, 10, 15, 19], [1, 5, 20]]
    list2 = [[1, 3, 8, 12], [2, 7, 8, 9, 10, 12]]
    for i in range(len(list1)):
        print("{} + {} = {}".format(list1[i], list2[i], merge_sorted_lists(list1[i], list2[i])))
