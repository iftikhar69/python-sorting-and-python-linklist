import random
import time
import copy
from typing import List

def bubble_sort(arr: List[int]) -> None:
    size = len(arr)
    for passnum in range(size - 1):
        for idx in range(size - passnum - 1):
            if arr[idx] > arr[idx + 1]:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]

def insertion_sort(arr: List[int]) -> None:
    for idx in range(1, len(arr)):
        temp = arr[idx]
        pos = idx - 1
        while pos >= 0 and arr[pos] > temp:
            arr[pos + 1] = arr[pos]
            pos -= 1
        arr[pos + 1] = temp

def selection_sort(arr: List[int]) -> None:
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def quick_sort(arr: List[int]) -> None:
    def _quick_sort(items, left, right):
        if left < right:
            pivot_idx = partition(items, left, right)
            _quick_sort(items, left, pivot_idx - 1)
            _quick_sort(items, pivot_idx + 1, right)

    def partition(items, left, right):
        pivot = items[right]
        i = left - 1
        for j in range(left, right):
            if items[j] <= pivot:
                i += 1
                items[i], items[j] = items[j], items[i]
        items[i + 1], items[right] = items[right], items[i + 1]
        return i + 1

    if arr:
        _quick_sort(arr, 0, len(arr) - 1)

def counting_sort(arr: List[int]) -> None:
    if not arr:
        return
    min_val = min(arr)
    max_val = max(arr)
    offset = -min_val
    count = [0] * (max_val - min_val + 1)
    for num in arr:
        count[num + offset] += 1
    idx = 0
    for i, cnt in enumerate(count):
        value = i - offset
        for _ in range(cnt):
            arr[idx] = value
            idx += 1

def _counting_sort_exp(arr: List[int], exp: int) -> None:
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        idx = (arr[i] // exp) % 10
        count[idx] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        idx = (arr[i] // exp) % 10
        output[count[idx] - 1] = arr[i]
        count[idx] -= 1
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr: List[int]) -> None:
    # Handle negatives by separating negatives and positives.
    if not arr:
        return
    positives = [x for x in arr if x >= 0]
    negatives = [-x for x in arr if x < 0]  # store abs for sorting

    if positives:
        max_pos = max(positives)
        exp = 1
        while max_pos // exp > 0:
            _counting_sort_exp(positives, exp)
            exp *= 10

    if negatives:
        max_neg = max(negatives)
        exp = 1
        while max_neg // exp > 0:
            _counting_sort_exp(negatives, exp)
            exp *= 10
        # negatives were sorted by absolute value; convert back and reverse
        negatives = [-x for x in reversed(negatives)]

    # combine negatives then positives
    arr[:] = negatives + positives

def merge_sort(arr: List[int]) -> None:
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def bucket_sort(arr: List[int]) -> None:
    if not arr:
        return
    min_val = min(arr)
    max_val = max(arr)
    bucket_count = max(1, len(arr))
    range_width = max_val - min_val + 1
    buckets = [[] for _ in range(bucket_count)]
    for num in arr:
        idx = int((num - min_val) / range_width * (bucket_count - 1))
        buckets[idx].append(num)
    arr.clear()
    for bucket in buckets:
        insertion_sort(bucket)
        arr.extend(bucket)

SORT_METHODS = {
    '1': ("Bubble Sort", bubble_sort),
    '2': ("Insertion Sort", insertion_sort),
    '3': ("Selection Sort", selection_sort),
    '4': ("Quick Sort", quick_sort),
    '5': ("Counting Sort", counting_sort),
    '6': ("Radix Sort", radix_sort),
    '7': ("Merge Sort", merge_sort),
    '8': ("Bucket Sort", bucket_sort),
}

def print_menu() -> None:
    print("\nChoose sorting method:")
    for k, (name, _) in SORT_METHODS.items():
        print(f"{k}. {name}")
    print("9. Run all (compare times)")
    print("0. Back to main")

def get_array_dynamic() -> List[int]:
    while True:
        print("\nArray input options:")
        print("1. Enter numbers manually (space separated)")
        print("2. Generate random array by size and range")
        choice = input("Choose (1 or 2): ").strip()
        if choice == '1':
            raw = input("Enter numbers separated by spaces: ").strip()
            if not raw:
                print("No numbers entered. Try again.")
                continue
            try:
                arr = [int(x) for x in raw.split()]
            except ValueError:
                print("Invalid input. Only integers allowed.")
                continue
            return arr
        elif choice == '2':
            try:
                size = int(input("Enter array size (positive integer): ").strip())
                if size <= 0:
                    print("Size must be positive.")
                    continue
            except ValueError:
                print("Invalid size.")
                continue
            try:
                lo = int(input("Enter min value (default 0): ").strip() or "0")
                hi = int(input("Enter max value (default 100): ").strip() or "100")
            except ValueError:
                print("Invalid range values.")
                continue
            if lo > hi:
                print("Min cannot be greater than max.")
                continue
            arr = [random.randint(lo, hi) for _ in range(size)]
            print(f"Generated array of size {size}.")
            return arr
        else:
            print("Invalid option.")

def display_array(arr: List[int], max_display: int = 40) -> None:
    n = len(arr)
    if n == 0:
        print("[]")
        return
    if n <= max_display:
        print(arr)
    else:
        head = arr[:10]
        tail = arr[-10:]
        print(f"size={n} -> {head} ... {tail}")

def time_and_run(name: str, func, arr: List[int], ascending: bool) -> float:
    a = copy.copy(arr)
    start = time.perf_counter()
    func(a)
    if not ascending:
        a.reverse()
    elapsed = time.perf_counter() - start
    print(f"\n{name} completed in {elapsed:.6f}s")
    print("Result preview:")
    display_array(a)
    return elapsed

def run_all_sorts(arr: List[int], ascending: bool) -> None:
    base = arr
    results = {}
    for key, (name, func) in SORT_METHODS.items():
        elapsed = time_and_run(name, func, base, ascending)
        results[name] = elapsed
    print("\nSummary (seconds):")
    for name, t in sorted(results.items(), key=lambda x: x[1]):
        print(f"{name:15s} : {t:.6f}")

def main_menu():
    current = get_array_dynamic()
    while True:
        print("\nMAIN MENU")
        print("1. Change array")
        print("2. Sort menu")
        print("3. Show current array")
        print("4. Exit")
        cmd = input("Choose option: ").strip()
        if cmd == '1':
            current = get_array_dynamic()
        elif cmd == '2':
            while True:
                print_menu()
                choice = input("Enter option (0-9): ").strip()
                if choice == '0':
                    break
                if choice == '9':
                    asc = input("Ascending? (y/n, default y): ").strip().lower() != 'n'
                    run_all_sorts(current, asc)
                    continue
                entry = SORT_METHODS.get(choice)
                if not entry:
                    print("Invalid option.")
                    continue
                name, func = entry
                asc = input("Ascending? (y/n, default y): ").strip().lower() != 'n'
                print("\nOriginal preview:")
                display_array(current)
                arr_copy = copy.copy(current)
                time_and_run(name, func, arr_copy, asc)
        elif cmd == '3':
            print("Current array preview:")
            display_array(current)
        elif cmd == '4':
            print("Exiting.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main_menu()

