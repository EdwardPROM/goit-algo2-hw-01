def serch_max_and_min(array):
    if len(array) == 1:
        return array[0], array[0]
    if len(array) == 2:
        return min(array[0], array[1]), max(array[0], array[1])
    devide = len(array) // 2
    left = serch_max_and_min(array[:devide])
    right = serch_max_and_min(array[devide:])
    return min(left[0], right[0]), max(left[1], right[1])


array = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]

result = serch_max_and_min(array)
print(result)