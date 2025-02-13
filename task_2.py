def quick_select(array, k):
    if k < 0 or k >= len(array):  # Перевірка, чи знаходиться k в допустимих межах
        return Exception("k виходить за межі масиву")
    if len(array) ==1:
        return array[0]
    pivot = array[len(array) // 2]  # Вибираємо pivot як середній елемент
    left = [x for x in array if x < pivot]   # Елементи менші за pivot
    equal = [x for x in array if x == pivot] # Елементи, рівні pivot
    right = [x for x in array if x > pivot]  # Елементи більші за pivot
    print(f"Pivot: {pivot}, Left: {left}, Equal: {equal}, Right: {right}")  # Дебаг
    left_size = len(left)
    equal_size = len(equal)

    if k < left_size:  # Якщо k-й елемент знаходиться у left
        return quick_select(left, k)
    elif k < left_size + equal_size:  # Якщо k знаходиться в equal
        return pivot
    else:  # Якщо k знаходиться у right
        return quick_select(right, k - left_size - equal_size)  # Коригуємо k

array = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
result = quick_select(array, 33)
print(result)
