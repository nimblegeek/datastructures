def two_sum(nums: list[int], target: int) -> list[int]:
    # Create a hash table to store numbers and their indices
    num_to_index = {}
    
    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement that would add up to target
        complement = target - num
        
        # Check if the complement exists in our hash table
        if complement in num_to_index:
            # If it exists, we found our solution
            return [num_to_index[complement], i]
        
        # Store the current number and its index
        num_to_index[num] = i
    
    # The problem guarantees exactly one solution, so we won't reach here
    return []

# Example usage:
if __name__ == "__main__":
    # Test cases from the problem statement
    print(two_sum([2,7,11,15], 9))  # Output: [0,1]
    print(two_sum([3,2,4], 6))       # Output: [1,2]
    print(two_sum([3,3], 6))         # Output: [0,1]