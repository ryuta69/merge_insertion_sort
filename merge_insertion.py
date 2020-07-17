def merge_insertion_sort(l):
    def binary_search_insertion(sorted_list, item):
        left = 0
        right = len(sorted_list) - 1
        while left < right:
            middle = (left + right) // 2
            if sorted_list[middle] < item:
                left = middle + 1
            else:
                right = middle
        sorted_list.insert(left, item)
        return sorted_list

    def sortlist_2d(list_2d):
        def merge(left, right):
            result = []
            while left and right:
                if left[0][0] < right[0][0]:
                    result.append(left.pop(0))
                else:
                    result.append(right.pop(0))
            return result + left + right

        length = len(list_2d)
        if lngth <= 1:
            return list_2d
        middle = length // 2
        return merge(sortlist_2d(list_2d[:middle]), sortlist_2d(list_2d[middle:]))

    two_paired_list = []
    is_surplus      = False
    for i in range(0, len(l), 2):
        if (i == len(l) - 1):
            is_surplus = True
        else:
            if l[i] < l[i+1]:
                two_paired_list.append([l[i], l[i+1]])
            else:
                two_paired_list.append([l[i+1], l[i]])
    sorted_list_2d = sortlist_2d(two_paired_list)
    result = [i[0] for i in sorted_list_2d]
    result.append(sorted_list_2d[-1][1])

    for i in range(len(sorted_list_2d) - 1):
        pivot = sorted_list_2d[i][1]
        result = binary_search_insertion(result, pivot)
    if is_surplus:
        pivot = l[-1]
        result = binary_search_insertion(result, pivot)

    return result

A = [100, 2000, 999, 2, 5]
print(merge_insertion_sort(A))
B = [1, 11]
print(merge_insertion_sort(C))
C = ['A', 'Z', 'T', 'C']
print(merge_insertion_sort(C))