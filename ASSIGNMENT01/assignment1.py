import random
import time


def bubble_sort(my_list):
    steps = 0
    n = len(my_list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            steps += 1  
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                steps += 3  
    return steps

def selection_sort(my_list):
    steps = 0
    n = len(my_list)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            steps += 1  
            if my_list[j] < my_list[min_idx]:
                min_idx = j
        if min_idx != i:
            my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]
            steps += 3 
    return steps

def insertion_sort(my_list):
    steps = 0
    for i in range(1, len(my_list)):
        key = my_list[i]
        j = i - 1
        steps += 1  
        while j >= 0 and my_list[j] > key:
            my_list[j + 1] = my_list[j]
            j -= 1
            steps += 2  
        my_list[j + 1] = key
        steps += 1  
    return steps

def insertion_sort_sublist(my_list, left, right):
    steps = 0
    for i in range(left + 1, right + 1):
        key = my_list[i]
        j = i - 1
        steps += 1
        while j >= left and my_list[j] > key:
            my_list[j + 1] = my_list[j]
            j -= 1
            steps += 2
        my_list[j + 1] = key
        steps += 1
    return steps


def quick_sort(my_list):
    steps = 0

    def median_of_three(arr, low, high):
        mid = (low + high) // 2
        a, b, c = arr[low], arr[mid], arr[high]
        if (a - b) * (c - a) >= 0:
            return low
        elif (b - a) * (c - b) >= 0:
            return mid
        else:
            return high

    def partition(arr, low, high):
        nonlocal steps
        pivot_index = median_of_three(arr, low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        steps += 3  
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            steps += 1 
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                steps += 3  
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        steps += 3  
        return i + 1

    def quick_sort_recursive(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_recursive(arr, low, pi - 1)
            quick_sort_recursive(arr, pi + 1, high)

    if len(my_list) > 1:
        quick_sort_recursive(my_list, 0, len(my_list) - 1)
    return steps



def main():
   
    rand_list = [random.randint(0, 1000) for _ in range(100)]
    test_cases = {
        "Best Case": sorted(rand_list),
        "Worst Case": sorted(rand_list, reverse=True),
        "Average Case": rand_list
    }

    print("----- T(n) (steps) for each sorting algorithm -----")
    for case_name, lst in test_cases.items():
        print(f"\n{case_name}:")
        for sort_func in [bubble_sort, selection_sort, insertion_sort, quick_sort, lambda l: insertion_sort_sublist(l, 0, len(l)-1)]:
            temp_list = lst.copy()
            steps = sort_func(temp_list)
            print(f"{sort_func.__name__}: steps={steps}, sorted correctly={temp_list == sorted(lst)}")

   
    sizes = [10, 50, 100, 500, 1000]
    print("\n Timing algorithms")
    print(f"{'n':>6} | {'Bubble':>10} | {'Selection':>10} | {'Insertion':>10} | {'Quick':>10}")
    print("-" * 55)
    for n in sizes:
        lst = list(range(n, 0, -1))  # worst-case
        t_bubble = time.time()
        bubble_sort(lst.copy())
        t_bubble = time.time() - t_bubble

        t_selection = time.time()
        selection_sort(lst.copy())
        t_selection = time.time() - t_selection

        t_insertion = time.time()
        insertion_sort(lst.copy())
        t_insertion = time.time() - t_insertion

        t_quick = time.time()
        quick_sort(lst.copy())
        t_quick = time.time() - t_quick

        print(f"{n:6} | {t_bubble:10.6f} | {t_selection:10.6f} | {t_insertion:10.6f} | {t_quick:10.6f}")

if __name__ == "__main__":
    main()