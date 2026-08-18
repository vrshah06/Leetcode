matrix = eval(input("Enter a 2D matrix: "))
target = int(input("Enter the target value: "))
rows = len(matrix)
cols = len(matrix[0])
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == target:
            print(f"Target {target} found at position ({i}, {j})")
            break
    else:
        continue
    break

#Better Approach
def binarySearch(self,matrix,target):
    low =0
    high = len(matrix)-1
    while low<=high:
        mid = (low+high)//2
        if nums[mid] == target:
            return True
        elif nums[mid]<target:
            low = mid+1
        else:
            high = mid-1
    return False
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        if matrix[i][0]<=target<=matrix[i][m-1]:
            return self.binarySearch(matrix[i],target)
    return False