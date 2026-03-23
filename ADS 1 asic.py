def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n - 1)
    print(n, end=" ")


def print_n_to_1(n):
    if n == 0:
        return
    print(n, end=" ")
    print_n_to_1(n - 1)


def sum_natural(n):
    if n == 0:
        return 0
    return n + sum_natural(n - 1)


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)


def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)


def count_digits(n):
    if 0 <= n <= 9:
        return 1
    return 1 + count_digits(n // 10)


def reverse_number(n):
    if n == 0:
        return
    print(n % 10, end="")
    reverse_number(n // 10)


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def is_palindrome(s, left, right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return is_palindrome(s, left + 1, right - 1)


def sum_array(arr, n):
    if n == 0:
        return 0
    return sum_array(arr, n - 1) + arr[n - 1]


def max_array(arr, n):
    if n == 1:
        return arr[0]
    return max(arr[n - 1], max_array(arr, n - 1))


def count_occurrences(arr, n, target):
    if n == 0:
        return 0
    return count_occurrences(arr, n - 1, target) + (1 if arr[n - 1] == target else 0)


def linear_search(arr, index, target):
    if index == len(arr):
        return False
    if arr[index] == target:
        return True
    return linear_search(arr, index + 1, target)


def is_sorted(arr, n):
    if n == 0 or n == 1:
        return True
    if arr[n - 2] > arr[n - 1]:
        return False
    return is_sorted(arr, n - 1)


def binary_search(arr, left, right, target):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, left, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, right, target)


print("Task 1:")
print_1_to_n(5)
print("\n")

print("Task 2:")
print_n_to_1(5)
print("\n")

print("Task 3:")
print(sum_natural(5))
print()

print("Task 4:")
print(factorial(5))
print()

print("Task 5:")
print(power(2, 4))
print()

print("Task 6:")
print(sum_digits(572))
print()

print("Task 7:")
print(count_digits(5729))
print()

print("Task 8:")
reverse_number(1234)
print("\n")

print("Task 9:")
print(fibonacci(6))
print()

print("Task 10:")
print("Palindrome" if is_palindrome("level", 0, len("level") - 1) else "Not palindrome")
print("Palindrome" if is_palindrome("hello", 0, len("hello") - 1) else "Not palindrome")
print()

print("Task 11:")
arr1 = [3, 5, 2, 7]
print(sum_array(arr1, len(arr1)))
print()

print("Task 12:")
arr2 = [4, 9, 1, 7, 3]
print(max_array(arr2, len(arr2)))
print()

print("Task 13:")
arr3 = [1, 2, 3, 2, 2, 5]
print(count_occurrences(arr3, len(arr3), 2))
print()

print("Task 14:")
arr4 = [4, 7, 1, 9, 3]
print("Found" if linear_search(arr4, 0, 9) else "Not found")
print()

print("Task 15:")
arr5 = [1, 2, 4, 7, 9]
arr6 = [1, 5, 3, 8]
print("Sorted" if is_sorted(arr5, len(arr5)) else "Not sorted")
print("Sorted" if is_sorted(arr6, len(arr6)) else "Not sorted")
print()

print("Task 16:")
arr7 = [1, 3, 5, 7, 9, 11]
index = binary_search(arr7, 0, len(arr7) - 1, 7)
if index != -1:
    print("Element found at index", index)
else:
    print("Element not found")