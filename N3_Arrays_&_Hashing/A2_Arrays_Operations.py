
array = [1,2,3,4,5]

# Array Traversal - Process of visiting all the elements of the array once. 

for i in range(len(array)):
    print(array[i], end = " ")
print()
                # Time Complexity:  O(n)
                # Space Complexity: O(1)


# Insertion in Array - Process of inserting one or more elements at any position in array. 

array.insert(2, 2.5)                # (position, new_element)
print(f"Updated Array: {array}")

                # Time Complexity:  Best Case = O(1), Average and Worst Case = O(n)
                # Space Complexity: Base Case = O(1), Average and Worst Case = O(n)


# Deletion in Array - Process of deleting an element at any index in an array.

key = 6     # value to delete 

if key in array:
    array.remove(6)
else:
    print("Element not found!")
print(f"Updated Array: {array}")

                # Time Complexity:  Best Case = O(1), Avg and Worst Case = O(n)
                # Space Complexity: Best Case = O(1), Avg and Worst Case = O(n)


# Searching in Array - Traversing over an array and search for an element.

def search_element(array, key):
    for i in range(len(array)):
        if array[i] == key:
            return i
    return -1

if __name__ == "__main__":
    array = (2,4,6)
    result = search_element(array, 4)
    print(f"Key found at index: {result}.")

                # Time Complexity:  Best Case = O(1), Avg and Worst Case = O(n)
                # Space Complexity: O(1)