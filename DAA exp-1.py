import random
import time

# Interpolation Search Function
def interpolation_search(arr, key):
    low = 0
    high = len(arr) - 1
    probes = 0

    while low <= high and key >= arr[low] and key <= arr[high]:

        probes += 1

        # Avoid division by zero
        if arr[high] == arr[low]:
            if arr[low] == key:
                return low, probes
            else:
                return -1, probes

        pos = low + int(
            ((high - low) / (arr[high] - arr[low])) *
            (key - arr[low])
        )

        if pos < 0 or pos >= len(arr):
            return -1, probes

        if arr[pos] == key:
            return pos, probes

        elif arr[pos] < key:
            low = pos + 1

        else:
            high = pos - 1

    return -1, probes


# Dataset Creation
def create_dataset():
    print("\nChoose Dataset Type")
    print("1. Uniform Distribution")
    print("2. Non-Uniform Distribution")

    dataset_type = int(input("Enter choice: "))

    print("\nData Entry Method")
    print("1. Manual Entry")
    print("2. Random Generation")

    method = int(input("Enter choice: "))

    if method == 1:
        arr = list(map(int, input("Enter sorted elements: ").split()))
        arr.sort()

    else:
        n = int(input("Enter number of elements: "))

        if dataset_type == 1:
            start = random.randint(1, 20)
            step = random.randint(2, 10)

            arr = [start + i * step for i in range(n)]

        else:
            arr = sorted([random.randint(1, n * n) for _ in range(n)])

    return arr, dataset_type


# Main Program
print("=== INTERPOLATION SEARCH ===")

arr, dtype = create_dataset()

print("\nDataset:")
print(arr)

key = int(input("\nEnter key to search: "))

start_time = time.perf_counter()

index, probes = interpolation_search(arr, key)

end_time = time.perf_counter()

execution_time = (end_time - start_time) * 1000000  # microseconds

print("\n----- Result -----")

if index != -1:
    print(f"Key {key} found at index {index}")
else:
    print(f"Key {key} not found")

print(f"Number of probes/comparisons: {probes}")
print(f"Execution time: {execution_time:.2f} microseconds")

if dtype == 1:
    print("\nDataset Type: Uniform Distribution")
    print("Expected Performance: Near O(log log n)")
else:
    print("\nDataset Type: Non-Uniform Distribution")
    print("Expected Performance: Can degrade toward O(n)")