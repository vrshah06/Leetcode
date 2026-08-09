class Solution:
    # Function to find the minimum element using linear search
    def findMin(self, nums):

        # Initialize answer with a large number
        min_val = float('inf')

        # Traverse each element
        for i in range(len(nums)):

            # Update minimum value
            min_val = min(min_val, nums[i])

        # Return the result
        return min_val

# Input array
nums = [4, 5, 6, 7, 0, 1, 2]

# Create object of Solution
sol = Solution()

# Call function and store result
result = sol.findMin(nums)

# Output the result
print("Minimum element is", result)
