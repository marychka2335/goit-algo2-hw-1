def find_min_max(arr):
    if len(arr) == 1:
        return (arr[0], arr[0])
    elif len(arr) == 2:
        return (min(arr[0], arr[1]), max(arr[0], arr[1]))
    
    mid = len(arr) // 2
    left_min_max = find_min_max(arr[:mid])
    right_min_max = find_min_max(arr[mid:])
    
    overall_min = min(left_min_max[0], right_min_max[0])
    overall_max = max(left_min_max[1], right_min_max[1])
    
    return (overall_min, overall_max)

if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    (min_val, max_val) = find_min_max(arr)
    print(f"Min: {min_val}, Max: {max_val}")
