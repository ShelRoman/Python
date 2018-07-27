def bubble_sort(list_l):
    while True:
        is_changes_made = False
        for i in range(1, len(list_l)):
            if list_l[i] < list_l[i - 1]:
                list_l[i], list_l[i - 1] = list_l[i - 1], list_l[i]
                is_changes_made = True
        if not is_changes_made:
            break
    return list_l


def insertion_sort(list_l):
    for i in range(1, len(list_l)):
        x = list_l[i]
        j = i - 1
        while j >= 0 and x < list_l[j]:
            list_l[j + 1] = list_l[j]
            j -= 1
        list_l[j + 1] = x
    return list_l


def selection_sort(list_l):
    for i in range(len(list_l)):
        min_i = i
        for j in range(i, len(list_l)):
            if list_l[j] < list_l[min_i]:
                min_i = j
        list_l[i], list_l[min_i] = list_l[min_i], list_l[i]
    print(list_l)


def _merge(left, right):
    res = []
    while len(left) or len(right):
        if len(left) and len(right):
            if left[0] < right[0]:
                res.append(left.pop(0))
            else:
                res.append(right.pop(0))
        elif len(left):
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    return res


def merge_sort(list_l):
    return list_l if len(list_l) <= 1 else _merge(merge_sort(list_l[:len(list_l) // 2]),
                                                  merge_sort(list_l[len(list_l) // 2:]))
