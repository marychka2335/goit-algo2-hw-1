import random

def quick_select(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = arr[random.randint(0, len(arr) - 1)]

    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]

    if k < len(lows):
        return quick_select(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quick_select(highs, k - len(lows) - len(pivots))

if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    k = 3  # Пошук 3-го найменшого елемента (індекс 2)
    kth_smallest = quick_select(arr, k-1)
    print(f"{k}-й найменший елемент: {kth_smallest}")
