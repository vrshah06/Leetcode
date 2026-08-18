nums = eval(input("Enter the array: "))
#Store triplets in a set to avoid duplicates
st = set()
n = len(nums)
#Brute Force Approach
#First loop for the first element
for i in range(n):
    #Second loop for the second element
    for j in range(i+1,n):
        #Third loop for the third element
        for k in range(j+1,n):
            #Check if the sum of the three elements is zero
            if nums[i]+nums[j]+nums[k]==0:
                #Store the triplet in a sorted order to avoid duplicates
                triplet = tuple(sorted([nums[i],nums[j],nums[k]]))
                st.add(triplet)
print("Unique triplets that sum to zero are:", list(st))

#Better Approach
ans = set()
#First loop for the first element
for i in range(n):
    #set to store the elements we have seen so far
    seen = set()
    #Second loop for the second element
    for j in range(i+1,n):
        #calculate the third element that would make the sum zero
        third = -(nums[i]+nums[j])
        #Check if the third element is in the set
        if third in seen:
            #Store the triplet in a sorted order to avoid duplicates
            triplet = tuple(sorted([nums[i], nums[j], third]))
            ans.add(triplet)
        #Add the current element to the set
        seen.add(nums[j])
if nums[i] == 0 and nums.count(0) >= 3:
    ans.add((0, 0, 0))
print("Unique triplets that sum to zero are:", list(ans))
