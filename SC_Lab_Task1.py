def binarySearchRecursive(arr, target, left, right):
    """
    Recursively searches for the target in the sorted array.

    Args:
        arr (list): The sorted array.
        target: The value to search.
        left (int): The left index of the search range.
        right (int): The right index of the search range.

    Returns:
        int: The index of the target value if found, or -1 if not found.
    """
    if arr is None or len(arr) == 0:  # Check if the array is None or empty
        return -1
    
    if left > right:  # Base case: if the search range is empty, target is not found
        return -1

    mid = left + (right - left) // 2  # Calculate the middle index of the current range

    if arr[mid] == target:  # If the target is found at the middle index
        return mid
    
    elif arr[mid] > target:  # If the target is smaller than the middle value, search left half
        return binarySearchRecursive(arr, target, left, mid - 1)
    else:  # If the target is larger than the middle value, search right half
        return binarySearchRecursive(arr, target, mid + 1, right)


def binarySearchAllIndices(arr, target, left, right):
    """
    Finds all indices of the target in the sorted array.

    Args:
        arr (list): The sorted array.
        target: Value to search for.
        left (int): The left index of the search range.
        right (int): The right index of the search range.

    Returns:
        list: A list of indices where the target appears, or an empty list if not found.
    """
    if arr is None or len(arr) == 0:  # Check if the array is None or empty
        return []

    if left > right:  # Base case: if the search range is empty, return an empty list
        return []

    mid = left + (right - left) // 2  # Calculate the middle index of the current range

    if arr[mid] == target:  # If the target is found at the middle index
        indices = [mid]  # Initialize a list with the current index
        
        # Recursively find indices in the left half of the array
        indices.extend(binarySearchAllIndices(arr, target, left, mid - 1))
        
        # Recursively find indices in the right half of the array
        indices.extend(binarySearchAllIndices(arr, target, mid + 1, right))
        
        # Return a sorted list of all indices where the target is found
        return sorted(indices)
    
    elif arr[mid] > target:  # If the target is smaller than the middle value, search left half
        return binarySearchAllIndices(arr, target, left, mid - 1)
    else:  # If the target is larger than the middle value, search right half
        return binarySearchAllIndices(arr, target, mid + 1, right)
