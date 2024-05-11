def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print("Iteration", i+1, ":", arr)

# Dynamic input from the user for array length
arr_length = int(input("Enter the length of the array: "))

# Dynamic input from the user for array elements
arr_input = input("Enter the elements of the array separated by space: ").split()
arr = [int(x) for x in arr_input]  # Convert input elements to integers

print("Original array:", arr)
selection_sort(arr)
print("Sorted array:", arr)
